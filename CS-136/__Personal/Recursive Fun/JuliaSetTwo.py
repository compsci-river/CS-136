#
#River Sheppard
#Julia Set 2.0
#

import sys
import math
import StdDraw
from color import Color

class Pix:
    def __init__(self,x,y,val):
        self.x = x
        self.y = y
        self.val = val

class Heatmap:
    def __init__(self,res):
        self.res = res
        self.size = 768
        self.scale = self.res/self.size
        self.vals = [[None for i in range(self.res)] for i in range(self.res)]
        self.list = []
        self.setUp()

    def listing(self):
        for ix in range(self.res):
            for iy in range(self.res):
                self.list.append(Pix(ix,iy,self.vals[ix][iy]))
        self.list.sort(key=self.sortVal)
        self.oDraw()

    def oDraw(self):
        le = len(self.list)
        for i in range(le):
            v = i/le
            #print(v)
            StdDraw.setPenColor(self.setColor(v))
            StdDraw.filledSquare(self.list[i].x+0.5,self.list[i].y+0.5,0.5)
            

    def sortVal(self,pix):
        return pix.val

    def setUp(self):
        StdDraw.setCanvasSize(self.size,self.size)
        StdDraw.setXscale(0,self.res)
        StdDraw.setYscale(0,self.res)

    def setColor(self,val):
            v = [0,0.125,0.25,0.375,0.5,0.625,0.75,0.875]
            c = 0
            oneCol = [0,0,0]
            twoCol = [0,0,0]
            cols = [0,0,0]
            if val <= v[1]:
                oneCol = [255,255,255]
                twoCol = [255,0,255]
            elif val <= v[2]:
                c = 1
                oneCol = [255,0,255]
                twoCol = [255,0,0]
            elif val <= v[3]:
                c = 2
                oneCol = [255,0,0]
                twoCol = [255,200,0]
            elif val <= v[4]:
                c = 3
                oneCol = [255,200,0]
                twoCol = [255,255,0]
            elif val <= v[5]:
                c = 4
                oneCol = [255,255,0]
                twoCol = [0,255,0]
            elif val <= v[6]:
                c = 5
                oneCol = [0,255,0]
                twoCol = [0,0,255]
            elif val <= v[7]:
                c = 6
                oneCol = [0,0,255]
                twoCol = [0,0,128]
            else:
                c = 7
                oneCol = [0,0,128]
                twoCol = [0,0,0]
            scTwo = (val - v[c])/0.16
            scOne = (0.16 - scTwo)/0.16

            for i in range(3):
                cols[i] = int((oneCol[i] * scOne) + (twoCol[i] * scTwo))
                if cols[i] > 255:
                    cols[i] = 255
                elif cols[i] < 0:
                    cols[i] = 0

            return Color(cols[0],cols[1],cols[2])

    def draw(self):
        for ix in range(self.res):
            for iy in range(self.res):
                val = self.vals[ix][iy]
                StdDraw.setPenColor(self.setColor(val))
                StdDraw.filledSquare(ix+0.5,iy+0.5,0.5)

class Julia:
    def __init__(self):
        self.res = 1000
        self.min = -1.5
        self.max = 1.5
        self.cover = self.max - self.min
        self.limit = 10
        self.maxIters = 1000
        self.h = Heatmap(self.res)

    def run(self,c):
        for ix in range(self.res):
            for iy in range(self.res):
                z = complex(ix / self.res * self.cover + self.min,
                            iy / self.res * self.cover + self.min)

                iters = 0
                
                while abs(z) <= self.limit and iters < self.maxIters:
                    z = z**2 + c
                    iters += 1

                self.h.vals[ix][iy] = iters / self.maxIters
        self.h.draw()
        #self.h.listing()


if __name__ == "__main__":
    j = Julia()
##    for i in range(200):
##        c = complex(i/200,-1+i/100)
##        StdDraw.clear()
##        j.run(c)
##        print("new")
##        StdDraw.show(1000)
##        s = "ZZZ-"+str(i)+".bmp"
##        StdDraw.save(s)
    c = complex(46/200,-1+46/100)
    j.run(c)
    StdDraw.show(10)
        























                
