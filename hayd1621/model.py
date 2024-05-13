import os
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from tensorflow import tile
from tensorflow import expand_dims
from tensorflow.keras.applications.resnet_v2 import preprocess_input
from itertools import islice

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
    ### Predicting the emotion
    predicted_emotions = model.predict(preproc_pict)
    vals_list = np.round(predicted_emotions, 2)*100

    return vals_list

def output_api(vals_list):
    ### Creating output dictionary
    class_names = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'sad', 'surprised']
    vals_dict = dict(zip(class_names, vals_list.flatten().tolist()))

    sorted_dict_desc = {k: v for k, v in sorted(vals_dict.items(), key=lambda item: item[1], reverse=True)}
    first_value = next(iter(sorted_dict_desc.values()))

    if first_value >= 75:
        output_dict = dict(islice(sorted_dict_desc.items(), 1))
    else:
        output_dict = dict(islice(sorted_dict_desc.items(), 2))
    return output_dict

def output_bq(vals_list):
    return np.argmax(np.array(vals_list))

if __name__ == '__main__':
    loading_model()
