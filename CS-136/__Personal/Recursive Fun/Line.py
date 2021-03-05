#
#River Sheppard
#Line
#

import math
import StdDraw
from Point import Point

class Line:
    def __init__(self,pOne,pTwo):
        self.pOne = pOne
        self.pTwo = pTwo

    def getStart(self):
        return self.pOne

    def getEnd(self):
        return self.pTwo

    def getSize(self):
        x = (self.pTwo.X()-self.pOne.X())**2
        y = (self.pTwo.Y()-self.pOne.Y())**2
        return math.sqrt(x+y)

    def getTurn(self):
        x = (self.pTwo.X()-self.pOne.X())
        y = (self.pTwo.Y()-self.pOne.Y())
        return math.atan2(y,x)

    def getPoint(self,p):
        scale = p*self.getSize()
        x = self.getStart().X()+scale*math.cos(self.getTurn())
        y = self.getStart().Y()+scale*math.sin(self.getTurn())
        return Point(x,y)

    def draw(self,col):
        StdDraw.setPenColor(col)
        StdDraw.line(self.pOne.X(),self.pOne.Y(),self.pTwo.X(),self.pTwo.Y())

    def print(self):
        print(self.pOne.str()+":"+self.pTwo.str())
