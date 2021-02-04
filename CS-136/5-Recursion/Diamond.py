#
#River Sheppard
#Diamond
#

import sys
import math
import StdDraw
from color import Color

def drawDiamond(xList,yList):
    StdDraw.filledPolygon(xList,yList)
    StdDraw.show(0.001)

def recursiveDiamond(n,x,y,s,t,stage):
    xList = [x,x+s/math.sqrt(3)*math.cos(t+math.pi/6),x+s*math.cos(t),x+s/math.sqrt(3)*math.cos(t-math.pi/6)]
    yList = [y,y+s/math.sqrt(3)*math.sin(t+math.pi/6),y+s*math.sin(t),y+s/math.sqrt(3)*math.sin(t-math.pi/6)]
    drawDiamond(xList,yList)
    n-=1
    if n > 0:
        if stage == 1:
            recursiveDiamond(n,xList[2],yList[2],s**1.25,t,1)
        else:
            recursiveDiamond(n,xList[2],yList[2],0.5,t,1)
        recursiveDiamond(n,xList[1],yList[1],s/math.sqrt(3),t+math.pi/6,1)
        recursiveDiamond(n,xList[3],yList[3],s/math.sqrt(3),t-math.pi/6,1)
            

def start(n,s):
    recursiveDiamond(n,0,0,s,0.0,0)
    recursiveDiamond(n,0,0,s,math.pi/2,0)
    recursiveDiamond(n,0,0,s,math.pi,0)
    recursiveDiamond(n,0,0,s,3*math.pi/2,0)
    recursiveDiamond(n,-2.25,-2.25,s,math.pi/4,0)
    recursiveDiamond(n,2.25,-2.25,s,3*math.pi/4,0)
    recursiveDiamond(n,2.25,2.25,s,5*math.pi/4,0)
    recursiveDiamond(n,-2.25,2.25,s,7*math.pi/4,0)

def setUp():
    StdDraw.setCanvasSize(768,768)
    StdDraw.setXscale(-2.25,2.25)
    StdDraw.setYscale(-2.25,2.25)
    StdDraw.setPenColor(Color(0,0,0))
    StdDraw.filledRectangle(-2.25,-2.25,4.5,4.5)
    StdDraw.setPenColor(Color(0,50,10))
    
if __name__ == "__main__":
    setUp()
    start(7,0.25)
    StdDraw.show(1000)
