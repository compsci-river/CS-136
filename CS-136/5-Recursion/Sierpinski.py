#
#River Sheppard
#Sierpinski
#Description: Recusively draws triangles in deminishing sizes following the
#Sierpinski pattern. It draws three triangles around each triange in the
#previous iteration.
#

import sys
import math
import StdDraw

#Draws a filled equilateral triangle point down with side length s and the
#bottom point at x,y
#Inputs: float x, the x position of the bottom point of the triangle. float y,
#the y position of the bottom point of the triangle. float s, the side length of
#the triangle.
#Outputs: null
def filledTriangle(x, y, s):
    a = s/2
    h = a * math.sqrt(3)
    xList = [x, x-a, x+a]
    yList = [y, y+h, y+h]
    StdDraw.filledPolygon(xList, yList)

#Calls filledTriangle and then calls itself three times, to draw the sierpinski
#pattern.
#Inputs: int n, the number of iterations remaining. float x, the x position of
#the bottom point of the triangle. float y, the y position of the bottom point
#of the triangle. float s, the side length of the triangle.
#Outputs: null
def sierpinski(n, x, y, s):
    filledTriangle(x,y,s)
    if n > 1:
        n -= 1
        a = s/2
        h = a * math.sqrt(3)
        sierpinski(n, x-a, y, a)
        sierpinski(n, x+a, y, a)
        sierpinski(n, x, y+h, a)

#Sets everything up. Draws an empty triangle that contains the sierpenski
#pattern. Allows for user input for the number of iterations that should be run,
#then calls sierpenski draw the pattern. Then uses StdDraw.show() to draw the
#pattern.s
if __name__ == "__main__":
    StdDraw.polygon([0, 1, 0.5], [0, 0, 0.5*math.sqrt(3)])
    iterations = 5
    if len(sys.argv) > 1:
        iterations = int(sys.argv[1])
    sierpinski(iterations, 0.5, 0.0, 0.5)
    StdDraw.show(1000)
