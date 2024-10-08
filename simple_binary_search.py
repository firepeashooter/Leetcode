sorted = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
key = 23

"""Returns the index of the key in the list in log(n) time complexity"""

def binary_search(list, key, low, high):


    #The magic calculation of middle that preserves the index
    mid = low + (high - low) // 2
    
    
    if low <= high:

        if key == list[mid]:
            return mid #The index of the value we are looking for
        elif key < list[mid]:
            return binary_search(list, key, low, mid - 1)
        elif key > list[mid]:
            return binary_search(list, key, mid + 1, high)

    else:
        return -1
        



    






print(binary_search(sorted, key, 0, len(sorted) - 1))

