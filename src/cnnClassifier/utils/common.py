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

