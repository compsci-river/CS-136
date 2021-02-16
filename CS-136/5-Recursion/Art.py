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

#Class that defines a Line, along with some helpful methods to retrieve
#information about the line.
class Line:
    #Constructor, takes x,y cordinates for the start and the end of the line
    #Inputs: float x, the x position of the start point. float y, the y position
    #of the start point. float xOne, the x position of the end point. float yOne
    #the y position of the end point.
    #Outputs: null
    def __init__(self,x,y,xOne,yOne):
        self.x = x
        self.y = y
        self.xOne = xOne
        self.yOne = yOne

    #Returns the start position of the line
    #Inputs: null
    #Outputs: List, a list containing the x,y cordinates of the start point
    def getStart(self):
        return [self.x,self.y]

    #Returns the end position of the line
    #Inputs: null
    #Outputs: list, a list containing the x,y cordinates of the end point
    def getEnd(self):
        return [self.xOne,self.yOne]

    #Returns the middle position of the line
    #Inputs: null
    #Outputs: List, a list containing the x,y cordinates of the middle point
    def getMid(self):
        return [(self.x+self.xOne)/2,(self.y+self.yOne)/2]

    #Returns a list of all the needed points, the start point, a point size
    #distance and angle turn away from the middle point and the end point.
    #Inputs: float size, the distance the new point should be from the middle
    #point. float turn, the angle in radians for the new point from the middle
    #point.
    #Outputs: List, a list containing the valid points
    def getPoints(self,size,turn):
        mid = self.getMid()
        midPoint = [mid[0]+size*math.cos(turn),mid[1]+size*math.sin(turn)]
        return self.getStart()+midPoint+self.getEnd()

    #Returns the length of the line
    #Inputs: null
    #Outputs: float s, the length of the line
    def getSize(self):
        y = (self.yOne-self.y)**2
        x = (self.xOne-self.x)**2
        s = math.sqrt(y+x)
        return s

    #Returns the angle that the line is rotated at.
    #Inputs: null
    #Outputs: float, the angle that the line is at in radians
    def getTurn(self):
        y = self.yOne-self.y
        x = self.xOne-self.x
        return math.atan2(y,x)
                
    #Draws the line
    #Inputs: null
    #Outputs: null
    def drawLine(self):
        StdDraw.setPenRadius(self.getSize()*0.05)
        StdDraw.line(self.x,self.y,self.xOne,self.yOne)

    #Draws a polygon between the line and another line
    #Inputs: Line nextLine, the other line to draw the polygon with
    #Outputs: null
    def draw(self,nextLine):
        xList = [self.x,self.xOne,nextLine.xOne,nextLine.x]
        yList = [self.y,self.yOne,nextLine.yOne,nextLine.y]
        StdDraw.filledPolygon(xList,yList)

#A class used to create a linked list of lines
class Node:
    #Constructor
    #Inputs: Line line, the line contained by the node
    def __init__(self,line):
        self.line = line
        self.next = None

#A class that holds a linked list and contains functions to be run on it
class Path:
    #Constructor
    def __init__(self):
        self.start = None
        self.last = None

    #Splits the linked list into two sepereate linked lists, takes each line in
    #each node and cuts it in half and puts each new line in a new node and puts
    #them in a new linked list each with their own path
    #Inputs: null
    #Outputs: List, contains the two new paths
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

    #Pops the first line from the linked list and draws a polygon from it to the
    #next line.
    #Inputs: null
    #Outputs: boolean, whether or not there are more items in the path
    def draw(self):
        node = self.start
        if node.next != None:
            node.line.draw(node.next.line)
            self.start = node.next
            return True
        else:
            return False

#Class for the Heighway Dragon Curve
class DragonCurveAnim:
    #Constuctor
    def __init__(self):
        pass

    #The recursive part of the code, if there are no more iterations remaining
    #adds the current path to paths otherwise it splits the current path and
    #calls itself with the two new paths and decreasing the number of remaining
    #iterations.
    #Inputs: int n, the number of remaining iterations. Path path, the path
    #containing the linked list of the lines that have travelled to this point.
    #int flip, contains 1 or -1 to flip the direction the split occurs.
    #List[Path] paths, the list containing the paths that have been created.
    #Outputs: List[Path] paths, the list containing the paths that have been
    #created
    def dragonCurve(self,n,path,flip,paths):
        if n == 0:
            paths.append(path)
        elif n > 0:
            splitPaths = self.split(path,flip)
            paths = self.dragonCurve(n-1,splitPaths[0],1,paths)
            paths = self.dragonCurve(n-1,splitPaths[1],-1,paths)
        return paths

    #Splits the current path into two paths and also turns the line into a right
    #angle to form the Heighway Dragon Curve
    #Inputs: Path path, the current path, the one you are splitting. int flip,
    #1 or -1 which work to flip the right angle in the correct direction.
    #Outputs: List[Path] paths, a list containing the two new paths
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

    #Draws the path that the lines took in the given colors, forms a cool
    #pattern formed by the shape of the Heighway Dragon Curve.
    #Inputs: List[Path] paths, the list containing the paths
    #Outputs: null
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
            
    #Draws the Heighway Dragon Curve
    #Inputs: int n, the number of iterations that ran to form the curve.
    #List[Path] paths, the list containing the paths
    #Outputs: null
    def borderDraw(self,n,paths):
        StdDraw.setPenColor(StdDraw.BLACK)
        StdDraw.setPenRadius(0.025*(0.99**n))
        for i in range(0,len(paths)):
            paths[i].last.line.drawLine()
        StdDraw.show(500)

#Class that defines the way the user will interact with the Heighway Dragon
#Curve
class Art:
    #Constructor
    def __init__(self):
        self.curve = DragonCurveAnim()

    #Sets up the StdDraw window
    #Inputs: float s, the scale with which to draw the window.
    #Outputs: null
    def windowSetUp(self,s):
        StdDraw.setCanvasSize(768,768)
        StdDraw.setXscale(-s,s)
        StdDraw.setYscale(-s,s)

    #Draws both the colors and the heighway dragon curve, animates from 1 to n
    #iterations
    #Inputs: int n, the number of iterations that ran to form the curve.
    #List[Path] paths, the list containing the paths
    #Outputs: null
    def full(self,n,path):
        for i in range(1,n+1):
            StdDraw.clear()
            paths = self.curve.dragonCurve(i,path,1,[])
            self.curve.colorDraw(paths)
            self.curve.borderDraw(i,paths)
            StdDraw.show(500)
        print("Finished!")
        StdDraw.show(1000)

    #Draws the colors generated by the heighway dragon curve, animates from 1 to
    #n iterations
    #Inputs: int n, the number of iterations that ran to form the curve.
    #List[Path] paths, the list containing the paths
    #Outputs: null
    def colors(self,n,path):
        for i in range(1,n+1):
            StdDraw.clear()
            paths = self.curve.dragonCurve(i,path,1,[])
            self.curve.colorDraw(paths)
            StdDraw.show(500)
        print("Finished!")
        StdDraw.show(1000)

    #Draws the heighway dragon curve, animates from 1 to n iterations
    #Inputs: int n, the number of iterations that ran to form the curve.
    #List[Path] paths, the list containing the paths
    #Outputs: null
    def outline(self,n,path):
        for i in range(1,n+1):
            StdDraw.clear()
            paths = self.curve.dragonCurve(i,path,1,[])
            self.curve.borderDraw(i,paths)
            StdDraw.show(500)
        print("Finished!")
        StdDraw.show(1000)

    #Takes user input on the StdDraw window to draw a custom line, takes two
    #clicks on the StdDraw window and draws a line between the two points.
    #Inputs: null
    #Outputs: Line line, the line formed by the two clicks
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

    #Runs the program based on the user input
    #Inputs: int n, the number of iterations to run. int mode, the int decribing
    #which method to call. int lineMode, the int describing which line to use.
    #Outputs: null
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

    #Collects user input on how to run the program, allows for system arguments
    #or asks for input in the window
    #Inputs: null
    #Outputs: null
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

#Test main, just triggers the start of the program.
if __name__ == "__main__":
    art = Art()
    art.setUp()

        











        
