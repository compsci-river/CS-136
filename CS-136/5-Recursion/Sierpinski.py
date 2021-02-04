#
#River Sheppard
#Sierpinski
#Description: Recusively draws triangles in deminishing sizes
#

import sys
import math
import StdDraw

def filledTriangle(x, y, s):
    a = s/2
    h = a * math.sqrt(3)
    xList = [x, x-a, x+a]
    yList = [y, y+h, y+h]
    StdDraw.filledPolygon(xList, yList)

def sierpinski(n, x, y, s):
    filledTriangle(x,y,s)
    if n > 1:
        n -= 1
        a = s/2
        h = a * math.sqrt(3)
        sierpinski(n, x-a, y, a)
        sierpinski(n, x+a, y, a)
        sierpinski(n, x, y+h, a)

if __name__ == "__main__":
    StdDraw.polygon([0, 1, 0.5], [0, 0, 0.5*math.sqrt(3)])
    iterations = 5
    if len(sys.argv) > 1:
        iterations = int(sys.argv[1])
    sierpinski(iterations, 0.5, 0.0, 0.5)
    StdDraw.show(1000)
