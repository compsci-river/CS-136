#
#River Sheppard
#Cube
#

import sys
import math
import StdDraw
from color import Color

class Cube:
    def __init__(self):
        pass

    def drawPlane(self,xList,yList,c):
        StdDraw.setPenColor(c)
        StdDraw.filledPolygon(xList,yList)

    def drawCube(self,x,y,s,cList,flip):
        xList = [x,x+s*math.cos(math.pi/6),x,x-s*math.cos(math.pi/6)]
        yList = [y,y-flip*s*math.sin(math.pi/6),y-2*flip*s*math.sin(math.pi/6),y-flip*s*math.sin(math.pi/6)]
        self.drawPlane(xList,yList,cList[0])
        xList = [x,x,x-flip*s*math.cos(math.pi/6),x-flip*s*math.cos(math.pi/6)]
        yList = [y,y+flip*s,y+flip*s-flip*s*math.sin(math.pi/6),y-flip*s*math.sin(math.pi/6)]
        self.drawPlane(xList,yList,cList[1])
        xList = [x,x,x+flip*s*math.cos(math.pi/6),x+flip*s*math.cos(math.pi/6)]
        self.drawPlane(xList,yList,cList[2])

    def recursiveCube(self,n,x,y,s,cList,flip):
        self.drawCube(x,y,s,cList,flip)
        n-=1
        if n > 0:
            a=s/2.5
            self.recursiveCube(n,x,y,a,cList,-flip)
            self.recursiveCube(n,x-s*math.cos(math.pi/6),y+flip*s-flip*s*math.sin(math.pi/6),a,cList,flip)
            self.recursiveCube(n,x+s*math.cos(math.pi/6),y+flip*s-flip*s*math.sin(math.pi/6),a,cList,flip)
            self.recursiveCube(n,x,y-2*flip*s*math.sin(math.pi/6),a,cList,flip)

    def setUp(self,s):
        StdDraw.setCanvasSize(768,768)
        StdDraw.setXscale(-s,s)
        StdDraw.setYscale(-s,s)
        StdDraw.setPenColor(Color(0,0,0))
        StdDraw.filledRectangle(-s,-s,2*s,2*s)

    def cube(self,n,xPos,yPos,size,colors):
        if n < 1:
            n = 1
        self.drawCube(xPos,yPos,size,colors,-1)
        self.recursiveCube(n,xPos,yPos,size/2,colors,1)

    def background(self):
        bright = Color(255,255,255)
        shaded = Color(150,150,150)
        gray = Color(50,50,50)
        self.setUp(5)
        self.cube(5,0,0,5,[bright,shaded,gray])


if __name__ == "__main__":
    cube = Cube()
    cube.background()
    StdDraw.show(1000)
