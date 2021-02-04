#
#River Sheppard
#Farthest Insertion
#

import sys
from Point import Point
from Tour import Tour
import StdDraw

filename = sys.argv[1]
with open(filename, 'r') as file:
    lines = file.read().split()
    file.close()
        
# get dimensions
w = int(lines[0])
h = int(lines[1])
StdDraw.setCanvasSize(w, h)
StdDraw.setXscale(0, w)
StdDraw.setYscale(0, h)

tour = Tour()
tourList = []
for i in range (2, len(lines),2):
    x = float(lines[i])
    y = float(lines[i+1])
    p = Point(x, y)
    tourList = tour.list(p, tourList)

tour.farthestInsertion(tourList)

# draw to standard draw
tour.draw()
check = True
while check:
    StdDraw.show(5000)
    if StdDraw.hasNextKeyTyped():
        check = False

# print tour to standard output
print("Tour distance = " + str(tour.distance()))
tour.show()
