#
#River Sheppard
#New Dragon Curve
#

import sys
import math
import random
import StdDraw
from color import Color
import Line

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

class Node:
    def __init__(self,l):
        self.l = l
        self.next = None

class Path:
    def __init__(self):
        self.start = None
        self.last = None

    def cut(self):
        node = self.start
        pathOne = Path()
        pathTwo = Path()
        lastOne = None
        lastTwo = None
        while node != None:
            start = node.l.getStart()
            mid = node.l.getMid()
            end = node.l.getEnd()
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
            node.l.draw(node.next.l)
            self.start = node.next
            return True
        else:
            return False

def draw(path,flip):
    line = path.last.l
    start = line.getStart()
    mid = line.getMid()
    end = line.getEnd()
    size = line.getSize()/2
    turn = line.getTurn()+flip*math.pi/2
    paths = path.cut()
    pathOne = paths[0]
    pathTwo = paths[1]
    midPoint = [mid[0]+size*math.cos(turn),mid[1]+size*math.sin(turn)]
    lineOne = Line(start[0],start[1],midPoint[0],midPoint[1])
    lineTwo = Line(midPoint[0],midPoint[1],end[0],end[1])
    pathOne.last.next = Node(lineOne)
    pathOne.last = pathOne.last.next
    pathTwo.last.next = Node(lineTwo)
    pathTwo.last = pathTwo.last.next
    return [pathOne,pathTwo]

def recur(n,path,flip,pathList):
    if n == 0:
        pathList.append(path)
    if n > 0:
        paths = draw(path,flip)
        pathList = recur(n-1,paths[0],1,pathList)
        pathList = recur(n-1,paths[1],-1,pathList)
    return pathList

def setUp(s):
    StdDraw.setCanvasSize(768,768)
    StdDraw.setXscale(-s,s)
    StdDraw.setYscale(-s,s)
    StdDraw.filledSquare(0,0,s)

if __name__ == "__main__":
    setUp(1.5)
    s=7
    if len(sys.argv) > 1:
        s = int(sys.argv[1])
    l = Line(-5/6,-0.5,7/6,-0.5)
    n = Node(l)
    p = Path()
    p.start = n
    p.last = n
    pathList = recur(s,p,1,[])
    drawing = True
    colors = [StdDraw.RED,StdDraw.ORANGE,StdDraw.YELLOW,StdDraw.GREEN,StdDraw.CYAN,StdDraw.BLUE,StdDraw.DARK_BLUE,StdDraw.MAGENTA,StdDraw.VIOLET]
    while drawing:
        for i in range(0,len(pathList)):
            g =i
            while g >= len(colors):
                g-=len(colors)
            StdDraw.setPenColor(colors[g])
            drawing = pathList[i].draw()
        StdDraw.show(100)
    StdDraw.setPenColor(StdDraw.WHITE)
    StdDraw.setPenRadius(0.025*(0.9**s))
    for i in range(0,len(pathList)):
        pathList[i].last.l.drawLine()
        StdDraw.show(0.01)
    StdDraw.show(500)
