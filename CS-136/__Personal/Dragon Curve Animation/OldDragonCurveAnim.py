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
        self.oldX = -0.5
        self.fullN = 1

    def setColor(self):
        c = [Color(175,0,230),Color(255,100,255),Color(255,0,0),Color(0,255,0),Color(0,0,255),Color(255,255,0)]
        d = random.randint(0,len(c)-1)
        return c[d]

    def scaleColor(self,c,s):
        b = [int(s*c.getRed()),int(s*c.getGreen()),int(s*c.getBlue())]
        a = Color(b[0],b[1],b[2])
        return a

    def drawLine(self,x,y,xOne,yOne):
        StdDraw.line(x,y, xOne, yOne)
        StdDraw.show(0.001)

    def animLine(self,x,y,s,t):
        scale = 100
        xOne = x + s*math.cos(t)
        yOne = y + s*math.sin(t)
        a = (math.sqrt(0.5)**self.fullN)/(2**(self.fullN-1))
        oldXone = self.oldX + a
        c = self.setColor()
        for i in range(1,scale):
            StdDraw.setPenColor(self.scaleColor(c,i/scale))
            scaleX = self.oldX + (x-self.oldX)*i/scale
            scaleY = y*i/scale
            scaleXone = oldXone + (xOne-oldXone)*i/scale
            scaleYone = yOne*i/scale
            self.drawLine(scaleX,scaleY,scaleXone,scaleYone)
        self.oldX += a

    def curve(self,n,s,x,y,t,sign):
        if n == 0:
            self.animLine(x,y,s,t)
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
        StdDraw.filledSquare(0,0,s)

    def dragonCurve(self,n,size,xPos,yPos,turn):
        if n < 1:
            n = 1
        self.fullN = n
        self.curve(n,size,xPos,yPos,turn,True)

    def start(self,n,s):
        self.setUp(s)
        StdDraw.line(-0.5,0,0.5,0)
        self.dragonCurve(n,1.0,-0.5,0.0,0.0)
        

    

if __name__ == "__main__":
    s = 1
    dragonCurve = DragonCurve()
    dragonCurve.start(7,s)
    StdDraw.show(1000)

        
            
