from collections import Counter
import math

def merge_characters(ancestor, ancestors, ancestor_indices, counter):
    # make disappear the character

    new_prev_dict = ancestors.copy()
    new_prev_index_dict = ancestor_indices.copy()

    for successor in ancestors.keys():
        
        ancestor_index = ancestors[successor].index(ancestor) if ancestor in ancestors[successor] else -1
        while ancestor_index != -1:
            # remove ancestor pointer from successor
            ancestor_ptr = ancestor_indices[successor].pop(ancestor_index)
            # remove ancestor from successor
            ancestors[successor].pop(ancestor_index)

            # remove ancestor count from counter
            counter[ancestor] -= 1 # 
            # remove successor count from counter
            counter[successor] -= 1

            # calculate new ancestor pointer
            new_ancestor_ptr = ancestor_ptr - len(ancestor)
            if new_ancestor_ptr == 0: # can't ??????
                print('ancestor:',ancestor,ancestor_ptr, ancestor_index)
                print('successor:',successor)
                print(ancestors)
                print(ancestor_indices)

            # get new ancestor from ancestor pointer
            # 

            new_ancestor_index = ancestor_indices[ancestor].index(new_ancestor_ptr)
            ancestor_indices[ancestor].pop(new_ancestor_index)
            # remove new ancestor from ancestor
            new_ancestor = ancestors[ancestor].pop(new_ancestor_index)

            # cleanup dict if possible
            if len(ancestors[successor]) == 0:
                del new_prev_dict[successor]
            if len(ancestor_indices[successor]) == 0:
                del new_prev_index_dict[successor]
            if len(ancestors[ancestor]) == 0:
                del new_prev_dict[ancestor]
            if len(ancestor_indices[ancestor]) == 0:
                del new_prev_index_dict[ancestor]
            if counter[ancestor] <= 0:
                del counter[ancestor]
            if counter[successor] <= 0:
                del counter[successor]

            # insert combined ancestor-successor with index
            new_key = ancestor + successor
            # new key insertion
            if new_key not in new_prev_dict:
                new_prev_dict[new_key] = []
                new_prev_index_dict[new_key] = []
                counter[new_key] = 0
            new_prev_dict[new_key].append(new_ancestor)
            new_prev_index_dict[new_key].append(new_ancestor_ptr)
            counter[new_key] += 1

            # replace new successor's ancestor as new_key
            new_successor_ptr = ancestor_ptr + len(successor)
             # find new_successor
            new_successor_index = -1
            new_successor = ''
            for key,arr in ancestor_indices.items():
                if new_successor_ptr in arr:
                    new_successor = key
                    new_successor_index = ancestor_indices[key].index(new_successor_ptr)
                    break
            new_prev_index_dict[new_successor][new_successor_index] = ancestor_ptr
            new_prev_dict[new_successor][new_successor_index] = new_key


            # update ancestor_index
            ancestor_index = ancestors[successor].index(ancestor) if ancestor in ancestors[successor] else -1

    return new_prev_dict, new_prev_index_dict




def createAncestorDict(s):
    counter = Counter(s)
    ancestors = {}
    prev_index_dict = {}

    for i in range(len(s)-1): # O(n)
        # new key in dict
        if s[i+1] not in ancestors.keys():
            ancestors[s[i+1]] = []
            prev_index_dict[s[i+1]] = []
        
        # add prev
        ancestors[s[i+1]].append(s[i])
        prev_index_dict[s[i+1]].append(i)

    while True:
        # calculate entropy of next characters
        entropy_dict = {}
        for ancestor in counter.keys(): # O(n²)
            if ancestor not in entropy_dict:
                entropy_dict[ancestor] = 0
            for count_from in counter.keys():
                char_prob = Counter(ancestors[count_from])[ancestor] / counter[ancestor]
                entropy_dict[ancestor] -= 0 if char_prob == 0 else char_prob * math.log2(char_prob)

        # FIRST VERSION: check for zeroes
        stop = True
        for e in entropy_dict.keys():
            if entropy_dict[e] == 0.0:
                # merge characters
                print(e)
                print(ancestors)
                print(prev_index_dict)
                print()
                ancestors, prev_index_dict = merge_characters(e, ancestors, prev_index_dict, counter)
                stop = False
                break

        if stop:
            return ancestors, prev_index_dict, counter
        # repeat till random
        # TODO

def dgc(s, end_char='<end>'): # TODO MAYBE ADD AN END CHAR????
    chars = [c for c in s]

    while True:
        successor_dict = {}
        for i in range(len(chars)): # get next reference
            if chars[i] not in successor_dict: # init list
                successor_dict[chars[i]] = []

            if i + 1 < len(chars):
                successor_dict[chars[i]].append(chars[i+1]) # add next reference
            else:
                successor_dict[chars[i]].append(end_char) # add next reference
        

        entropy_dict = {}
        for char in successor_dict.keys(): # calculate entropy of each char
            counter = Counter(successor_dict[char])
            total = sum(counter.values())
            probabilities = [c / total for c in counter.values()]
            entropy = sum([-math.log2(p) * p if p != 0.0 else 0 for p in probabilities])
            entropy_dict[char] = entropy

        # TODO get which char to merge or stop
        ## VERSION 1 : ONLY MERGE CHARS WITH ENTROPY OF 0
        stop = True
        for char, H in entropy_dict.items():
            if H == 0: # MERGE CHAR with next
                stop = False
                # get all indices of occurrence
                indices = [i for i in range(len(chars)-1) if chars[i] == char] # TODO TO ALTER IF ADDED END CHAR
                print(chars)
                # rebuild array with merged chars
                new_chars = chars[0:indices[0]]
                for j in range(len(indices)):
                    i = indices[j]
                    new_chars.append(chars[i] + chars[i+1]) #  add merged char
                    if i + 2 < len(chars) and j + 1 < len(indices): # add intact chars in between
                        new_chars.extend(chars[i+2:indices[j+1]])
                    else:
                        new_chars.extend(chars[i+2:])

                # update
                chars = new_chars
                break


        if stop:
            return chars



# p, i, c = createAncestorDict('tobeornottobeortobeornot')
# print('Stap')
# print(p)
# print(i)
# print(c)
print(dgc('tobeornottobeortobeornot'))