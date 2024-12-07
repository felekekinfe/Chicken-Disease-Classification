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
def read_yaml(yaml_path:Path)-> ConfigBox:

    try:

        with open(yaml_path,'r') as yaml_file:
            data=yaml.safe_load(yaml_file)
            logger.info(f'Reading yaml file from:{yaml_path}')
            return ConfigBox(data)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
@ensure_annotations
def create_directory(directory_path:list,verbose=True):

    for path in directory_path:
        os.makedirs(path,exist_ok=True)

        

@ensure_annotations
def save_json(path,data):

    with open(path,'w') as p:
        json.dump(data,p,indent=4)
        logger.info(f'json file created at{path}')

@ensure_annotations
def get_size(path):

    size_in_kb=os.path.getsize(path)//1024

    return f'{size_in_kb}KB'