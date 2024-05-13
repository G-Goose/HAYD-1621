from fastapi import FastAPI, UploadFile, File
from hayd1621.model import output_api, pred, loading_model, input_process
import tensorflow as tf
from PIL import Image


import numpy as np
import io

app = FastAPI()

app.state.model = loading_model()



@app.get("/")
def index():
    return {"status": "ok"}

@app.post('/upload_your_nice_face')
async def receive_image(img: UploadFile):
    ### Receiving and processing the image
    request_object_content = await img.read()
    img = Image.open(io.BytesIO(request_object_content))
    print('* * * before-processing completed * * *')

    ### Predicting the emotion
    predicted_emotion = output_api(pred(preproc_pict = input_process(img), model = app.state.model))

    return predicted_emotion
