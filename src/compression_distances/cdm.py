from compression_algos.compressor import Compressor
from compression_distances.metric import Metric

# Compression-based dissimilarity measurement citation indirecte https://arxiv.org/pdf/2206.11573
class CDM(Metric):
    def dist(self, C: Compressor, x: str, y: str, break_string:bool=False, break_char:str='*') -> float:
        cx = len(C.C(x))
        cy = len(C.C(y))
        cxy = len(C.C(x+y)) if not break_string else len(C.C(x+break_char+y))
        return float(cx + cy) / cxy