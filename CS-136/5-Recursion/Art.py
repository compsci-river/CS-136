#
#River Sheppard
#Art
#Description:
#

import sys
import math
import random
import StdDraw
from color import Color

def randomColor(sLimit, limit):
    one = random.randint(sLimit,limit)
    two = random.randint(sLimit,limit)
    three = random.randint(sLimit,limit)
    c = Color(one,two,three)
    return c

def setColor(colorSet,n,fullN):
    col = n * int(255/fullN)
    if col < 0:
        col = 0
    if col > 255:
        col = 255
    if colorSet == 0:
        StdDraw.setPenColor(Color(255-col,255-col,255-col))
    elif colorSet == 1:
        StdDraw.setPenColor(Color(col,col,col))
    elif colorSet == 2:
        StdDraw.setPenColor(Color(255,255-col,255-col))
    elif colorSet == 3:
        StdDraw.setPenColor(Color(255-col,255,255-col))
    elif colorSet == 4:
        StdDraw.setPenColor(Color(255-col,255-col,255))
    if colorSet == 5:
        StdDraw.setPenColor(randomColor(0,255))
    if colorSet == 6:
        StdDraw.setPenColor(Color(255,255,255))

def geom(geomType, x, y, extra):
    if geomType == 0:
        StdDraw.filledCircle(x,y,extra)
    elif geomType == 1:
        StdDraw.circle(x,y,extra)
    elif geomType == 2:
        StdDraw.line(x,y,extra[0],extra[1])
    StdDraw.show(0.001)

def tree(n,fullN,x,y,size,turn,colorSet):
    setColor(colorSet,n,fullN)
    StdDraw.setPenRadius(0.015*n/fullN)
    extra = [float(x) + size * math.cos(turn),float(y) + size * math.sin(turn)]
    geom(2,x,y,extra)
    n -= 1
    if n > 0:
        size -= size/(10*(fullN-n))
        tilt = (math.pi/3)/n
        tree(n,fullN,extra[0],extra[1],size,turn-tilt,colorSet)
        tree(n,fullN,extra[0],extra[1],size,turn+tilt,colorSet)

def startTree(n,colorSet):
    turn = 0.0
    for i in range(0,8):
        turn += 2 * math.pi/8
        tree(n,n,1.5,1.5,0.2,turn,colorSet)

def circle(n,fullN,x,y,size,turn,colorSet):
    setColor(colorSet,n,fullN)
    StdDraw.setPenRadius(0.01 * n/fullN)
    geom(1,x,y,size)
    geom(0,x,y,size/2)
    n -= 1
    if n > 0:
        a = size ** 1.1
        if turn == 0:
            circle(n,fullN,x,y+(size+a),a,1,colorSet)
            circle(n,fullN,x+(size+a),y,a,2,colorSet)
            circle(n,fullN,x,y-(size+a),a,3,colorSet)
            circle(n,fullN,x-(size+a),y,a,4,colorSet)
        elif turn == 1:
            circle(n,fullN,x,y+(size+a),a,1,colorSet)
            if n%2 == 0:
                circle(int(n/2),fullN,x+(size+a),y,a,2,colorSet)
                circle(int(n/2),fullN,x-(size+a),y,a,4,colorSet)
        elif turn == 2:
            circle(n,fullN,x+(size+a),y,a,2,colorSet)
            if n%2 == 0:
                circle(int(n/2),fullN,x,y+(size+a),a,1,colorSet)
                circle(int(n/2),fullN,x,y-(size+a),a,3,colorSet)
        elif turn == 3:
            circle(n,fullN,x,y-(size+a),a,3,colorSet)
            if n%2 == 0:
                circle(int(n/2),fullN,x+(size+a),y,a,2,colorSet)
                circle(int(n/2),fullN,x-(size+a),y,a,4,colorSet)
        elif turn == 4:
            circle(n,fullN,x-(size+a),y,a,4,colorSet)
            if n%2 == 0:
                circle(int(n/2),fullN,x,y+(size+a),a,1,colorSet)
                circle(int(n/2),fullN,x,y-(size+a),a,3,colorSet)

def startCircle(n,colorSet):
    circle(n,n,1.5,1.5,0.175,0,colorSet)

def fern(n,fullN,x,y,size,turn,colorSet):
    setColor(colorSet,n,fullN)
    StdDraw.setPenRadius(0.01 * n/fullN)
    geom(0,x,y,size)
    n -= 1
    if n > 0:
        if turn == 0:
            a = size * 14/15
            fern(n,fullN,x,y+size+a,a,turn,colorSet)
            fern(n,fullN,x-3*size/2,y,size/2,1,colorSet)
            fern(n,fullN,x+3*size/2,y,size/2,1,colorSet)
        else:
            if x > 1.5:
                fern(n,fullN,x+size*29/15,y+math.sin(turn)*2*size,size*14/15,turn+1,colorSet)
            else:
                fern(n,fullN,x-size*29/15,y+math.sin(turn)*2*size,size*14/15,turn+1,colorSet)

def startFern(n,colorSet):
    fern(n,n,1.5,0.1,0.1,0,colorSet)

def setUp():
    StdDraw.setCanvasSize(768,768)
    StdDraw.setXscale(0,3)
    StdDraw.setYscale(0,3)
    StdDraw.setPenColor(Color(0,0,0))
    StdDraw.filledRectangle(0,0,3,3)

if __name__ == "__main__":
    n = 9
    colorTree = 5
    colorCircle = 6
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    if len(sys.argv) > 2:
        colorTree = int(sys.argv[2])
    if len(sys.argv) > 3:
        colorCircle = int(sys.argv[3])
    setUp()
    startCircle(n,colorCircle)
    startTree(n,colorTree)
    #startFern(50,5)
    
    




        
