#
#River Sheppard
#Cycle Insertion
#

import sys
from Point import Point
from Tour import Tour
import StdDraw

filename = sys.argv[1]
with open(filename, 'r') as file:
    lines = file.read().split()
    file.close()

w = int(lines[0])
h = int(lines[1])
StdDraw.setCanvasSize(w, h)
StdDraw.setXscale(0, w)
StdDraw.setYscale(0, h)

tourList = Tour()
tour = Tour()
for i in range (2, len(lines),2):
    x = float(lines[i])
    y = float(lines[i+1])
    p = Point(x, y)
    tourList.insertInOrder(p)
    tour.insertInOrder(p)

print("Tour distance = " + str(tour.distance()))
tour.draw()
StdDraw.show(1)

tour.cyclePoints(tourList)

tour.draw()
StdDraw.show(10000)

##ended = True
##
##while ended:
##    StdDraw.show(1)
##    if StdDraw.hasNextKeyTyped():
##        ended = False


