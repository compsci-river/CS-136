#
#River Sheppard
#Lab 2: Linked Lists
#Description: Creates a class that forms a linked list of nodes and then has
#three different ways to add new nodes to the list, first by sorting nodes in
#order that they were added to the list, the next method sorts them so that new
#points get added after the node they're nearest to, the third method sorts them
#so that the new point adds the smallest amount of distance to the tour
#

import Point
import StdDraw

#A node class is used to define the linked list, it contains a Point and a Node pointing to the next in the list
class Node:
#The constructor
    def __init__(self):
        self.p = None
        self.next = None

class Tour:
#the constructor, contains a Node which marks the first point on the list
    def __init__(self):
        self.start = None

#Prints out the list of nodes that define the tour as their cordinate points, it loops through the list and uses
#the toString function from the Point class
    def show(self):
        print(self.start.p.toString())
        node = self.start.next
        while node != self.start:
            print(node.p.toString())
            node = node.next

#Draws the tour to the StdDraw screen, loops through the points in the list and uses the draw and drawTo
#functions from the Point class
    def draw(self):
        node = self.start.next
        self.start.p.draw()
        self.start.p.drawTo(node.p)
        while node != self.start:
            node.p.draw()
            node.p.drawTo(node.next.p)
            node = node.next

#Counts the amount of items in the list, runs through the list adding one each time until it reaches the
#beginning again
#Returns: int size, the length of the list
    def size(self):
        count = 0
        node = self.start
        working = True
        while working:
            count += 1
            node = node.next
            if node == self.start:
                working = False
        return count

#Measures the distance traveled by the tour, loops through the points and adds each step calculated by the
#distanceTo function from the Point class
#Returns: float distance, the total distance that the tour covers
    def distance(self):
        distance = self.start.p.distanceTo(self.start.next.p)
        node = self.start.next
        while node != self.start:
            distance += node.p.distanceTo(node.next.p)
            node = node.next
        return distance

#Adds a point to the end of the tour so that in the end the points are listed in the order that they are added
#it creates a new node and then loops through to the end of the list then creates makes the .next of the last
#node equal the new node and the .next of the new node equal the first position on the list
#Inserts: Point p, the point where the new node is being added
    def insertInOrder(self, p):
        newNode = Node()
        newNode.p = p
        if self.start == None:
            self.start = newNode
        else:
            lastNode = self.start
            while lastNode.next != self.start:
                lastNode = lastNode.next
            lastNode.next = newNode
        newNode.next = self.start

#Adds a point to the list where it will be the shortest distance from the previous point in the list, loops
#through the list and checks the distance from the surrent node to the new point, then adds the new point as a
#node after the node where the shortest distance was found
#Inserts: Point p, the point where the new node is being added
    def insertNearest(self, p):
        newNode = Node()
        newNode.p = p
        if self.start == None:
            self.start = newNode
            newNode.next = self.start
        else:
            minDist = None
            lastNode = self.start
            minNode = lastNode
            for i in range(0,self.size()):
                dist = lastNode.p.distanceTo(newNode.p)
                if minDist == None:
                    minDist = dist
                if dist < minDist:
                    minDist = dist
                    minNode = lastNode
                lastNode = lastNode.next
            newNode.next = minNode.next
            minNode.next = newNode

#Calculates the distance of the tour if a testNode was added after the lastNode, calculates the distance to the
#lastNode, adds the distance from lastNode to testNode, adds distance from testNode to lastNode.next and then
#adds the rest of the tour from lastNode.next to the end
#Inserts: Node lastNode, the node which testNode will follow. Node testNode, the node that is not part of the
#tour that the distance is being checked for.
#Returns: float distance, the distance of the tour with the new test node
    def newDist(self, lastNode, testNode):
        node = self.start
        distance = 0.0
        while node != lastNode:
            distance += node.p.distanceTo(node.next.p)
            node = node.next
        distance += lastNode.p.distanceTo(testNode.p)
        distance += testNode.p.distanceTo(lastNode.next.p)
        node = lastNode.next
        while node != self.start:
            distance += node.p.distanceTo(node.next.p)
            node = node.next
        return distance

#Adds a new node to the tour at Point p so that it adds the least amount of distance onto the previous tour,
#creates a new node and then runs it through newDist adds the new node to the tour at the point where newDist
#returns the smallest value
#Inserts: Point p, the point where the new node is being added
    def insertSmallest(self, p):
        newNode = Node()
        newNode.p = p
        if self.start == None:
            self.start = newNode
            newNode.next = self.start
        elif self.size() == 1:
            self.start.next = newNode
            newNode.next = self.start
        else:
            minNode = self.start
            minDist = self.newDist(self.start, newNode)
            lastNode = self.start.next
            while lastNode != self.start:
                dist = self.newDist(lastNode, newNode)
                if dist < minDist:
                    minDist = dist
                    minNode = lastNode
                lastNode = lastNode.next
            newNode.next = minNode.next
            minNode.next = newNode

    def altDist(self, nodeOne, nodeTwo, tourList):
        oldDist = 0.0
        newDist = 0.0
        node = tourList.start
        print("a")
        while node.next != nodeTwo:
            node = node.next
        oldDist += node.p.distanceTo(nodeOne.p)
        oldDist += nodeOne.p.distanceTo(nodeOne.next.p)
        newDist += node.p.distanceTo(nodeTwo.p)
        newDist += nodeTwo.p.distanceTo(nodeOne.next.p)

        while node.next != nodeTwo:
            node = node.next
        oldDist += node.p.distanceTo(nodeTwo.p)
        oldDist += nodeTwo.p.distanceTo(nodeTwo.next.p)
        newDist += node.p.distanceTo(nodeOne.p)
        newDist += nodeOne.p.distanceTo(nodeTwo.next.p)

        distance = oldDist - newDist

        print(str(oldDist))
        print(str(newDist))

        if newDist < oldDist:
            print("true")
            return True
        else:
            return False

    def cyclePoints(self, tourList):
        locOne = self.start
        locTwo = self.start

        cycling = tourList.start.next
        cyclingOne = tourList.start.next

        while cycling != tourList.start:
            while cyclingOne != tourList.start:
                if cycling != cyclingOne:
                    if self.altDist(cycling, cyclingOne, tourList):
                        while (locOne.next.p.x != cycling.p.x) and (locOne.next.p.y != cycling.p.y):
                            locOne = locOne.next
                        while (locTwo.next.p.x != cyclingOne.p.x) and (locTwo.next.p.y != cyclingOne.p.y):
                            locTwo = locTwo.next
                        print("i")
                        holdOne = locOne.next
                        holdTwo = locTwo.next

                        holdOne.next = locTwo.next.next
                        holdTwo.next = locOne.next.next

                        locTwo.next = holdOne
                        locOne.next = holdTwo
                cyclingOne = cyclingOne.next
            cyclingOne = tourList.start.next
            cycling = cycling.next

                        

                        












        
            
        
