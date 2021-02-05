#
#River Sheppard
#Leaf
#

import sys
import math
import StdDraw
from color import Color


class Leaf:
    def __init__(self):
        pass
    
    def drawDiamond(self,xList,yList):
        StdDraw.filledPolygon(xList,yList)
        StdDraw.show(0.001)

    def recursiveDiamond(self,n,x,y,s,t,stage):
        xList = [x,x+s/math.sqrt(3)*math.cos(t+math.pi/6),x+s*math.cos(t),x+s/math.sqrt(3)*math.cos(t-math.pi/6)]
        yList = [y,y+s/math.sqrt(3)*math.sin(t+math.pi/6),y+s*math.sin(t),y+s/math.sqrt(3)*math.sin(t-math.pi/6)]
        self.drawDiamond(xList,yList)
        n-=1
        if n > 0:
            if stage == 1:
                self.recursiveDiamond(n,xList[2],yList[2],s**1.25,t,1)
            else:
                self.recursiveDiamond(n,xList[2],yList[2],2*s,t,1)
            self.recursiveDiamond(n,xList[1],yList[1],s/math.sqrt(3),t+math.pi/6,1)
            self.recursiveDiamond(n,xList[3],yList[3],s/math.sqrt(3),t-math.pi/6,1)

    def setUp(self,size):
        StdDraw.setCanvasSize(768,768)
        StdDraw.setXscale(-size,size)
        StdDraw.setYscale(-size,size)
        StdDraw.setPenColor(Color(0,0,0))
        StdDraw.filledRectangle(-size,-size,2*size,2*size)

    def leaf(self,n,xPos,yPos,size,turn):
        if n < 1:
            n = 1
        self.recursiveDiamond(n,xPos,yPos,size,turn,0)

    def background(self,n,s,size):
        self.setUp(size)
        StdDraw.setPenColor(Color(0,50,10))
        self.leaf(n,0,0,s,0.0)
        self.leaf(n,0,0,s,math.pi/2)
        self.leaf(n,0,0,s,math.pi)
        self.leaf(n,0,0,s,3*math.pi/2)
        self.leaf(n,-size,-size,s,math.pi/4)
        self.leaf(n,size,-size,s,3*math.pi/4)
        self.leaf(n,size,size,s,5*math.pi/4)
        self.leaf(n,-size,size,s,7*math.pi/4)

    
    
    
if __name__ == "__main__":
    leaf = Leaf()
    leaf.background(7,0.25,2.25)
    StdDraw.show(1000)
