import os
import numpy as np
import pandas as pd
from keras.utils import img_to_array
from keras.models import load_model
from tensorflow import tile
from tensorflow import expand_dims
from keras.applications.imagenet_utils import preprocess_input
from PIL import Image

def loading_model():
    def get_single_file_path(directory):
        # Get all entries in the directory
        entries = os.listdir(directory)
        # Filter to include only files
        files = [file for file in entries if os.path.isfile(os.path.join(directory, file))]
        files =[file for file in files if not (file.endswith(".gitignore") or file.endswith(".Identifier"))]
        print(files)
        # Assert that there is exactly one file
        assert len(files) == 1, f"Expected exactly one file in the directory, but found {len(files)}"
        # Get the full path of the only file
        return os.path.join(directory, files[0])

    path =get_single_file_path("model/")
    model = load_model(path)
    return model

def input_process(pict):
    pict = Image.open(pict)
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
