from compression_algos.compressor import Compressor
from metric import Metric

# CLM https://arxiv.org/pdf/2206.11573 TODO Pas la bonne source
class CLM(Metric):
    def dist(self, C: Compressor, x: str, y: str) -> float:
        cx = len(C.C(x))
        cy = len(C.C(y))
        cxy = len(C.C(x+y))
        return 1.0 - float(cx + cy - cxy) / cxy