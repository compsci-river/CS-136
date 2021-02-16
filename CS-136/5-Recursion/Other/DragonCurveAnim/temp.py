#
#River Sheppard
#DragonCurveAnim
#

import sys
import math
import random
import StdDraw
from color import Color

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

    def getPoints(self,size,turn):
        mid = self.getMid()
        midPoint = [mid[0]+size*math.cos(turn),mid[1]+size*math.sin(turn)]
        return self.getStart()+midPoint+self.getEnd()

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

class Node:
    def __init__(self,line):
        self.line = line
        self.next = None

class Path:
    def __init__(self):
        self.start = None
        self.last = None

    def split(self):
        node = self.start
        pathOne = Path()
        pathTwo = Path()
        lastOne = None
        lastTwo = None
        while node != None:
            start = node.line.getStart()
            mid = node.line.getMid()
            end = node.line.getEnd()
            nodeOne = Node(Line(start[0],start[1],mid[0],mid[1]))
            nodeTwo = Node(Line(mid[0],mid[1],end[0],end[1]))
            if pathOne.start == None:
                pathOne.start = nodeOne
                pathTwo.start = nodeTwo
            if lastOne != None:
                lastOne.next = nodeOne
                lastTwo.next = nodeTwo
            lastOne = nodeOne
            lastTwo = nodeTwo
            node = node.next
        pathOne.last = lastOne
        pathTwo.last = lastTwo
        return [pathOne,pathTwo]

    def draw(self):
        node = self.start
        if node.next != None:
            node.line.draw(node.next.line)
            self.start = node.next
            return True
        else:
            return False

class DragonCurveAnim:
    def __init__(self):
        pass

    def dragonCurve(self,n,path,flip,paths):
        if n == 0:
            paths.append(path)
        elif n > 0:
            splitPaths = self.split(path,flip)
            paths = self.dragonCurve(n-1,splitPaths[0],1,paths)
            paths = self.dragonCurve(n-1,splitPaths[1],-1,paths)
        return paths

    def split(self,path,flip):
        line = path.last.line
        size = line.getSize()/2
        turn = line.getTurn()+flip*math.pi/2
        points = line.getPoints(size,turn)
        lineOne = Line(points[0],points[1],points[2],points[3])
        lineTwo = Line(points[2],points[3],points[4],points[5])
        paths = path.split()
        paths[0].last.next = Node(lineOne)
        paths[0].last = paths[0].last.next
        paths[1].last.next = Node(lineTwo)
        paths[1].last = paths[1].last.next
        return paths

    def colorDraw(self,paths):
        drawing = True
        colors = [StdDraw.RED,StdDraw.ORANGE,StdDraw.YELLOW,StdDraw.GREEN,StdDraw.CYAN,StdDraw.BLUE,StdDraw.DARK_BLUE,StdDraw.MAGENTA,StdDraw.VIOLET]
        while drawing:
            for i in range(0,len(paths)):
                spin = i
                while spin >= len(colors):
                    spin -= len(colors)
                StdDraw.setPenColor(colors[spin])
                drawing = paths[i].draw()
            StdDraw.show(100)

    def borderDraw(self,n,paths):
        StdDraw.setPenColor(StdDraw.WHITE)
        StdDraw.setPenRadius(0.025*(0.9**n))
        for i in range(0,len(paths)):
            paths[i].last.line.drawLine()
        StdDraw.show(500)

    def setUp(self,s):
        StdDraw.setCanvasSize(768,768)
        StdDraw.setXscale(-s,s)
        StdDraw.setYscale(-s,s)

    def runAll(self,n,path,flip):
        paths = self.dragonCurve(n,path,flip,[])
        self.colorDraw(paths)
        self.borderDraw(n,paths)

if __name__ == "__main__":
    n = 7
    s = 1.5
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    line = Line(-5/6,-1/3,7/6,-1/3)
    node = Node(line)
    path = Path()
    path.start = node
    path.last = node
    curve = DragonCurveAnim()
    curve.setUp(s)
    for i in range(1,n+1):
        StdDraw.clear()
        StdDraw.setPenColor(StdDraw.BLACK)
        StdDraw.filledSquare(0,0,s)
        curve.runAll(i,path,1)
        StdDraw.show(500)
    StdDraw.show(1000)
        
        











        
