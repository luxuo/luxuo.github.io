from collections import Counter
import math
def calculate_probabilities(str):
    c = Counter(str)
    total = float(sum(c.values()))
    return [count / total for count in c.values()]

str = "tobeornottobeortobeornot"
ps = calculate_probabilities(str)
information = [-math.log2(p) for p in ps]
something = [i/p for i,p in zip(information,ps)]
print(ps)
print(information)
print(something)
print(sum(something))