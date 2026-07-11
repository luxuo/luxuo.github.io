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

# returns key that surprises most (by shannon entropy)
def min_key(str,dict):
    max_entropy = -1
    min_key = ''
    for key in dict.keys():
        probability = p(str, key, dict)
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
    print(replaced_str, key)
    return [key] + impasse(replaced_str, find_key=find_key)
    #print(max_key(dict))
    #print(min_key(str, dict))




#print(impasse('tobeornottobeortobeornot', max_key_log))
#print(impasse('If weights corresponding to the alphabetically ordered inputs', max_key_log))
print(impasse('11111111111'))
#print(len('tobeornottobeortobeornot'))
#impasse('not' * 8)