#
#River Sheppard
#Art
#Description:
#

import sys
import math
import StdDraw
from color import Color

import Leaf
import Tree

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def X(self):
        return self.x

    def Y(self):
        return self.y

    def draw(self,t):
        StdDraw.setPenRadius(0.005)
        StdDraw.point(self.X(),self.Y())
        StdDraw.show(t)

class Line:
    def __init__(self,pOne,pTwo):
        self.pOne = pOne
        self.pTwo = pTwo
        self.diffX = self.pTwo.X() - self.pOne.X()
        self.diffY = self.pTwo.Y() - self.pOne.Y()

    def getStart(self):
        return self.pOne

    def getEnd(self):
        return self.pTwo

    def getSize(self):
        return math.sqrt((self.diffX**2)+(self.diffY**2))

    def getTurn(self):
        return math.atan2(self.diffY,self.diffX)

    def draw(self,t):
        StdDraw.setPenRadius(self.getSize()*0.01)
        StdDraw.line(self.pOne.X(),self.pOne.Y(),self.pTwo.X(),self.pTwo.Y())
        StdDraw.show(t)

def customPoint():
    point = None
    while point == None:
        if StdDraw.mousePressed():
            point = Point(StdDraw.mouseX(),StdDraw.mouseY())
        StdDraw.show(10)
    StdDraw.setPenColor(StdDraw.BLACK)
    point.draw(50)
    StdDraw.setPenColor(StdDraw.WHITE)
    point.draw(50)
    return point

def customLine():
    print("Please select a start point")
    pOne = customPoint()
    print("Please select an end point")
    pTwo = customPoint()
    line = Line(pOne,pTwo)
    StdDraw.setPenColor(StdDraw.BLACK)
    line.draw(50)
    StdDraw.setPenColor(StdDraw.WHITE)
    line.draw(50)
    return line

def setPenColor():
    StdDraw.setPenColor(StdDraw.BLACK)

def draw(l,n):
    p = l.getStart()
    x = p.X()
    y = p.Y()
    s = l.getSize()
    t = l.getTurn()
    setPenColor()
    if n == 1:
        Leaf.leaf(x,y,s,t)
    elif n == 2:
        Tree.tree(x,y,s,t)
    StdDraw.show(10)

def numInput(s,mi,ma):
    working = True
    x = 0
    while working:
        x = input(s)
        if x == "":
            print("That is not a valid response, please try again")
        else:
            x = int(x)
            if x < mi or x > ma:
                print("That is not a valid response, please try again")
            else:
                working = False
    return x

def artInput():
    drawing = True
    length = 1
    while drawing:
        shaping = True
        n = numInput("1: Leaf\n2: Tree\nPlease select a shape: ",1,2)
        l = customLine()
        draw(l,n)
        buzzing = True
        buzz = numInput("1: Yes\n2: No\nWould you like to draw another shape: ",1,2)
        if buzz == 2:
            drawing = False

def setUp(s):
    StdDraw.setCanvasSize(768,768)
    StdDraw.setXscale(-s,s)
    StdDraw.setYscale(-s,s)
    
def startUp():
    setUp(3)
    artInput()

if __name__ == "__main__":
    startUp()
        







    
        
