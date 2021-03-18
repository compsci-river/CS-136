#
#River Sheppard
#Julia Sets
#

import sys
import math
import random
import StdDraw
from color import Color

class Pix:
    def __init__(self,x,y,i):
        self.x = x
        self.y = y
        self.i = i
        self.col = None

    def getPos(self):
        return [self.x,self.y]

    def getI(self):
        return self.i

    def setCol(self,col):
        self.col = col

    def draw(self):
        StdDraw.setPenColor(self.col)
        StdDraw._pixel(self.x,self.y)

class Node:
    def __init__(self):
        self.item = None
        self.next = None

class Julia:
    def __init__(self):
        self.res = 500
        self.min = -1.5
        self.max = 1.5
        self.cover = self.max - self.min
        self.limit = 10
        self.maxIters = 1000
        self.setUp()
        self.first = None
        self.length = 0

    def setUp(self):
        a = self.res
        StdDraw.setCanvasSize(a,a)
        StdDraw.setXscale(0,a)
        StdDraw.setYscale(0,a)

    def run(self,c):
        print("running")
        for ix in range(self.res):
            for iy in range(self.res):
                z = complex(ix / self.res * self.cover + self.min,
                            iy / self.res * self.cover + self.min)
                iters = 0
                while abs(z) <= self.limit and iters < self.maxIters:
                    z = z**2 + c
                    iters += 1
                self.addPixel(Pix(ix,iy,iters))
        self.addColor()
        self.draw()

    def draw(self):
        print("drawing")
        node = self.first
        while node != None:
            node.item.draw()
            node = node.next

    def addPixel(self,pix):
        self.length += 1
        if self.length%1000 == 0:
            print(self.length)
        pI = pix.getI()
        node = Node()
        node.item = pix
        if self.first == None:
            self.first = node
        elif self.first.item.getI() >= pI:
            node.next = self.first
            self.first = node
        elif self.first.next == None:
            self.first.next = node
        else:
            #print("hi")
            test = self.first
            trailing = None
            running = True
            while test.item.getI() < pI and running:
                #print("a")
                if test.next == None:
                    running = False
                else:
                    #print("u")
                    trailing = test
                    test = test.next
            node.next = test
            trailing.next = node
        

    def addColor(self):
        print("adding color")
        node = self.first
        count = 1
        while node != None:
            node.item.setCol(self.setColor(count,self.length))
            node = node.next
            count += 1

    def setColor(self,iters,length):
        shortVal = int(length/50)
        valRange = length - 2 * shortVal
        cover = int(valRange/6)
        if iters <= shortVal:
            return StdDraw.WHITE
        elif iters >= length - shortVal:
            return StdDraw.BLACK
        else:
            twoScale = 0
            oneScale = 0
            oneCol = [0,0,0]
            twoCol = [0,0,0]
            cols = [0,0,0]
            if iters <= cover + shortVal:
                twoScale =  (iters - shortVal)/cover
                oneScale = (cover - twoScale)/cover
                oneCol = [255,0,255]
                twoCol = [255,0,0]
            elif iters <= 2*cover + shortVal:
                twoScale =  (iters - (cover+shortVal))/cover
                oneScale = (cover - twoScale)/cover
                oneCol = [255,0,0]
                twoCol = [255,200,0]
            elif iters <= 3*cover + shortVal:
                twoScale =  (iters - (2*cover+shortVal))/cover
                oneScale = (cover - twoScale)/cover
                oneCol = [255,200,0]
                twoCol = [255,255,0]
            elif iters <= 4*cover + shortVal:
                twoScale =  (iters - (3*cover+shortVal))/cover
                oneScale = (cover - twoScale)/cover
                oneCol = [255,255,0]
                twoCol = [0,255,0]
            elif iters <= 5*cover+shortVal:
                twoScale =  (iters - (4*cover+shortVal))/cover
                oneScale = (cover - twoScale)/cover
                oneCol = [0,255,0]
                twoCol = [0,0,255]
            else:
                twoScale =  (iters - (5*cover+shortVal))/cover
                oneScale = (cover - twoScale)/cover
                oneCol = [0,0,255]
                twoCol = [0,0,128]
            for i in range(3):
                cols[i] = int((oneCol[i] * oneScale) + (twoCol[i] * twoScale))
                if cols[i] > 255:
                    cols[i] = 255
                elif cols[i] < 0:
                    cols[i] = 0

            return Color(cols[0],cols[1],cols[2])







if __name__ == "__main__":
    j = Julia()
    c = complex(-0.4,-0.59)
    j.run(c)
    StdDraw.show(1000)
        
