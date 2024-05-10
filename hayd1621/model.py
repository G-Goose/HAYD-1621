import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from tensorflow import tile
from tensorflow import expand_dims
from tensorflow.keras.applications.resnet_v2 import preprocess_input

def loading_model():
    path = "model/2024_05_10_resnet50v2_model.h5"
    model = load_model(path)
    return model

def input_process(pict):
    pict = pict.resize((224, 224))
    print('* * * pict resized * * * ')
    pict = img_to_array(pict)
    print(pict.shape)
    if pict.shape == (224, 224, 3):
        pass
    else:
        pict = tile(pict, [1, 1, 3])
    pict = expand_dims(pict, axis=0)
    preproc_pict = preprocess_input(pict)
    return preproc_pict

def pred(preproc_pict, model):
    y_pred = model.predict(preproc_pict)
    return y_pred # check the output format

# model = loading_model()
#    X_processed = input_process(X_pred)
#    y_pred = model.predict(X_processed)
# def evaluate():
#    return 0.99

if __name__ == '__main__':
    loading_model()
