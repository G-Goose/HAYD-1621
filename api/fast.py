from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
from hayd1621.model import input_process, pred # changed
import tensorflow as tf
from PIL import Image


import numpy as np
import cv2
import io

app = FastAPI()

# # Allow all requests (optional, good for development purposes)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods
#     allow_headers=["*"],  # Allows all headers
# )

@app.get("/hello")
def index():
    return {"status": "ok"}

@app.post('/upload_your_nice_face')
async def receive_image(img: UploadFile):
    ### Receiving and processing the image
    # contents = await img.read()
    request_object_content = await img.read()
    img = Image.open(io.BytesIO(request_object_content))
    # img = tf.keras.preprocessing.image.img_to_array(contents)
    print('* * * before-processing completed * * *')
    processed_face = input_process(img)
    print('* * * processing completed * * *')

    ### Predicting the emotion
    # predicted_emotion = pred(processed_face)

    ### Returning the predicted emotion
    # return {'emotion': predicted_emotion}
