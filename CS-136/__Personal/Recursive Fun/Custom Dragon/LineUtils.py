#
#River Sheppard
#Line Utilities
#

import sys
import math
import StdDraw

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def X(self):
        return self.x

    def Y(self):
        return self.y

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

class Line:
    def __init__(self,pOne,pTwo):
        self.pOne = pOne
        self.pTwo = pTwo

    def getStart(self):
        return self.pOne

    def getEnd(self):
        return self.pTwo

    def getSize(self):
        dX = (self.pTwo.X()-self.pOne.X())**2
        dY = (self.pTwo.Y()-self.pOne.Y())**2
        return math.sqrt(dX+dY)

    def getTurn(self):
        dX = (self.pTwo.X()-self.pOne.X())
        dY = (self.pTwo.Y()-self.pOne.Y())
        return math.atan2(dY,dX)

    def getPoint(self,percent):
        scale = percent*self.getSize()
        dX = self.pOne.X()+scale*math.cos(self.getTurn())
        dY = self.pOne.Y()+scale*math.sin(self.getTurn())
        return Point(dX,dY)

    def draw(self):
        StdDraw.line(self.pOne.X(),self.pOne.Y(),self.pTwo.X(),self.pTwo.Y())
        

