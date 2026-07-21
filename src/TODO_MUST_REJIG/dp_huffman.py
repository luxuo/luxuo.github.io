from collections import Counter
import math


def f(i,k):
    pass

def bravo(i,k):
    pass

def calculate_entropy(i,k):
    dict = bravo(i,k)
    su = sum(dict.values())
    probabilities = [x/su for x in dict.values()]
    return sum([-math.log2(p)*p for p in probabilities])
    

def dp_huffman(str):
    # split string into list of chars
    chars = [c for c in str]
