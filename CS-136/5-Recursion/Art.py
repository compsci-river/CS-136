#
#River Sheppard
#Art
#Description: Mostly the Heighway Dragon curve, but I save the route that each
#line segment travels and draw it as well. Then I also gave the option of
#creating a custom line using StdDraw input. The Heighway Dragon Curve is a
#famous fractal, where each line segment is turned into a right angle in
#alternating directions.
#

import sys
import math
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
        return math.atan2(y,x)
                

    def drawLine(self):
        StdDraw.setPenRadius(self.getSize()*0.025)
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
            StdDraw.show(100)
            for i in range(0,len(paths)):
                spin = i
                while spin >= len(colors):
                    spin -= len(colors)
                StdDraw.setPenColor(colors[spin])
                drawing = paths[i].draw()
            

    def borderDraw(self,n,paths):
        StdDraw.setPenColor(StdDraw.BLACK)
        StdDraw.setPenRadius(0.025*(0.9**n))
        for i in range(0,len(paths)):
            paths[i].last.line.drawLine()
        StdDraw.show(500)

class Art:
    def __init__(self):
        self.curve = DragonCurveAnim()

    def windowSetUp(self,s):
        StdDraw.setCanvasSize(1024,1024)
        StdDraw.setXscale(-s,s)
        StdDraw.setYscale(-s,s)

    def full(self,n,path):
        for i in range(1,n+1):
            StdDraw.clear()
            paths = self.curve.dragonCurve(i,path,1,[])
            self.curve.colorDraw(paths)
            self.curve.borderDraw(i,paths)
            StdDraw.show(500)

    def colors(self,n,path):
        for i in range(1,n+1):
            StdDraw.clear()
            paths = self.curve.dragonCurve(i,path,1,[])
            self.curve.colorDraw(paths)
            StdDraw.show(500)

    def outline(self,n,path):
        for i in range(1,n+1):
            StdDraw.clear()
            paths = self.curve.dragonCurve(i,path,1,[])
            self.curve.borderDraw(i,paths)
            StdDraw.show(500)

    def customLine(self):
        pointOne = False
        pointTwo = False
        one = []
        two = []
        print("Click somewhere on the StdDraw window to select the start point of the line")
        StdDraw.setPenColor(StdDraw.WHITE)
        StdDraw.filledSquare(0,0,1.5)
        StdDraw.show(100)
        while not pointOne:
            if StdDraw.mousePressed():
                one = [StdDraw.mouseX(),StdDraw.mouseY()]
                pointOne = True
            StdDraw.show(10)
        print("Click on the StdDraw window again to select the end point of the line")
        while not pointTwo:
            if StdDraw.mousePressed():
                two = [StdDraw.mouseX(),StdDraw.mouseY()]
                pointTwo = True
            StdDraw.show(10)
        line = Line(one[0],one[1],two[0],two[1])
        StdDraw.setPenColor(StdDraw.BLACK)
        line.drawLine()
        StdDraw.show(100)
        return line

    def run(self,n,mode,lineMode):
        self.windowSetUp(1.5)
        line = Line(-5/6,-1/3,7/6,-1/3)
        if lineMode == 2:
            line = Line(-1,-1,1,1)
        elif lineMode == 3:
            line = self.customLine()
        node = Node(line)
        path = Path()
        path.start = node
        path.last = node
        if mode == 2:
            self.colors(n,path)
        elif mode == 3:
            self.outline(n,path)
        else:
            self.full(n,path)

    def setUp(self):
        n = 7
        if len(sys.argv) > 1:
            n = int(sys.argv[1])
        else:
            n = int(input("How many iterations should run: "))

        mode = 0
        if len(sys.argv) > 2:
            mode = int(sys.argv[2])
        else:
            mode = int(input("Modes:\n1: Full\n2: Colors\n3: Borders\nPlease select an option: "))

        lineMode = 0
        if len(sys.argv) > 3:
            lineMode = int(sys.argv[3])
        else:
            lineMode = int(input("Line options:\n1: Standard\n2: Diagonal\n3: Custom\nPlease select an option: "))
        self.run(n,mode,lineMode)

if __name__ == "__main__":
    art = Art()
    art.setUp()
    
##    n = 7
##    if len(sys.argv) > 1:
##        n = int(sys.argv[1])
##    
##    line = Line(-5/6,-1/3,7/6,-1/3)
##    node = Node(line)
##    path = Path()
##    path.start = node
##    path.last = node
##    curve = DragonCurveAnim()
##    curve.setUp(s)
##    for i in range(1,n+1):
##        StdDraw.clear()
##        StdDraw.setPenColor(StdDraw.BLACK)
##        StdDraw.filledSquare(0,0,s)
##        curve.runAll(i,path,1)
##        StdDraw.show(500)
##    StdDraw.show(1000)
        
        











        
