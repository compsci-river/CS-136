#
#River Sheppard
#Leaf
#

import math
import StdDraw

def recur(n,x,y,s,t,stage):
    xList = [x,x+s/math.sqrt(3)*math.cos(t+math.pi/6),x+s*math.cos(t),x+s/math.sqrt(3)*math.cos(t-math.pi/6)]
    yList = [y,y+s/math.sqrt(3)*math.sin(t+math.pi/6),y+s*math.sin(t),y+s/math.sqrt(3)*math.sin(t-math.pi/6)]
    StdDraw.filledPolygon(xList,yList)
    scale = math.sqrt(3)
    turn = math.pi/6
    n -= 1
    if n > 0:
        if stage == 1:
            recur(n,xList[2],yList[2],4*s/5,t,1)
            recur(n,xList[1],yList[1],s/scale,t+turn,1)
            recur(n,xList[3],yList[3],s/scale,t-turn,1)
        else:
            recur(n,xList[2],yList[2],1.5*s,t,1)
            recur(5,xList[1],yList[1],s/scale,t+turn,1)
            recur(5,xList[3],yList[3],s/scale,t-turn,1)
##        recur(n,xList[1],yList[1],s/scale,t+turn,1)
##        recur(n,xList[3],yList[3],s/scale,t-turn,1)

def leaf(xPos,yPos,size,turn):
    s = 10*size/72
    recur(9,xPos,yPos,s,turn,0)

def setUp(s):
    StdDraw.setCanvasSize(768,768)
    StdDraw.setXscale(-s,s)
    StdDraw.setYscale(-s,s)

if __name__ == "__main__":
    setUp(3)

    leaf(0,0,3,0)
    StdDraw.show(1000)
