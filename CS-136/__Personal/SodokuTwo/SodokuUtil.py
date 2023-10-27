#
#River Sheppard
#Sodoku
#

import random
import StdDraw

class Tile:
    def __init__(self, value):
        self.value = None
        if value != 0:
            self.value = value
        self.testValue = self.value

    def getTestValue(self):
        return self.testValue

    def setTestValue(self, value):
        self.testValue = value

    def setValue(self):
        self.value = self.testValue

    def draw(self,x,y):
        if self.value != 0:
            StdDraw.setPenColor(StdDraw.BLACK)
            StdDraw.text(x,y,str(self.value))
        elif self.testValue != self.value:
            StdDraw.setPenColor(StdDraw.RED)
            StdDraw.text(x,y,str(self.testValue))


class Sodoku:
    def __init__(self, fName):
        self.grid = [[None for i in range(9)] for j in range(9)]
        self.empty = []
        self.running = True
        with open(fName) as f:
            for i in range(9):
                line = f.readline().split()
                for j in range(9):
                    val = int(line[j])
                    self.grid[j][i] = Tile(val)
                    if val == 0:
                        self.empty.append([j,i])
        f.close()
        pass

    def findSquare(self,v):
        square = 0
        if v >= 3:
            square = 3
            if v >= 6:
                square = 6
        return square

    def squareValues(self,x,y,values):
        squareX = self.findSquare(x)
        squareY = self.findSquare(y)
        for i in range(3):
            for j in range(3):
                val = self.grid[squareX+i][squareY+j].getTestValue()
                if val != None and val not in values:
                    values.append(val)
        return values

    def columnValues(self,x,values):
        for i in range(9):
            val = self.grid[x][i].getTestValue()
            if val != None and val not in values:
                values.append(val)
        return values

    def rowValues(self, y, values):
        for i in range(9):
            val = self.grid[i][y].getTestValue()
            if val != None and val not in values:
                values.append(val)
        return values

    def getPoten(self, x, y):
        values = self.rowValues(y,self.columnValues(x,self.squareValues(x,y,[])))
        poten = []
        for i in range(1,10):
            if i not in values:
                poten.append(i)
        return poten

    def fill(self, n):
        if n>= len(self.empty):
            self.running = False
        else:
            a = self.empty[n]
            x = a[0]
            y = a[1]
            poten = self.getPoten(x,y)
            while len(poten) > 0 and self.running:
                index = random.randint(0,len(poten)-1)
                self.grid[x][y].setTestValue(poten[index])
                self.fill(n+1)
                if self.running:
                    w = self.empty[n+1]
                    self.grid[w[0]][w[1]].setTestValue(None)
                    poten.pop(index)
            return

    def solve(self, n):
        if n>= len(self.empty):
            self.running = False
        else:
            a = self.empty[n]
            x = a[0]
            y = a[1]
            poten = self.getPoten(x,y)
            while len(poten) > 0 and self.running:
                self.grid[x][y].setTestValue(poten[0])
                self.solve(n+1)
                if self.running:
                    w = self.empty[n+1]
                    self.grid[w[0]][w[1]].setTestValue(None)
                    poten.pop(0)
            return

    def countSolutions(self):
        self.solve(0)
        a = self.empty[len(self.empty)-1]
        return len(self.getPoten(a[0],a[1]))

    def setValues(self):
        for i in range(9):
            for j in range(9):
                self.grid[i][j].setValue()

    def writeSodoku(self, fName):
        s = ""
        for i in range(9):
            for j in range(9):
                val = self.grid[i][j].getTestValue()
                if val == None:
                    val = 0
                s += str(val) + " "
            s += "\n"
        f = open(fName, "w")
        f.write(s)
        f.close()

    def removeValue(self):
        inty = random.randint(0,8)
        intx = random.randint(0,8)
        hold = self.grid[intx][inty].getTestValue()
        self.grid[intx][inty].setTestValue(0)
        self.empty.append([intx,inty])
        if self.countSolutions() == 1:
            self.grid[intx][inty].setValue()
        else:
            self.grid[intx][inty].setTestValue(hold)
            self.empty.pop(len(self.empty)-1)

    def draw(self):
        StdDraw.clear()
        StdDraw.setFontSize(20)
        for i in range(10):
            StdDraw.setPenColor(StdDraw.BLACK)
            if i == 3 or i == 6:
                StdDraw.setPenRadius(0.006)
            else:
                StdDraw.setPenRadius(0.0015)
            StdDraw.line(0.05,0.05+0.1*i,0.95,0.05+0.1*i)
            StdDraw.line(0.05+0.1*i,0.05,0.05+0.1*i,0.95)
        for i in range(9):
            for j in range(9):
                self.grid[i][j].draw(0.1+0.1*i,0.9-0.1*j)
        StdDraw.show(0.001)
        

def generateSodoku(n):
    s = Sodoku("Blank.txt")
    s.fill(0)
    while(s.countSolutions() > 1):
        s.fill(0)
    s.setValues()
    s.writeSodoku("Sodoku.txt")
    s = Sodoku("Sodoku.txt")
    while n > 0:
        s.removeValue()
        n = n - 1
    s.setValues()
    s.writeSodoku("Puzzle.txt")
    s.draw()
            



if __name__ == "__main__":
    generateSodoku(50000)






            
