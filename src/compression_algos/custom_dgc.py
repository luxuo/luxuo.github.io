from collections import Counter
import math

def merge_characters(ancestor, prev_dict, prev_dict_index):
    # make disappear the character
    # search for all occurrences of ancestor
    # ancestors -len(ancestor)

    new_prev_dict = prev_dict.copy()
    new_prev_index_dict = prev_dict_index.copy()

    for successor in prev_dict.keys():
        
        ancestor_index = prev_dict[successor].index(ancestor) if ancestor in prev_dict[successor] else -1
        while ancestor_index != -1:
            # remove ancestor from successor
            # remove ancestor index from successor
            successor_ancestor_index = prev_dict_index[successor].pop(ancestor_index)
            new_ancestor_index = successor_ancestor_index - len(prev_dict[successor].pop(ancestor_index))
            new_ancestor_index_index = prev_dict_index[ancestor].index(new_ancestor_index)
            prev_dict_index[ancestor].pop(new_ancestor_index_index)
            # remove new ancestor from ancestor
            new_ancestor = prev_dict[ancestor].pop(new_ancestor_index_index)

            # cleanup dict if possible TODO NEEDS ANOTHER CHECK FOR CHAR
            if len(prev_dict[successor]) == 0:
                del new_prev_dict[successor]
            if len(prev_dict_index[successor]) == 0:
                del new_prev_index_dict[successor]
            if len(prev_dict[ancestor]) == 0:
                del new_prev_dict[ancestor]
            if len(prev_dict_index[ancestor]) == 0:
                del new_prev_index_dict[ancestor]

            # insert combined ancestor-successor with index
            new_key = ancestor + successor
            # new key insertion
            if new_key not in new_prev_dict:
                new_prev_dict[new_key] = []
                new_prev_index_dict[new_key] = []
            new_prev_dict[new_key].append(new_ancestor)
            new_prev_index_dict[new_key].append(new_ancestor_index)

            # replace successor's successor's ancestor as ancestor-successor
            successor_successor_index = successor_ancestor_index + len(successor)
             # find successor
            successor_successor_index_index = -1
            successor_successor = ''
            for key,arr in prev_dict_index.items():
                if successor_successor_index in arr:
                    successor_successor = key
                    successor_successor_index_index = prev_dict_index[key].index(successor_successor_index)
                    break
            new_prev_index_dict[successor_successor][successor_successor_index_index] = successor_ancestor_index
            new_prev_dict[successor_successor][successor_successor_index_index] = new_key


            # update ancestor_index
            ancestor_index = prev_dict[successor].index(ancestor) if ancestor in prev_dict[successor] else -1
    return new_prev_dict, new_prev_index_dict




def createAncestorDict(s):
    counter = Counter(s)
    prev_dict = {}
    prev_index_dict = {}

    for i in range(len(s)-1): # O(n)
        # new key in dict
        if s[i+1] not in prev_dict.keys():
            prev_dict[s[i+1]] = []
            prev_index_dict[s[i+1]] = []
        
        # add prev
        prev_dict[s[i+1]].append(s[i])
        prev_index_dict[s[i+1]].append(i)

    # calculate entropy of next characters
    entropy_dict = {}
    for ancestor in counter.keys(): # O(n²)
        if ancestor not in entropy_dict:
            entropy_dict[ancestor] = 0
        for count_from in counter.keys():
            char_prob = Counter(prev_dict[count_from])[ancestor] / counter[ancestor]
            entropy_dict[ancestor] -= 0 if char_prob == 0 else char_prob * math.log2(char_prob)

    # FIRST VERSION: check for zeroes
    for e in entropy_dict.keys():
        if entropy_dict[e] == 0.0:
            # merge characters
            print(prev_dict)
            print(prev_index_dict)
            print()
            prev_dict, prev_index_dict = merge_characters(e, prev_dict, prev_index_dict)
            
    # merge characters
    # repeat till random
    # TODO

    return prev_dict, prev_index_dict, counter

p, i, c = createAncestorDict('tobeornottobeortobeornot')
print(p)
print(i)
print(c)