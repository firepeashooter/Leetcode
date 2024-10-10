
def longestCommonPrefix(strs: List[str]) -> str:

    prefix = ""

    #Edge case if the first word is empty then there is no common prefix amongst any of them (Or do we want to ignore the blank words?)
    if "" in strs:
        return ""


    for i in range(len(strs[0])): #Iterate through the first word of the list


        cur_letter = strs[0][i]

        for word in strs:

            if i > len(word) - 1: #If ever we reach an index out of bounds return prefix (for when the first word is longer than some of the other ones)
                return prefix

            temp_letter = word[i]

            if temp_letter != cur_letter:
                return prefix

        prefix += cur_letter

    return prefix
