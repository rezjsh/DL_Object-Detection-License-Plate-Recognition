from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    download_location: Path
    workspace: str
    project_name: str
    version: int
    format: str
