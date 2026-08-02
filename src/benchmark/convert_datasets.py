from sklearn.datasets import load_wine, load_iris, load_breast_cancer
from representations.numerical import bdncr

def load_compress_wine(stop_char = '*'): # convert wine dataset for compression compatibility
    X, y = load_wine(return_X_y=True)
    # unique digits for compression
    unique_digits = [chr(i) for i in range(ord(stop_char)+1, ord(stop_char) + X.shape[1]*2 + 3)]
    # establish max precision (manually done)
    max_precision = 2
    # create new X
    new_X = [stop_char.join([bdncr(X[row,col],max_precision,one=unique_digits[2*col], zero=unique_digits[2*col+1]) for col in range(X.shape[1])]) for row in range(X.shape[0])]
    return new_X, y

def load_compress_iris(stop_char='*'): # convert iris dataset for compression compatibility
    X, y = load_iris(return_X_y=True)
    # unique digits for compression
    unique_digits = [chr(i) for i in range(ord(stop_char)+1, ord(stop_char) + X.shape[1]*2 + 3)]
    # establish max_precision (manually done)
    max_precision = 1
    # create new X
    new_X = [stop_char.join([bdncr(X[row,col],max_precision,one=unique_digits[2*col], zero=unique_digits[2*col+1]) for col in range(X.shape[1])]) for row in range(X.shape[0])]
    return new_X, y

import numpy as np

def load_compress_breast_cancer(stop_char='*'):
    X, y = load_breast_cancer(return_X_y=True)
    # unique digits for compression
    unique_digits = [chr(i) for i in range(ord(stop_char)+1, ord(stop_char) + X.shape[1]*2 + 3)]
    # establish max_precision (manually done)
    max_precision = 1
    X = np.abs(X)[X > 0]
    print(np.min(X))
    # create new X
    # new_X = [stop_char.join([bdncr(X[row,col],max_precision,one=unique_digits[2*col], zero=unique_digits[2*col+1]) for col in range(X.shape[1])]) for row in range(X.shape[0])]
    # print(new_X)
    # return new_X, y
