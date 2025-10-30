import os
from src.components.data_ingestion import RoboflowDatasetDownloader
from src.utils.logging_setup import logger
from src.config.configuration import ConfigurationManager
from src.entity.config_entity import DataIngestionConfig
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
class DataIngestionPipeline:
    """
    Pipeline stage for data ingestion. Downloads the dataset from Roboflow and extracts it to the given directory.
    """
    def __init__(self, config: ConfigurationManager):
        
        """
        Initializes the DataIngestionPipeline.

        Args:
            config (ConfigurationManager): The configuration manager instance.
        """
        self.config = config.get_data_ingestion_config()
        self.data_ingestion = RoboflowDatasetDownloader(config=self.config)
        

    def run_pipeline(self) -> DataIngestionConfig:
        """
        Executes the data ingestion pipeline.

        Returns:
            DataIngestionConfig: The configuration used for data ingestion,
                                 which contains paths to the ingested data.
        """
        API_KEY = os.getenv("ROBOLFLOW_API_KEY")
        if API_KEY is None:
            raise ValueError("API key not found. Please set ROBOLFLOW_API_KEY in your environment.")
        try:
            
            logger.info("Starting data ingestion pipeline")
            dataset = self.data_ingestion.download(api_key=API_KEY)
            logger.info("Data ingestion pipeline completed")
            return dataset
        except Exception as e:
            logger.error(f"Error in data ingestion pipeline: {e}", exc_info=True)
            raise e

if __name__ == '__main__':
    try:
        config_manager_ingestion = ConfigurationManager()
        data_ingestion_pipeline = DataIngestionPipeline(config_manager=config_manager_ingestion)
        data_ingestion_pipeline.run_pipeline()
    except Exception as e:
        logger.error(f"Error in data ingestion pipeline: {e}")
        raise e