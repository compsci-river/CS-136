#
#River Sheppard
#Triangle
#

import sys
import math
import StdDraw
from color import Color

def show():
    StdDraw.show(0.001)

def drawTriangle(x,y,s,flip):
    scale = 10
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
    StdDraw.polygon(xList,yList)
    show()
    for i in range(0,scale):
        StdDraw.line(oneXlist[i],oneYlist[i],twoXlist[i+1],twoYlist[i+1])
        StdDraw.line(twoXlist[i],twoYlist[i],threeXlist[i+1],threeYlist[i+1])
        StdDraw.line(threeXlist[i],threeYlist[i],oneXlist[i+1],oneYlist[i+1])
        show()

def recursive(n,x,y,s,flip):
    if n == 0:
        drawTriangle(x,y,s,flip)
    else:
        n-=1
        s = s/2
        recursive(n,x,y,s,flip)
        y += flip*s*math.cos(math.pi/6)
        x -= s*math.sin(math.pi/6)
        recursive(n,x,y,s,flip)
        x += s
        recursive(n,x,y,s,flip)
        y += flip*s*math.cos(math.pi/6)
        x -= s/2
        flip *= -1
        recursive(n,x,y,s,flip)

def setUp():
    StdDraw.setCanvasSize(768,768)
    StdDraw.setXscale(-3,3)
    StdDraw.setYscale(-3,3)
    StdDraw.setPenColor(Color(0,0,0))
    StdDraw.filledRectangle(-3,-3,6,6)
    show()

if __name__ == "__main__":
    n=3
    setUp()
    StdDraw.setPenColor(Color(255,0,0))
    StdDraw.setPenRadius(0.003/n)
    recursive(n,0,-3,6,1)
