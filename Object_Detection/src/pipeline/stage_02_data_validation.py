from src.config.configuration import ConfigurationManager
from src.components.data_validation import DataValidation
from src.utils.logging_setup import logger

class DataValidationPipeline:
    """
    Pipeline stage for data validation.
    """
    def __init__(self, config_manager: ConfigurationManager):
        self.config = config_manager.get_data_validation_config()
        
    def run_pipeline(self):
        try:
            logger.info("Starting data validation pipeline")
            data_validation = DataValidation(config=self.config)
            data_validation.validate_all_files_exist()
            logger.info("Data validation pipeline completed")
            
        except Exception as e:
            logger.error(f"Error in data validation pipeline: {e}", exc_info=True)
            raise e