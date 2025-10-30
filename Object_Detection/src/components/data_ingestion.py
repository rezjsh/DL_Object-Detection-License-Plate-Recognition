from roboflow import Roboflow
from src.entity.config_entity import DataIngestionConfig
from src.utils.logging_setup import logger

class RoboflowDatasetDownloader:
    def __init__(self, config: DataIngestionConfig):
        """
        Initialize Roboflow dataset downloader.
        
        Args:
            config (DataIngestionConfig): Configuration object containing dataset details.
        """
        self.config = config
        self.dataset = None

    def download(self, api_key: str) -> str:
        """
        Download the dataset from Roboflow and extract it to the given directory.

        Args:
            api_key (str): Your Roboflow API key.
        
        Returns:
            dataset info object that contains location and metadata
        """
        logger.info("Downloading dataset from Roboflow...")
        rf = Roboflow(api_key=api_key)
        project = rf.workspace(self.config.workspace).project(self.config.project_name)
        version = project.version(self.config.version)
        self.dataset = version.download(model_format=self.config.format, location=self.config.download_location)
        logger.info(f"Dataset downloaded and extracted to: {self.dataset.location}")
        return self.dataset