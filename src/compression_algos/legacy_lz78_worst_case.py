from .compressor import Compressor
import math
class LZ78_WORST_CASE(Compressor):
    def C(self, x) -> str:
        pass

    def D(self, x) -> str:
        pass

    def C_len(self, x) -> int:
        # pire cas pour représentation nncr
        c = len(x)
        if c == 0:
            return 0
        return math.ceil(c**0.5 * math.log2(c) / 2**0.5)