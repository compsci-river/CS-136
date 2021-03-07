#########################################################################
# Name        : River Sheppard
# Description : Stack that can hold strings, uses a linked list that 
#               tracks the head and tail of the list.
#########################################################################/
import Position

class Node:
#Constructor for the node class contains a position called item, and another
#node called next which is how the list works
    def __init__(self):
        self.item = None
        self.next = None
	
class StackOfPositions:
#constructor for the StackOfPositions class, contains a node called first
    def __init__(self):
        self.first = None

    #Add a new position to the stack, takes a position, creates a node at that
    #position pushes all the nodes in the list forward and adds the new node to
    #the first position
    #Inputs: Position s, the new Position
    #Outputs: null
    def push(self, s):
        node = Node()
        node.item = s

        if self.first == None:
            self.first = node
        else:
            node.next = self.first
            self.first = node

    # Remove the most recently added position, takes the node in the first spot
    #in the list and returns its position, then it removes that node from the
    #list and resets the list so that it still tracks the first position
    #Inputs: null
    #Outputs: Position result, the position held by the first node in the list
    def pop(self):
        if self.first == None:
            throw ("Stack is empty!")
        result = self.first.item
        self.first = self.first.next
        return result

    # Return a string representation of the queue, uses the .toString() method
    #from position to create a string containing the position data
    #Inputs: null
    #Outputs: String result, a string holding all the position data
    def toString(self):
        result = ""
        current = self.first
        while current != None:
            result += current.item.toString()
            current = current.next
        return result

    # Check if the queue is empty, uses the fact that there will always be a
    #node in the first spot if there are items in the stack to check if there
    #are still items in the stack
    #Inputs: null
    #Outputs: Boolean ___, if there are still nodes in the stack
    def isEmpty(self):
        return self.first == None
    
# main method for testing out the class
if __name__ == "__main__":
    q = StackOfStrings()

    
