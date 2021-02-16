#
#River Sheppard
#Dragon Curve
#

import sys
import math
import random
import StdDraw
from color import Color

class Node:
    def __init__(self,l):
        self.line = l
        self.start = None
        self.next = None

class DragonCurve:
    def __init__(self):
        pass

    def curve(self,n,s,x,y,t,sign):
        if n == 0:
            StdDraw.line(x,y, x + s*math.cos(t), y + s*math.sin(t))
        else:
            a = s * math.sqrt(0.5)
            if sign:
                t -= math.pi/4
                self.curve(n-1,a,x,y,t,True)
                x = x + a*math.cos(t)
                y = y + a*math.sin(t)
                t += math.pi/2
                self.curve(n-1,a,x,y,t,False)
            else:
                t += math.pi/4
                self.curve(n-1,a,x,y,t,True)
                x = x + a*math.cos(t)
                y = y + a*math.sin(t)
                t -= math.pi/2
                self.curve(n-1,a,x,y,t,False)

    def setUp(self,s):
        StdDraw.setCanvasSize(768,768)
        StdDraw.setXscale(-s,s)
        StdDraw.setYscale(-s,s)
        StdDraw.setPenColor(Color(0,0,0))
        StdDraw.filledRectangle(-s,-s,2*s,2*s)

    def dragonCurve(self,n,size,xPos,yPos,turn):
        if n < 1:
            n = 1
        for i in range(0,n):
            StdDraw.clear()
            StdDraw.setPenColor(Color(0,0,0))
            StdDraw.filledRectangle(-s,-s,2*s,2*s)
            StdDraw.setPenColor(Color(255,0,0))
            self.curve(i,size,xPos,yPos,turn,True)
            StdDraw.show(500)

    def background(self,n,s):
        self.setUp(s)
        
        self.dragonCurve(n,1.0,-0.5,0.0,0.0)

    

if __name__ == "__main__":
    s = 1
    dragonCurve = DragonCurve()
    dragonCurve.background(15,s)
    StdDraw.show(1000)

        
            
