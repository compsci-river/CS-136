import StdDraw
import math
import sys

 #########################################################################
 #  YOU DO NOT NEED TO MODIFY THIS FILE
 #
 # Taken from section 3.2, An Introduction to Programming (in Java) by Robert
 # Sedgewick and Kevin Wayne
 #
 #  Execution:    python Point.py
 #
 #  Immutable data type for 2D points.
 #
 #########################################################################

class Point:

    def __init__(self, x, y):
        self.x = x   # Cartesian
        self.y = y   # coordinates

    # return Euclidean distance between invoking point self and that
    def distanceTo(self, that):
        dx = self.x - that.x
        dy = self.y - that.y
        return math.sqrt(dx*dx + dy*dy)

    # draw this point using standard draw
    def draw(self):
        StdDraw.point(self.x, self.y)

    # draw the line from the invoking point self to that using standard draw
    def drawTo(self, that):
        StdDraw.line(self.x, self.y, that.x, that.y)

    # return string representation of this point
    def toString(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

# test client
if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        # get dimensions
        lines = file.read().split()
        file.close();
    w = int(lines[0])
    h = int(lines[1])
    StdDraw.setCanvasSize(w, h)
    StdDraw.setXscale(0, w)
    StdDraw.setYscale(0, h)
    StdDraw.setPenRadius(.001)

    StdDraw.show(0)
    prevPoint = Point(0,0)
    # read in and plot points one at at time
    for i  in range(2, len(lines),2):
        x = float(lines[i])
        y = float(lines[i+1])
        p = Point(x, y)
        if i > 2:
            prevPoint.drawTo(p)
        prevPoint = p
        #p.draw()
        StdDraw.show(0)
