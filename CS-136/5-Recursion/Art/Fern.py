#
#River Sheppard
#Fern
#

import sys
import math
import random
import StdDraw
from color import Color

class Fern:
    def __init__(self):
        self.right = math.pi/2
        self.sixty = math.pi/3
        self.fortyFive = math.pi/4
        self.thirty = math.pi/6
        self.sqrtThree = math.sqrt(3)
        self.sqrtTwo = math.sqrt(2)
        self.colors = []

    def randomColor(self,sLimit, limit):
        one = random.randint(sLimit,limit)
        s = random.randint(0,2)
        two = [0,0,0]
        two[s] = one
        c = Color(two[0],two[1],two[2])
        return c

    def setColor(self,s):
        if len(self.colors) <= s:
            self.colors.append(self.randomColor(100,200))
        StdDraw.setPenColor(self.colors[s])

    def drawSquare(self,n,x,y,t,s,flip,stage):
        xList = [x,x+s*math.cos(t),x+s*self.sqrtTwo*math.cos(t-flip*self.fortyFive),x+s*math.cos(t-flip*self.right)]
        yList = [y,y+s*math.sin(t),y+s*self.sqrtTwo*math.sin(t-flip*self.fortyFive),y+s*math.sin(t-flip*self.right)]
        self.setColor(stage)
        StdDraw.polygon(xList,yList)
        StdDraw.show(0.001)
        if flip == 1:
            self.drawTriangle(n-1,xList[1],yList[1],t,s,stage)
        else:
            self.drawTriangle(n-1,xList[2],yList[2],t,s,stage)

    def drawTriangle(self,n,x,y,t,s,stage):
        if n > 0:
            xList = [x,x+s/2*math.cos(t-self.thirty),x+s*math.cos(t-self.right)]
            yList = [y,y+s/2*math.sin(t-self.thirty),y+s*math.sin(t-self.right)]
            self.setColor(stage)
            StdDraw.polygon(xList,yList)
            StdDraw.show(0.001)
            self.drawSquare(n,xList[1],yList[1],t-self.thirty,s/2*self.sqrtThree,1,stage)
            self.drawSquare(n,xList[1],yList[1],t+self.sixty,s/2,-1,stage+1)

    def fern(self,n,x,y,t,s):
        self.drawSquare(n,x,y,t,s,1,0)

    def setUp(self,s):
        StdDraw.setCanvasSize(768,768)
        StdDraw.setXscale(-s,s)
        StdDraw.setYscale(-s,s)
        StdDraw.setPenColor(Color(0,0,0))
        StdDraw.filledRectangle(-s,-s,2*s,2*s)

    def background(self,n,size,s):
        self.setUp(size)
        StdDraw.setPenColor(Color(0,150,255))
        self.fern(n,-2,-3,self.right,s)

if __name__ == "__main__":
    fern = Fern()
    fern.background(20,4,1.15)
    StdDraw.show(1000)
