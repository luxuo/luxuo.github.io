from tests import test_representations
from benchmark.convert_datasets import load_compress_wine, load_compress_iris, load_compress_breast_cancer
from compression_algos.legacy_lzw import LZW
from compression_distances.cdm import CDM
from compression_distances.clm import CLM
from compression_distances.unproven_cd import UNPROVEN_CD
#test_representations.run_tests()

#load_compress_wine()
#load_compress_iris()
#load_compress_breast_cancer()

# s = 'tobeornottobeortobeornot'
# c = LZW()
# a = c.C(s)
# print(a)
# print(c.C_len(s), len(s) * 8)

print(UNPROVEN_CD().d(LZW(), '111121111', '111121111', True))