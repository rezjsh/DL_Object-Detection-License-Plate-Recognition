from Object_Detection.src.entity.config_entity import DataIngestionConfig
from src.constants.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.utils.helpers import create_directory, read_yaml_file
from src.utils.logging_setup import logger
from src.core.singleton import SingletonMeta

class ConfigurationManager(metaclass=SingletonMeta):
    def __init__(self, config_file_path: str = CONFIG_FILE_PATH, params_file_path: str = PARAMS_FILE_PATH):
        self.config = read_yaml_file(config_file_path)
        self.params = read_yaml_file(params_file_path)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        logger.info("Getting data ingestion config")
        config = self.config.data_ingestion
        params = self.params.data_ingestion
        logger.info(f"Data ingestion config: {config}")
        logger.info(f"Data ingestion params: {params}")

        dirs_to_create = [config.download_location]
        logger.info(f"Dirs to create: {dirs_to_create}")
        create_directory(dirs_to_create)
        logger.info("Creating data ingestion config")

        data_ingestion_config = DataIngestionConfig(
            download_location=config.download_location,
            workspace=params.workspace,
            project_name=params.project_name,
            version=params.version,
            format=params.format
        )
        logger.info(f"Data ingestion config created: {data_ingestion_config}")
        return data_ingestion_config
