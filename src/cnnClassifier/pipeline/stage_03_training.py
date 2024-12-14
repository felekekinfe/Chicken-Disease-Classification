

from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.training import Training
from cnnClassifier import logger

STAGE_NAME='TRAINING'

class TrainingPipeline:
    def __init__(self):
        
        pass
    def main(self):
        config=ConfigurationManager()
        training_config=config.get_training_config()
        training=Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if  __name__=='__main__':
    try:
        logger.info(f'Starting {STAGE_NAME}')
        obj=TrainingPipeline()
        obj.main()
        logger.info(f'Completed {STAGE_NAME}')
    except Exception as e:
        logger.exception(e)
        raise e
