from fastapi import FastAPI, UploadFile
from hayd1621.model import output_api, output_bq, pred, loading_model, input_process
from bq import bq

app = FastAPI()

app.state.model = loading_model()

@app.get("/")
def index():
    return {"status": "ok"}

@app.post('/upload_your_nice_face')
async def mood_percent(img: UploadFile):
    ### Receiving and processing the image
    processed_face = input_process(img.file)

    ### Predicting the emotion
    predicted_emotion = output_api(pred(preproc_pict = processed_face, model = app.state.model))

    return predicted_emotion

@app.get('/save_to_bq')
def save_to_bq(val):
    result = bq.update_or_insert_value(new_value=val)
    return {"response": result}
