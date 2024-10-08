class Stack:
    def __init__(self):
        self.items = []
        self.length = 0
    

    def push(self, item):
        self.items.append(item)
        self.length += 1


    def pop(self):
        if self.length > 0:
            self.length -= 1
            return self.items.pop(-1) #Removes the last item of the list (top of the stack)
        else:
            print("Error: Pop to an empty stack")


def isPalindrome(x: int) -> bool:

        stack = Stack()

        starting_string_int = str(x)
        new_string_int = []



        for char in starting_string_int: #Push all the numbers onto the stack
            stack.push(char)

        
        #Take each letter out and make a new string with them
        for char in starting_string_int:
            new_string_int.append(stack.pop())

        new_string_int = "".join(new_string_int)

        #Compare new string with the old string
        return starting_string_int == new_string_int
        
