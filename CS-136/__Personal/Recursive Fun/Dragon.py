#
#River Sheppard
#
#

import math
import StdDraw

import LineUtils as u

class Dragon:
    def __init__(self):
        self.lines = []

    def curve(self,n,line):
        if n == 0:
            self.lines.append(line)
        else:
            m = line.getPoint(0.5)
            t = line.getTurn()-math.pi/2
            s = line.getSize()/2
            dX = m.X()+s*math.cos(t)
            dY = m.Y()+s*math.sin(t)
            p = u.Point(dX,dY)

            self.curve(n-1,u.Line(line.getStart(),p))
            self.curve(n-1,u.Line(p,line.getEnd()))

    def draw(self):
        for a in self.lines:
            a.draw()

def anim(n,line):
    for i in range(1,n+1):
        d = Dragon()
        d.curve(i,line)
        #StdDraw.clear()
        d.draw()
        StdDraw.show(1000)
        
def SetUp(s):
    StdDraw.setCanvasSize(768,768)
    StdDraw.setXscale(-s,s)
    StdDraw.setYscale(-s,s)
    StdDraw.setPenRadius(0.001)

if __name__ == "__main__":
    SetUp(1)
    pOne = u.Point(-0.5,0)
    pTwo = u.Point(0.5,0)
    line = u.Line(pOne,pTwo)
    anim(15,line)
