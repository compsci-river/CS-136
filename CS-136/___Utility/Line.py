#
#River Sheppard
#Line
#

import math
import StdDraw

class Line:
    def __init__(self,x,y,xOne,yOne):
        self.x = x
        self.y = y
        self.xOne = xOne
        self.yOne = yOne

    def getStart(self):
        return [self.x,self.y]

    def getEnd(self):
        return [self.xOne,self.yOne]

    def getMid(self):
        return [(self.x+self.xOne)/2,(self.y+self.yOne)/2]

    def getSize(self):
        y = (self.yOne-self.y)**2
        x = (self.xOne-self.x)**2
        s = math.sqrt(y+x)
        return s

    def getTurn(self):
        y = self.yOne-self.y
        x = self.xOne-self.x
        if x > 0.0001:
            if y > 0.0001:
                return math.pi/4
            elif y < -0.0001:
                return 7*math.pi/4
            else:
                return 0
        elif x < -0.0001:
            if y > 0.0001:
                return 3*math.pi/4
            elif y < -0.0001:
                return 5*math.pi/4
            else:
                return math.pi
        else:
            if y > 0.0001:
                return math.pi/2
            else:
                return 3*math.pi/2

    def drawLine(self):
        StdDraw.line(self.x,self.y,self.xOne,self.yOne)

    def draw(self,nextLine):
        xList = [self.x,self.xOne,nextLine.xOne,nextLine.x]
        yList = [self.y,self.yOne,nextLine.yOne,nextLine.y]
        StdDraw.filledPolygon(xList,yList)

if __name__ == "__main__":
    l = Line(0.25,0.25,0.75,0.75)
    l.drawLine()
    StdDraw.show(500)


        
