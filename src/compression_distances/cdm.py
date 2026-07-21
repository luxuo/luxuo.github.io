from compression_algos.compressor import Compressor
from metric import Metric

# Compression-based dissimilarity measurement https://www.researchgate.net/publication/3085076_Shared_Information_and_Program_Plagiarism_Detection TODO check si c la bonne source
class CDM(Metric):
    def dist(self, C: Compressor, x: str, y: str) -> float:
        cx = len(C.C(x))
        cy = len(C.C(y))
        cxy = len(C.C(x+y))
        return float(cx + cy) / cxy