from abc import ABC, abstractmethod
class Compressor(ABC):
    @abstractmethod
    def C(self, x:str) -> str: 
        pass

    @abstractmethod
    def D(self, x:str) -> str:
        pass

    @abstractmethod
    def C_len(self, x:str) -> float:
        pass