import csv
from interfaces.data_source import ILogSource

class CsvLogSource(ILogSource):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_logs(self) -> list[str]:
        logs = []
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as f:
                # ใช้ DictReader เพื่ออ่านข้อมูลตามหัวคอลัมน์ (Header)
                reader = csv.DictReader(f)
                for row in reader:
                    # จัดรูปแบบข้อความจาก CSV (สมมติว่ามีคอลัมน์ timestamp, level, message)
                    line = f"{row.get('timestamp', '')} [{row.get('level', '')}] {row.get('message', '')}"
                    logs.append(line)
        except FileNotFoundError:
            return ["Error: CSV file not found."]
        return logs