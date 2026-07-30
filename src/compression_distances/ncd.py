from compression_algos.compressor import Compressor
from compression_distances.metric import Metric

# Normalized Compression Distance https://arxiv.org/pdf/cs/0111054
class NCD(Metric):
    def dist(self, C: Compressor, x: str, y: str) -> float:
        cx = len(C.C(x))
        cy = len(C.C(y))
        cxy = len(C.C(x+y))
        return float(cxy - min( cx, cy)) / max(cx, cy)