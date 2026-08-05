from compression_algos.compressor import Compressor
from compression_distances.metric import Metric

# CLM https://www.researchgate.net/publication/3085076_Shared_Information_and_Program_Plagiarism_Detection, cité dans https://arxiv.org/pdf/2206.11573
class CLM(Metric):
    def dist(self, C: Compressor, x: str, y: str, break_string:bool=False, break_char:str='*') -> float:
        cx = len(C.C(x))
        cy = len(C.C(y))
        cxy = len(C.C(x+y)) if not break_string else len(C.C(x+break_char+y))
        return 1.0 - float(cx + cy - cxy) / cxy

    def d(self, C:Compressor, x: str, y: str, break_string:bool=False, break_char:str='*') -> float:
            cx = C.C_len(x)
            cy = C.C_len(y)
            cxy = C.C_len(x+y) if not break_string else C.C_len(x+break_char+y)
            return 1.0 - float(cx + cy - cxy) / cxy