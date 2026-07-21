from compression_algos.compressor import Compressor
from metric import Metric

# Compression-based dissimilarity measurement citation indirecte https://arxiv.org/pdf/2206.11573
class CDM(Metric):
    def dist(self, C: Compressor, x: str, y: str) -> float:
        cx = len(C.C(x))
        cy = len(C.C(y))
        cxy = len(C.C(x+y))
        return float(cx + cy) / cxy