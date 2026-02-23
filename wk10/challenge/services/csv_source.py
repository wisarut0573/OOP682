import csv
from interfaces.data_source import ILogSource
from typing import List

class CsvLogSource(ILogSource):
    def __init__(self, filepath):
        self.filepath = filepath
        
    def get_logs(self) -> List[str]:
        logs = []
        try:
            with open(self.filepath, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    # นำข้อมูลแต่ละคอลัมน์มาต่อกันด้วย comma
                    logs.append(", ".join(row))
            return logs
        except FileNotFoundError:
            return ["Error: CSV File not found"]