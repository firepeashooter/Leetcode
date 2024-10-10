def romanToInt(s: str) -> int:

    key = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    edge = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    total = 0   
    i = 0     

    while i <= len(s) - 1:

        #Check to see if it's an edge case
        if i != (len(s) - 1):        #We don't need to check if the last letter is a combination of two
            temp = ""
            temp += s[i]
            temp += s[i+1]

            if temp in edge:
                total += edge[temp]
                i += 1              #Skip the next letter since we looked at it this time
            else: #If not an edge case simply add the total
                total += key[s[i]]
        else:
                total += key[s[i]] #This only runs on the last letter of the string

        i += 1


    return total

print(romanToInt("MCMXCIV"))