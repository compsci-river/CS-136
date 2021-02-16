#
#River Sheppard
#Tree
#

import math
import StdDraw

def recur(n,nn,x,y,s,t):
    StdDraw.setPenRadius(0.015*n/nn)
    xOne = x+s*math.cos(t)
    yOne = y+s*math.sin(t)
    StdDraw.line(x,y,xOne,yOne)
    n-=1
    if n > 0:
        s -= s/(10*(nn-n))
        tt = math.pi/3/n
        recur(n,nn,xOne,yOne,s,t-tt)
        recur(n,nn,xOne,yOne,s,t+tt)

def tree(xPos,yPos,s,turn):
    size = s*11/80
    recur(9,9,xPos,yPos,size,turn)

def setUp(s):
    StdDraw.setCanvasSize(768,768)
    StdDraw.setXscale(-s,s)
    StdDraw.setYscale(-s,s)

def start(s):
    setUp(s)
    tree(0,0,s,0)

if __name__ == "__main__":
    start(3)
    StdDraw.show(1000)
