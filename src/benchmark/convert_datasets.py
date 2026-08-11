from sklearn.datasets import load_wine, load_iris, load_breast_cancer
from representations.numerical import bdncr
import numpy as np
import math

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

def adjust_tolerance(X, tolerance=1e2, tolerances=None):
    if tolerances is None:
        return (X.copy() * tolerance).astype(int)
    X = X.copy()
    for i,tol in zip(range(len(tolerances)), tolerances):
        X[:,i] * tol
    return X.astype(int)

def nncr_create_dict(X, tolerance=1e2, tolerances=None):
    X = adjust_tolerance(X, tolerance=tolerance, tolerances=tolerances)
    values_dict = {}
    j = 0
    # foreach col
    for col in X.T:
        values_dict[j] = []
        arr = np.sort(col)
        while np.count_nonzero(arr) > 0: # while there is still area to be removed
            # get sum
            total = float(sum(arr))
            # minimal information
            min_info = float('inf')
            min_index = -1
            for i in range(len(arr)): # foreach element in sorted column
                # calculate information
                area = float(arr[i]) * (len(arr)-i)
                p = area / total
                information = -math.log2(p) if p != 0.0 else float('inf')
                if information < min_info: # replace minimal information
                    min_info = information
                    min_index = i

            # add value to dict
            if arr[min_index] not in values_dict[j]:
                values_dict[j].append(arr[min_index])
            # subtract value from array
            arr[min_index:] -= arr[min_index]
            # re-sort array
            arr = np.sort(arr)

        # check for minimal delta to be the same as max precision,. if not, replace lowest delta for max precision TODO

        # increment pointer
        j += 1

    # sort all features
    for features in values_dict.values():
        features.sort()
    
    return values_dict

def largest_val(arr, val):
    # assumes sorted array
    for i in range(len(arr)):
        if val < arr[i]:
            return i - 1
    return len(arr)-1

def nncr_information_compression_transformation(X, values_dict, tolerance=1e2, tolerances=None):
    X = adjust_tolerance(X,tolerance=tolerance,tolerances=tolerances)
    #values_dict = nncr_create_dict(X)
    # create new matrix
    features_len = 0
    offsets = [0]
    for arr in values_dict.values():
        features_len += len(arr)
        offsets.append(len(arr) + offsets[-1])
    new_X = np.zeros((X.shape[0], features_len))

    
    # fill in new values
    for row in range(X.shape[0]): # row
        for col in range(X.shape[1]): # cols in untransformed X
            features = values_dict[col] # column features
            # "compress" all values in a BoW sense
            min_val = min(features)
            while X[row,col] >= min_val:
                # subtract largest value possible from features
                ptr = largest_val(features, X[row,col])
                X[row,col] -= features[ptr]
                # increments count of appropriate feature
                new_X[row, offsets[col] + ptr] += 1
                #print(new_X,row,col, 'ptr:',ptr, 'off:',offsets[col], 'feat:',features[ptr])
                #print()

    return new_X
            


    
    