#River Sheppard
#Dragon Curve

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
            s = line.getSize()/(2*math.sqrt(3))
            midLine = u.Line(u.Point(m.X()+s*math.cos(t),m.Y()+s*math.sin(t)),
                             u.Point(m.X()-s*math.cos(t),m.Y()-s*math.sin(t)))

            self.curve(n-1,u.Line(line.getStart(),midLine.getStart()))
            self.curve(n-1,midLine)
            self.curve(n-1,u.Line(midLine.getEnd(),line.getEnd()))

    def draw(self):
        for line in self.lines:
            line.draw()
            StdDraw.show(100)

def anim(n,line):
    for i in range(1,n+1):
        d = Dragon()
        d.curve(i,line)
        StdDraw.clear()
        d.draw()
        StdDraw.show(1000)
        
def SetUp(s):
    StdDraw.setCanvasSize(768,768)
    StdDraw.setXscale(-s,s)
    StdDraw.setYscale(-s,s)
    StdDraw.setPenRadius(0.001)

if __name__ == "__main__":
    SetUp(1)
    pOne = u.Point(-0.75,0)
    pTwo = u.Point(0.75,0)
    line = u.Line(pOne,pTwo)
    anim(7,line)
