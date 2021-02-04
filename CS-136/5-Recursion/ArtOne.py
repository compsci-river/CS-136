#
#River Sheppard
#ArtOne
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

def geomOne(x, y, s):
    StdDraw.setPenColor(randomColor(0,255))
    StdDraw.circle(x,y,s)
    a=s/2
    StdDraw.filledCircle(x,y,a)
    StdDraw.show(0.01)

def recurOne(n, x, y, s, t, nn):
    StdDraw.setPenRadius(0.025 * n/nn)
    geomOne(x,y,s)
    if n > 1:
        n -= 1
        a = s ** 1.1
        if t == 1 or t == 0:
            recurOne(n,x,y+(s+a),a,1,nn)
            if n%2 == 0:
                recurOne(n,x+(s+a),y,a,3,nn)
                recurOne(n,x-(s+a),y,a,4,nn)
        if t == 2 or t == 0:
            recurOne(n,x,y-(s+a),a,2,nn)
            if n%2 == 0:
                recurOne(n,x+(s+a),y,a,3,nn)
                recurOne(n,x-(s+a),y,a,4,nn)
        if t == 3 or t == 0:
            recurOne(n,x+(s+a),y,a,3,nn)
            if n%2 == 0:
                recurOne(n,x,y+(s+a),a,1,nn)
                recurOne(n,x,y-(s+a),a,2,nn)
        if t == 4 or t == 0:
            recurOne(n,x-(s+a),y,a,4,nn)
            if n%2 == 0:
                recurOne(n,x,y+(s+a),a,1,nn)
                recurOne(n,x,y-(s+a),a,2,nn)

def geomTwo(x,y,xTwo,yTwo):
    StdDraw.setPenColor(randomColor(0, 255))
    StdDraw.line(x,y,xTwo,yTwo)
    StdDraw.show(0.01)

def recurTwo(n, x, y, s, nn, turn):
    xOne = x + s * math.cos(turn)
    yOne = y + s * math.sin(turn)
    c = Color(255, int(255/n), int(255/n))
    rad = 0.01 * n/nn
    StdDraw.setPenColor(c)
    StdDraw.setPenRadius(rad)
    geomTwo(x,y,xOne,yOne)
    if n > 1:
        n -= 1
        s = s - s/(10*(nn-n))
        tilt = (math.pi/3)/(n)
        recurTwo(n,xOne,yOne,s,nn,turn-tilt)
        recurTwo(n,xOne,yOne,s,nn,turn+tilt)

def geomThree(x, y, s):
    #StdDraw.setPenColor(randomColor(0,255))
    StdDraw.circle(x,y,s)
    a=s/2
    StdDraw.filledCircle(x,y,a)
    StdDraw.show(0.01)

def recurThree(n, x, y, s, t, nn):
    g = (nn-n) * 25
    h = (nn-n+1)* 25
    c = randomColor(g,h)
    StdDraw.setPenColor(c)
    StdDraw.setPenRadius(0.025 * n/nn)
    geomThree(x,y,s)
    if n > 1:
        n -= 1
        a = s ** 1.1
        if t == 1 or t == 0:
            recurThree(n,x,y+(s+a),a,1,nn)
            if n%2 == 0:
                recurThree(n,x+(s+a),y,a,3,nn)
                recurThree(n,x-(s+a),y,a,4,nn)
        if t == 2 or t == 0:
            recurThree(n,x,y-(s+a),a,2,nn)
            if n%2 == 0:
                recurThree(n,x+(s+a),y,a,3,nn)
                recurThree(n,x-(s+a),y,a,4,nn)
        if t == 3 or t == 0:
            recurThree(n,x+(s+a),y,a,3,nn)
            if n%2 == 0:
                recurThree(n,x,y+(s+a),a,1,nn)
                recurThree(n,x,y-(s+a),a,2,nn)
        if t == 4 or t == 0:
            recurThree(n,x-(s+a),y,a,4,nn)
            if n%2 == 0:
                recurThree(n,x,y+(s+a),a,1,nn)
                recurThree(n,x,y-(s+a),a,2,nn)
        
        

if __name__ == "__main__":
    n = 9
    recursion = 1
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    if len(sys.argv) > 2:
        recursion = int(sys.argv[2])
    if recursion == 2:
        StdDraw.setCanvasSize(1024,1024)
        StdDraw.setXscale(0,3)
        StdDraw.setYscale(0,3)
        recurOne(n, 1.5, 1.5, 0.15,0,n)
    elif recursion == 3:
        StdDraw.setPenColor(Color(0,0,0))
        StdDraw.filledRectangle(0,0,1,1)
        turn = 0.0
        for i in range(0,n):
            turn += 2 * math.pi/n
            recurTwo(n, 0.5, 0.5, 0.05, n, turn)
    elif recursion == 1:
        StdDraw.setCanvasSize(1024,1024)
        StdDraw.setXscale(0,3)
        StdDraw.setYscale(0,3)
        StdDraw.setPenColor(Color(0,0,0))
        StdDraw.filledRectangle(0,0,3,3)
        recurThree(n, 1.5, 1.5, 0.15,0,n)
        turn = 0.0
        for i in range(0,n):
            turn += 2 * math.pi/n
            recurTwo(n, 1.5, 1.5, 0.15, n, turn)
    StdDraw.show(1000)
