#
#River Sheppard
#Fibonacci
#

import math
import StdDraw

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def X(self):
        return self.x

    def Y(self):
        return self.y

    def dist(self,p):
        xOne = (p.X()-self.x)**2
        yOne = (p.Y()-self.y)**2
        return math.sqrt(xOne+yOne)

class Line:
    def __init__(self,pOne,pTwo):
        self.pOne = pOne
        self.pTwo = pTwo

    def getSize(self):
        pass

    def getTurn(self):
        pass

class Rect:
    def __init__(self,p,pOne,pTwo,pThree):
        self.p = p
        self.pOne = pOne
        self.pTwo = pTwo
        self.pThree = pThree

    def newCorn(self):
        return self.pTwo

    def draw(self):
        x = [self.p.X(),self.pOne.X(),self.pTwo.X(),self.pThree.X()]
        y = [self.p.Y(),self.pOne.Y(),self.pTwo.Y(),self.pThree.Y()]
        StdDraw.polygon(x,y)

    def side(self):
        d = self.p.dist(self.pOne)
        if self.p.dist(self.pThree) > d:
            d = self.p.dist(self.pThree)
        return d

def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

def square(n,seq,t,p,rrs):
    if n < len(seq):
        a = 0
        d = seq[n]
        r = None
        x = p.X()
        y = p.Y()
        tt = 0
        for i in range((n+1)%2,n,2):
            a += seq[i]
        if t == 1:
            r = Rect(p, Point(x-d,y),Point(x-d,y-a),Point(x,y-a))
            tt = 2
        elif t == 2:
            r = Rect(p,Point(x,y-d),Point(x+a,y-d),Point(x+a,y))
            tt = 3
        elif t == 3:
            r = Rect(p,Point(x+d,y),Point(x+d,y+a),Point(x,y+a))
            tt = 4
        elif t == 4:
            r = Rect(p,Point(x,y+d),Point(x-a,y+d),Point(x-a,y))
            tt = 1
        
        rr = square(n+1,seq,tt,r.newCorn(),rrs)
        rr.append(r)
        return rr
    else:
        return []

def setUp(d):
    StdDraw.setCanvasSize(1024,1024)
    StdDraw.setXscale(-d,d)
    StdDraw.setYscale(-d,d)
    StdDraw.setPenRadius(0.001)

def draw(n):
    seq = []
    for i in range(0,n+1):
        c = fibonacci(i)
        seq.append(c)
    rrs = square(1,seq,1,Point(0,1),[])
    a = 0
    for i in range((n+1)%2,n,2):
            a += seq[i]
    setUp(a)
    for r in rrs:
        r.draw()

if __name__ == "__main__":
    draw(15)
    StdDraw.show(1000)






        
