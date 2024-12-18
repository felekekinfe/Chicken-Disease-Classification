from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import BaseModelTrainingPipeline


STAGE_NAME='Data Ingestion Stages'

try:
    logger.info(f'>>>>> stage {STAGE_NAME} started<<<<<<')
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME='Prepare Base Model Stage'

try:
    logger.info(f'>>>>> stage {STAGE_NAME} started<<<<<<')
    prepare_base_model=BaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<')
except Exception as e:
    logger.exception(e)
    raise e
