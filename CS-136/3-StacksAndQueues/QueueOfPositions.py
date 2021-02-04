#########################################################################
# Name        : River Sheppard
# Description : Queue that can hold strings, uses a linked list that 
#               tracks the head and tail of the list.
#########################################################################/

class Node:

    def __init__(self):
        self.item = None
        self.next = None

class QueueOfPositions:

    def __init__(self):
        self.first = None
        self.last  = None

    # Add a new position to the queue, takes a position and creates a node with
    #that position and then adds it onto the end of the list
    #Inputs: Position s, the position being added to the list
    #Outputs: null
    def enqueue(self, s):
        node = Node()
        node.item = s
        node.next = None

        if self.last != None:
            self.last.next = node
        self.last = node

        if self.first == None:
            self.first = node

    # Remove the least recently added position, takes the node in the first spot
    #in the list and returns its position, then it removes that node from the
    #list and resets the list so that it still tracks the first position
    #Inputs: null
    #Outputs: Position result, the position held by the first node in the list
    def dequeue(self):
        if self.first == None:
            throw ("Queue is empty!")
        result = self.first.item
        self.first = self.first.next
        if self.first == None:
            self.last = None
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
    q = QueueOfStrings()

    
