#
#River Sheppard
#Dragon Curve
#

import sys
import StdDraw
from color import Color
import math



def curve(n,s,x,y,t,sign):
    if n == 0:
        StdDraw.line(x,y, x + s*math.cos(t), y + s*math.sin(t))
    else:
        a = s * math.sqrt(0.5)
        if sign:
            t -= math.pi/4
            curve(n-1,a,x,y,t,True)
            x = x + a*math.cos(t)
            y = y + a*math.sin(t)
            t += math.pi/2
            curve(n-1,a,x,y,t,False)
        else:
            t += math.pi/4
            curve(n-1,a,x,y,t,True)
            x = x + a*math.cos(t)
            y = y + a*math.sin(t)
            t -= math.pi/2
            curve(n-1,a,x,y,t,False)

def setUp():
    StdDraw.setCanvasSize(768,768)
    StdDraw.setXscale(0,2)
    StdDraw.setYscale(0,2)

if __name__ == "__main__":
    setUp()
    for i in range(0,15):
        #StdDraw.clear()
        StdDraw.setPenRadius(0.01/(i+1))
        curve(i,1.0,0.5,1.0,0.0,True)
        StdDraw.show(50)
        
            
