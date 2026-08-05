from .compressor import Compressor
import math
class LZ78_WORST_CASE(Compressor):
    def C(self, str) -> str:
        pass

    def D(self, str) -> str:
        pass

    def C_len(self, str) -> int:
        # pire cas pour représentation nncr
        c = len(str)
        if c == 0:
            return 0
        return math.ceil(c**0.5 * math.log2(c) / 2**0.5)