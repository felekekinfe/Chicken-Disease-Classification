import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(yaml_path):

    try:

        with open(yaml_path,'r') as yaml_file:
            data=yaml.safe_load(yaml_file)
            logger.info(f'Reading yaml file from:{yaml_path}')
            return ConfigBox(data)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        return e
@ensure_annotations
def create_directory(directory_path:list,verbose=True):

    for path in directory_path:
        os.makedirs(path,exist_ok=True)

        if verbose:
            logger.inf(f'directory created at:{path}')


@ensure_annotations
def save_json(path,data):

    with open(path,'w') as p:
        json.dump(data,p,indent=4)
        logger.info(f'json file created at{path}')

@ensure_annotations
def load_json(path):
    with open(path,'r') as f:
        data=json.load(f)
    logger.info(f'json file loaded from{path}')
    return ConfigBox(data)

@ensure_annotations
def decode_image(img_str,file_name):
    img_data=base64.b64decode(img_str)
    with open(file_name, 'wb') as f:
        f.write(img_data)
        f.close()
@ensure_annotations
def encode_image(cropped_img_path):
    with open(cropped_img_path,'rb') as f:
        encoded_img=base64.b64encode(f.read())
    
