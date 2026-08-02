from abc import ABC, abstractmethod
class Compressor(ABC):
    @abstractmethod
    def C(self, str:str) -> str: 
        pass

    @abstractmethod
    def D(self, str:str) -> str:
        pass

    @abstractmethod
    def C_len(self, str:str) -> int:
        pass