import math

# probability of landing on key sequence in str
def p(str, key, dict):
    return (len(key) * dict[key])/float(len(str))


# find key that covers most area in the sequence
def max_key(_, dict):
    max = -1
    max_key = ''
    for key in dict.keys():
        if (dict[key] -1) * len(key) > max:
            max = (dict[key] - 1) * len(key)
            max_key = key
    return max_key

def max_key_log(_, dict):
    max = -1
    max_key = ''
    for key in dict.keys():
        if math.log(dict[key]) * math.log(len(key)) > max:
            max = math.log(dict[key]) * math.log(len(key))
            max_key = key
    return max_key

def max_key_log_freq(_, dict):
    max = -1
    max_key = ''
    for key in dict.keys():
        if math.log(dict[key]) * math.log(len(key)) > max:
            max = dict[key] * math.log(len(key))
            max_key = key
    return max_key

def max_key_sqrt(_, dict):
    max = -1
    max_key = ''
    for key in dict.keys():
        if math.log(dict[key]) * math.log(len(key)) > max:
            max = math.sqrt(dict[key]) * math.sqrt(len(key))
            max_key = key
    return max_key

def huffman_key(_, dict):
    max_count = -1
    max_key = ''
    for key in dict.keys():
        if len(key) > 1:
            continue
        if dict[key] > max_count:
            max_key = key
            max_count = dict[key]
    return max_key

# returns key that surprises most (by shannon entropy)
# isn't quite what i am looking for
def min_key(str,dict):
    max_entropy = -1
    min_key = ''
    for key in dict.keys():
        probability = p(str, key, dict)
        # this formula is flawed, it requres all probabilities to compute, yet it only computes one
        if -math.log(probability) * probability > max_entropy:
            max_entropy = -math.log(probability) * probability
            min_key = key
    return min_key

# compression algorithm
def impasse(str, find_key=max_key,stop_char='*'):
    dict = {}
    index_dict = {}
    for j in range(1, len(str) + 1):
        for i in range(j-1,-1,-1):
            # constrain substring
            if str[i] == stop_char:
                break
            # initialisation
            if str[i:j] not in dict:
                dict[str[i:j]] = 0
                index_dict[str[i:j]] = -1
            # prevent repeated overlap pattern
            if index_dict[str[i:j]] < i:
                # increment occurence
                dict[str[i:j]] += 1
                index_dict[str[i:j]] = j - 1
            #print(' ' * i + str[i:j])
    #print(dict)

    key = find_key(str, dict)
    replaced_str = str.replace(key, stop_char)

    # exit condition
    if replaced_str == stop_char * len(replaced_str):
        return [key]
    # recursive call
    #print(replaced_str, key) # progress display
    return [key] + impasse(replaced_str, find_key=find_key)
    #print(max_key(dict))
    #print(min_key(str, dict))

def compress(str, tree, zero='_', one='#'):
    code = one
    for key in tree:
        str = str.replace(key, code)
        code = zero + code
    print(str)
    print('<end>'.join(tree) + '<end>' + str)

def calculate_entropy(str, keys, replace_char='*'):
    # calculate probabilities
    probabilities = []
    for key in keys:
        masked_str = str.replace(key,'')
        probabilities.append((len(str) - len(masked_str)) / len(str))
        str = str.replace(key, replace_char * len(key))

    # return entropy of system
    return sum([-math.log2(p) * p for p in probabilities])
    

def calculate_key_entropy(str, keys, replace_char='*'):
    # calculate occurrences
    occurrences = []
    for key in keys:
        count = 0
        while key in str:
            count += 1
            str = str.replace(key, replace_char * len(key), 1)
        occurrences.append(count)

    # return entropy of system
    return sum([-math.log2(p) * p for p in [x / sum(occurrences) for x in occurrences]])

str = 'tobeornottobeortobeornot'#'1111111111101111111'
str = 'hello mellow fellow how is yellow '
str = 'what is love baby dont hurt me dont hurt me no more'
str = 'not' * 8
str = 'what\'s up boys! today we will be shooting clay discs'
str = 'dcode decodes lzw'
with open('/home/pingu/Documents/ift4055/luxuo.github.io/src/english.txt', 'r') as f:
    str = f.read()
key_functions = [max_key_log, max_key_sqrt, huffman_key, max_key_log_freq]
for func in key_functions:
    tree = impasse(str, func)
    print(tree)
    print(calculate_entropy(str, tree))
    print(calculate_key_entropy(str, tree))
