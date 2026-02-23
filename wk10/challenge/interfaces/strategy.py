from abc import ABC, abstractmethod
from typing import List

# Strategy Interface
class IFilterStrategy(ABC):
    @abstractmethod
    def filter(self, logs: List[str]) -> List[str]:
        pass