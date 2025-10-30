from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration for the Data Ingestion Stage.
    """
    download_location: Path
    workspace: str
    project_name: str
    version: int
    format: str

@dataclass(frozen=True)
class DataValidationConfig:
    """
    Configuration for the Data Validation Stage.
    """
    data_dir: Path 
    required_files: list 
    status_file: Path