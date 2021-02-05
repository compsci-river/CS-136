#
#River Sheppard
#Dragon Curve
#

import sys
import math
import random
import StdDraw
from color import Color

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
        self.curve(n,size,xPos,yPos,turn,True)

    def background(self,n,s):
        self.setUp(s)
        StdDraw.setPenColor(Color(255,255,0))
        self.dragonCurve(n,1.0,0.0,0.0,0.0)
        StdDraw.setPenColor(Color(0,255,0))
        self.dragonCurve(n,1.0,0.0,0.0,math.pi/2)
        StdDraw.setPenColor(Color(0,0,255))
        self.dragonCurve(n,1.0,0.0,0.0,math.pi)
        StdDraw.setPenColor(Color(255,0,0))
        self.dragonCurve(n,1.0,0.0,0.0,3*math.pi/2)

    

if __name__ == "__main__":
    s = 1.25
    dragonCurve = DragonCurve()
    dragonCurve.background(15,s)
    StdDraw.show(1000)

        
            
