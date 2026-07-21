from abc import ABC, abstractmethod
class Compressor(ABC):
    @abstractmethod
    def C(self, str):
        pass

    @abstractmethod
    def D(self, str):
        pass