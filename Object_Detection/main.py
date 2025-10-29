from src.utils.logging_setup import logger
from src.config.configuration import ConfigurationManager
from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline
if __name__ == '__main__':
    try:
        config_manager = ConfigurationManager()
        
        # --- Data Ingestion Stage ---
        STAGE_NAME = "Data Ingestion Stage"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_ingestion_pipeline = DataIngestionPipeline(config=config_manager)
        data_ingestion_pipeline.run_pipeline()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logger.error(f"Error occurred during {STAGE_NAME} stage: {e}")
        raise e