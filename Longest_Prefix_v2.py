def longestCommonPrefix(self, strs: List[str]) -> str:

    prefix = ""

    sorted_strs = sorted(strs) #Sort the list so we only have to look at the first and last string


    first = sorted_strs[0]
    last = sorted_strs[-1]


    for i in range(len(min(first, last))): #Compare the first and last string

        if first[i] != last[i]: #As soon as there is a letter that is different we return prefix
            return prefix
        else:
            prefix += i

    return prefix 
                

