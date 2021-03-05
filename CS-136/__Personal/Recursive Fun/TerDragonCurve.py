#
#River Sheppard
#TerDragon Curve
#
#

import math
import StdDraw

from Point import Point
from Line import Line

class TerDragon:
    def __init__(self):
        pass

    def curve(self,line,n,lines):
        #line.print()
        if n <= 0:
            lines.append(line)
            return lines
        else:
            s = self.cut(line)
            for a in s:
                lines = self.curve(a,n-1,lines)
            return lines

    def cut(self,line):
        a = line.getSize()/(2*math.sqrt(3))
        t = line.getTurn()-math.pi/2
        pMid = line.getPoint(0.5)
        xScale = a*math.cos(t)
        yScale = a*math.sin(t)
        pOne = Point(pMid.X()+xScale,pMid.Y()+yScale)
        pTwo = Point(pMid.X()-xScale,pMid.Y()-yScale)
        p = [line.getStart(),pOne,pTwo,line.getEnd()]
        return [Line(p[0],p[1]),Line(p[1],p[2]),Line(p[2],p[3])]

    def draw(self,lines,col):
        StdDraw.setPenRadius(0.0005)
        for a in lines:
            a.draw(col)

    def run(self,xT):
        y = Point(0,0)
        x = xT
        col = [StdDraw.RED,StdDraw.ORANGE,StdDraw.YELLOW,StdDraw.GREEN,StdDraw.BLUE,StdDraw.MAGENTA]
        for i in range(6):
            w = Point(math.cos(x),math.sin(x))
            v = Line(y,w)
            a = self.curve(v,9,[])
            self.draw(a,col[i])
            x -= math.pi/3

if __name__ == "__main__":
    StdDraw.setCanvasSize(768,768)
    StdDraw.setXscale(-1.1,1.1)
    StdDraw.setYscale(-1.1,1.1)
    z = TerDragon()
    x = math.pi/2
    while True:
        StdDraw.clear()
        z.run(x)
        x += math.pi/6
        StdDraw.show(1)
    StdDraw.show(1000)






    
        
