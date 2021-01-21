#########################################################################
# Name        : River Sheppard
# Description : Stack that can hold strings, uses a linked list that 
#               tracks the head and tail of the list.
#########################################################################/
import Position

class Node:

    def __init__(self):
        self.item = None
        self.next = None
	
class StackOfPositions:

    def __init__(self):
        self.first = None

    # Add a new position to the queue
    def push(self, s):
        node = Node()
        node.item = s;

        if self.first == None:
            self.first = node
        else:
            node.next = self.first
            self.first = node

    # Remove the least recently added position
    def pop(self):
        if self.first == None:
            throw ("Stack is empty!")
        result = self.first.item
        self.first = self.first.next
        return result

    # Return a string representation of the queue	
    def toString(self):
        result = ""
        current = self.first
        while current != None:
            result += current.item.toString()
            current = current.next
        return result

    # Check if the queue is empty
    def isEmpty(self):
        return self.first == None
    
# main method for testing out the class
if __name__ == "__main__":
    q = StackOfStrings()

    
