from interfaces.data_source import ILogSource

class FileLogSource(ILogSource):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_logs(self) -> List[str]:
        with open(self.file_path, 'r') as file:
            return file.readlines()           
        
   