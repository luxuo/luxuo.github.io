def createAncestorDict(s: str):
    prev_dict = {}
    for i in range(len(s)-1):
        # new key in dict
        if s[i+1] not in prev_dict.keys():
            prev_dict[s[i+1]] = []
        
        # add prev
        prev_dict[s[i+1]].append(s[i])

        # check
        # TODO

    return prev_dict

print(createAncestorDict('tobeornottobeortobeornot'))