from compression_algos.compressor import Compressor
from compression_distances.metric import Metric

# Normalized Compression Distance https://arxiv.org/pdf/cs/0111054
class NCD(Metric):
    def dist(self, C: Compressor, x: str, y: str) -> float:
        cx = len(C.C(x))
        cy = len(C.C(y))
        cxy = len(C.C(x+y))
        return float(cxy - min( cx, cy)) / max(cx, cy)

    def d(self, C:Compressor, x: str, y: str, break_string:bool=False, break_char:str='*') -> float:
        cx = C.C_len(x)
        cy = C.C_len(y)
        cxy = C.C_len(x+y) if not break_string else C.C_len(x+break_char+y)
        return float(cxy - min( cx, cy)) / max(cx, cy,1)