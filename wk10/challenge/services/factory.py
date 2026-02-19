from services.file_source import FileLogSource
from services.mock_source import MockLogSource
from services.csv_source import CsvLogSource
from interfaces.data_source import ILogSource

class SourceFactory:
    @staticmethod
    def create_source(source_type: str, path: str = None) -> ILogSource:
        if source_type == "file":
            return FileLogSource(path)
        elif source_type == "mock":
            return MockLogSource()
        elif source_type == "csv":
            return CsvLogSource(path)
        else:
            raise ValueError(f"Unknown source type: {source_type}")