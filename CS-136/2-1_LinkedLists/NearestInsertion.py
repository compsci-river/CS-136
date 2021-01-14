import sys
from Point import Point
from Tour import Tour
import StdDraw

 #########################################################################
 #  YOU DO NOT NEED TO MODIFY THIS FILE
 #
 #  Execution:    python NearestInsertion.py <file.txt>
 #  Dependencies: Tour.py Point.py StdIn.py StdDraw.py
 #
 #  Run nearest neighbor insertion heuristic for traveling
 #  salesperson problemand plot results. For example:
 #
 #  % python NearestInsertion.py tsp1000.txt
 #
 #########################################################################/

filename = sys.argv[1]
delay = -1
if len(sys.argv) > 2:
    delay = float(sys.argv[2])
with open(filename, 'r') as file:
    lines = file.read().split()
    file.close()
        
# get dimensions
w = int(lines[0])
h = int(lines[1])
StdDraw.setCanvasSize(w, h)
StdDraw.setXscale(0, w)
StdDraw.setYscale(0, h)

# turn on animation mode
StdDraw.show(0)

# run nearest insertion heuristic
tour = Tour()
for i in range (2, len(lines),2):
    x = float(lines[i])
    y = float(lines[i+1])
    p = Point(x, y)
    tour.insertNearest(p)
    if delay > -1:
        StdDraw.clear()
        tour.draw()
        StdDraw.show(delay)

# draw to standard draw
tour.draw()
StdDraw.show(5000)

# print tour to standard output
print("Tour distance = " + str(tour.distance()))
tour.show()
