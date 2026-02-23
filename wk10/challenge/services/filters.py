from interfaces.strategy import IFilterStrategy
from typing import List

class ErrorOnlyFilter(IFilterStrategy):
    def filter(self, logs: List[str]) -> List[str]:
        return [l for l in logs if "ERROR" in l]

class NoFilter(IFilterStrategy):
    def filter(self, logs: List[str]) -> List[str]:
        return logs