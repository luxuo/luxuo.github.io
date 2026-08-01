from collections import Counter
import math

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