from compressor import Compressor

class LZMA(Compressor):
    def C(self, str) -> str:
        return ''

    def D(self, str) -> str:
        return ''