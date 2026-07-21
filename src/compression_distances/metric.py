from abc import ABC, abstractmethod
from compression_algos.compressor import Compressor
class Metric(ABC):
    @abstractmethod
    def dist(self, C: Compressor, x: str, y: str) -> float:
        pass