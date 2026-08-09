from tests import test_representations
from benchmark.convert_datasets import load_compress_wine, load_compress_iris, load_compress_breast_cancer, nncr_create_dict, nncr_information_compression_transformation
from compression_algos.legacy_lzw import LZW
from compression_distances.cdm import CDM
from compression_distances.clm import CLM
from compression_distances.unproven_cd import UNPROVEN_CD
import benchmark.models
import numpy as np
#test_representations.run_tests()

#load_compress_wine()
#load_compress_iris()
#load_compress_breast_cancer()


#print(UNPROVEN_CD().d(LZW(), '111121111', '111121111', True))

#X =np.array([[3, 2, 3], [5, 2, 6], [6,5,4]])

# print(X)
# print(nncr_create_dict(X))

# print(nncr_information_compression_transformation(X))