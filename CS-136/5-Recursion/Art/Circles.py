#
#River Sheppard
#Circles
#

import sys
import math
import random
import StdDraw
from color import Color

class Circles:
    def __init__(self):
        pass

    def draw(self,x,y,s):
        StdDraw.circle(x,y,s)
        StdDraw.filledCircle(x,y,s/2)

    def recur(self,n,x,y,s,t,stage):
        self.draw(x,y,s)
        n-=1
        if n > 0:
            scale = 2*s
            s = s/1.1
            t -= math.pi/4
            x += scale*math.cos(t)
            y += scale*math.sin(t)
            self.recur(n,x,y,s,t,1)

    def setUp(self,s):
        StdDraw.setCanvasSize(768,768)
        StdDraw.setXscale(-s,s)
        StdDraw.setYscale(-s,s)
        StdDraw.filledSquare(0,0,s)

    def circles(self,n,x,y,s):
        if n < 1:
            n = 1
        self.recur(n,x,y,s,1*math.pi/2,0)
        self.recur(n,-x,-y,s,3*math.pi/2,0)
        self.recur(n,x,-y,s,0*math.pi/2,0)
        self.recur(n,-x,y,s,2*math.pi/2,0)

if __name__ == "__main__":
    size = 1.5
    n = 50
    s = 0.25
    circles = Circles()
    circles.setUp(size)
    StdDraw.setPenColor(StdDraw.WHITE)
    StdDraw.setPenRadius(0.001)
    circles.circles(n,5*s/7,5*s/7,s*2/3)
    StdDraw.show(1000)







