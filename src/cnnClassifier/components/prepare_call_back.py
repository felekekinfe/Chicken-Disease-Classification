import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from cnnClassifier.entity.config_entity import ModelCallbackConfig

class PrepareCallbacK:
    def __init__(self,config: ModelCallbackConfig):
        self.config=config

    @property
    def create_tb_callback(self):
        timestamp=time.strftime("%Y-%m-%dT%H:%M-%S")
        tb_running_log_dir=os.path.join(self.config.tensorboard_root_log_dir,f'tb_logs_at_{timestamp}')

        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    @property
    def create_checkpoint_callback(self):
        return tf.keras.callbacks.ModelCheckpoint(filepath=self.config.checkpoint_model_filepath,save_best_only=True)
    
    def get_tb_checkpoint_callback(self):
        return [self.create_tb_callback,self.create_checkpoint_callback]
    
