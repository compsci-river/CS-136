#
#River Sheppard
#Triangle
#

import sys
import math
import StdDraw
from color import Color

class Triangle:
    def __init__(self):
        pass

    def drawTriangle(self,x,y,s,flip):
        angle = math.pi/6
        xList = [x,x-s*math.sin(angle),x+s*math.sin(angle)]
        yList = [y,y+flip*s*math.cos(angle),y+flip*s*math.cos(angle)]
        StdDraw.polygon(xList,yList)

    def drawLines(self,x,y,s,flip,scale):
        angle = math.pi/6
        xList = [x,x-s*math.sin(angle),x+s*math.sin(angle)]
        oneXlist = [x]
        twoXlist = [xList[1]]
        threeXlist = [xList[2]]
        yList = [y,y+flip*s*math.cos(angle),y+flip*s*math.cos(angle)]
        oneYlist = [y]
        twoYlist = [yList[1]]
        threeYlist = [yList[2]]
        for i in range(0,scale):
            oneXlist.append(x-(i+1)*s*math.sin(angle)/scale)
            twoXlist.append(xList[1]+(i+1)*s/scale)
            threeXlist.append(xList[2]-(i+1)*s*math.sin(angle)/scale)
            oneYlist.append(y+(i+1)*flip*s*math.cos(angle)/scale)
            twoYlist.append(y+flip*s*math.cos(angle))
            threeYlist.append(yList[2]-(i+1)*flip*s*math.cos(angle)/scale)
        for i in range(0,scale):
            StdDraw.line(oneXlist[i],oneYlist[i],twoXlist[i+1],twoYlist[i+1])
            StdDraw.line(twoXlist[i],twoYlist[i],threeXlist[i+1],threeYlist[i+1])
            StdDraw.line(threeXlist[i],threeYlist[i],oneXlist[i+1],oneYlist[i+1])

    def recursive(self,n,x,y,s,flip):
        if n == 0:
            self.drawLines(x,y,s,flip,15)
        else:
            n-=1
            s = s/2
            self.recursive(n,x,y,s,flip)
            y += flip*s*math.cos(math.pi/6)
            x -= s*math.sin(math.pi/6)
            self.recursive(n,x,y,s,flip)
            x += s
            self.recursive(n,x,y,s,flip)
            y += flip*s*math.cos(math.pi/6)
            x -= s/2
            flip *= -1
            self.recursive(n,x,y,s,flip)

    def setUp(self,s):
        StdDraw.setCanvasSize(768,768)
        StdDraw.setXscale(-s,s)
        StdDraw.setYscale(-s,s)
        StdDraw.setPenColor(Color(0,0,0))
        StdDraw.filledRectangle(-s,-s,2*s,2*s)
        

    def triangle(self,n,size,xPos,yPos,flip):
        if n < 1:
            n = 1
        self.drawTriangle(xPos,yPos,size,-flip)
        self.recursive(n,xPos,yPos,size,-flip)

    def background(self,n,s,size):
        self.setUp(size)
        StdDraw.setPenColor(Color(255,0,0))
        StdDraw.setPenRadius(0.001)
        self.triangle(n,s,0,2.598,1)

if __name__ == "__main__":
    triangle = Triangle()
    triangle.background(3,6,3)
    StdDraw.show(1000)
