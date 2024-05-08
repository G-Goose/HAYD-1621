import numpy as np
import pandas as pd
import tensorflow as tf
from keras import img_to_array, preprocess_input
from tensorflow import tile
from tensorflow import expand_dims

def loading_model():
    path = "/Users/gregory/code/G-Goose/HAYD-1621/test_trained_model"
    model = tf.keras.models.load_model(path)
    return model

def input_process(pict):
    pict.resize((254, 254))
    pict = img_to_array(pict)
    pict = tile(pict, [1, 1, 3])
    pict = expand_dims(pict, axis=0)
    preproc_pict = preprocess_input(pict)
    return preproc_pict

def pred(preproc_pict):
    model = loading_model()
    y_pred = model.predict(preproc_pict)
    return y_pred # check the output format

# model = loading_model()
#    X_processed = input_process(X_pred)
#    y_pred = model.predict(X_processed)

# def evaluate():
#    return 0.99

if __name__ == '__main__':
    evaluate()
