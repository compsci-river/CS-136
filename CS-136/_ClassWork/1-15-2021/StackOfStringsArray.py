#River Sheppard
# Programming activity
#
# Goal: Finish a class implementing Stack ADT (sort of)
#  - Use a Python list of strings to hold items
#  - Throw an exception if pop() is called on an empty stack
#

class StackOfStringsArray:

    def __init__(self):
        self.items = []        # Holds the stack's data 

    # Add the string s to the stack
    def push(self, s):
        self.items.append(s)

    # Remove the most recently added item from the stack
    # Throw an error if the stack is empty
    def pop(self):
        if self.isEmpty():
            throw ("Stack is empty!")
        else:
            s = self.items[len(self.items)-1]
            del self.items[len(self.items)-1]
            return s

    # Check if the stack is empty, return True if empty, False otherwise
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    # Return a string representing the items in the stack
    def toString(self):
        result = ""
        for i in range(0, len(self.items)):
            result += self.items[i] + " "
        return result

# Main test code
if __name__ == "__main__":
    s = StackOfStringsArray()

    print("before adding: " + s.toString())

    print("Pushing words: ", end="")
    s.push("it")
    print("it ", end="")
    s.push("was")
    print("was ", end="")
    s.push("the")
    print("the ", end="")
    s.push("best")
    print("best ", end="")
    s.push("of")
    print("of ", end="")
    s.push("times")
    print("times")
 
    while not s.isEmpty():
        print(s.pop() + " ", end="")
    print()

    print("after popping: " + s.toString())

