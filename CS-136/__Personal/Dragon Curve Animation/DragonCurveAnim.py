#
#River Sheppard
#Animated Dragon Curve
#

import math
import StdDraw

class Line:
    def __init__(self,x):
        self.line = x

    def getStart(self):
        return [self.line[0],self.line[1]]

    def getEnd(self):
        return [self.line[2],self.line[3]]
    
    def getMid(self):
        return [(self.line[0]+self.line[2])/2,(self.line[1]+self.line[3])/2]

    def getMag(self):
        return math.sqrt(((self.line[2]-self.line[0])**2)+((self.line[3]-self.line[1])**2))

    def getRot(self):
        return math.atan2(self.line[3]-self.line[1],self.line[2]-self.line[0])

    def getDirMid(self):
        t = self.getRot() + self.line[4] * math.pi/4
        a = self.getMag() / math.sqrt(2)
        return [self.line[0]+a*math.cos(t),self.line[1]+a*math.sin(t)]

    def getLineSegments(self):
        m = self.getMid()
        d = self.getDirMid()
        return [Line([self.line[0],self.line[1],m[0],m[1],1]),
                Line([self.line[0],self.line[1],d[0],d[1],1]),
                Line([m[0],m[1],self.line[2],self.line[3],-1]),
                Line([d[0],d[1],self.line[2],self.line[3],-1])]

    def draw(self):
        StdDraw.line(self.line[0],self.line[1],self.line[2],self.line[3])

    def getInterval(self,x,xOne,percent):
        return x + (xOne - x) * percent;

    def getIntervalLine(self,target,percent):
        return Line([self.getInterval(self.line[0],target.line[0],percent),
                     self.getInterval(self.line[1],target.line[1],percent),
                     self.getInterval(self.line[2],target.line[2],percent),
                     self.getInterval(self.line[3],target.line[3],percent),
                     self.line[4]])
        

class DragonCurve:
    def __init__(self,n,s):
        self.n = n
        self.setUp(s)
        self.lines = [Line([-s/2,0,s/2,0,1])]
        self.targets = []
        self.run()

    def setUp(self,s):
        StdDraw.setCanvasSize(768,768)
        StdDraw.setXscale(-s,s)
        StdDraw.setYscale(-s,s)

    def run(self):
        m = 0
        while self.n > m:
            m += 1
            newLines = []
            newTargets = []
            for line in self.lines:
                temp = line.getLineSegments()
                for i in range(2):
                    newLines.append(temp[2*i])
                    newTargets.append(temp[2*i+1])
            self.lines = newLines
            self.targets = newTargets
            self.draw(m)
            self.lines = self.targets

    def draw(self,m):
        StdDraw.setPenRadius(0.025*(0.9**m))
        for i in range(25):
            StdDraw.clear()
            for j in range(len(self.lines)):
                s = self.lines[j]
                t = self.targets[j]
                s.getIntervalLine(t,i/25).draw()
            StdDraw.show(10)
        StdDraw.show(100)
            


if __name__ == "__main__":
    n = 13
    s = 1
    d = DragonCurve(n,s)
    print("Done.")
    

    
