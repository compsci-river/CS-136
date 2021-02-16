#
#River Sheppard
#Tree
#

import sys
import math
import StdDraw
from color import Color

class Tree:
    def __init__(self):
        pass

    def recursiveLines(self,n,nn,x,y,s,t):
        StdDraw.setPenRadius(0.015*n/nn)
        xOne = x+s*math.cos(t)
        yOne = y+s*math.sin(t)
        StdDraw.line(x,y,xOne,yOne)
        n-=1
        if n > 0:
            s -= s/(10*(nn-n))
            tt = math.pi/3/n
            self.recursiveLines(n,nn,xOne,yOne,s,t-tt)
            self.recursiveLines(n,nn,xOne,yOne,s,t+tt)

    def setUp(self,s):
        StdDraw.setCanvasSize(768,768)
        StdDraw.setXscale(-s,s)
        StdDraw.setYscale(-s,s)
        StdDraw.setPenColor(Color(0,0,0))
        StdDraw.filledRectangle(-s,-s,2*s,2*s)

    def tree(self,n,xPos,yPos,s,turn):
        if n < 1:
            n = 1
        size = s*11/80
        self.recursiveLines(n,n,xPos,yPos,size,turn)

    def background(self,s):
        self.setUp(s)
        turn = 0.0
        StdDraw.setPenColor(StdDraw.WHITE)
        for i in range(0,8):
            turn += 2 * math.pi/8
            self.tree(9,0,0,s,turn)

    def start(self,s):
        tree.setUp(s)
        StdDraw.setPenColor(StdDraw.WHITE)
        tree.tree(9,0,0,s,0)

if __name__ == "__main__":
    tree = Tree()
    #tree.start(3)
    tree.background(3)
    
    StdDraw.show(1000)
