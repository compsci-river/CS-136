#
#River Sheppard
#Sodoku Solver
#

import StdDraw

class Tile:
    def __init__(self,value):
        self.value = None
        if value != 0:
            self.value = value
        self.testValue = self.value

    def getValue(self):
        return self.value

    def getTestValue(self):
        return self.testValue

    def setTestValue(self,value):
        self.testValue = value

    def validate(self):
        self.value = self.testValue

    def draw(self,x,y):
        #StdDraw.setPenColor(StdDraw.WHITE)
        #StdDraw.filledSquare(x,y,0.05)
        if self.value != None:
            StdDraw.setPenColor(StdDraw.BLACK)
            StdDraw.text(x,y,str(self.value))
        elif self.testValue != None:
            StdDraw.setPenColor(StdDraw.RED)
            StdDraw.text(x,y,str(self.testValue))

class Sodoku:
    def __init__(self,fName):
        self.tiles = [[None for i in range(9)] for j in range(9)]
        self.empty = []
        with open(fName) as f:
            for i in range(9):
                line = f.readline().split()
                for j in range(9):
                    val = int(line[j])
                    self.tiles[j][i] = Tile(val)
                    if val == 0:
                        self.empty.append([j,i])
        pass

    def potenVals(self,x,y):
        values = self.rowValues(y,self.columnValues(x,self.squareValues(x,y,[])))
        poten = []
        for i in range(1,10):
            if i not in values:
                poten.append(i)
        return poten

    def rowValues(self,y,values):
        for i in range(9):
            val = self.tiles[i][y].getTestValue()
            if val != None and val not in values:
                values.append(val)
        return values

    def columnValues(self,x,values):
        for i in range(9):
            val = self.tiles[x][i].getTestValue()
            if val != None and val not in values:
                values.append(val)
        return values

    def squareValues(self,x,y,values):
        squareX = self.findSquare(x)
        squareY = self.findSquare(y)
        for i in range(3):
            for j in range(3):
                val = self.tiles[squareX+i][squareY+j].getTestValue()
                if val != None and val not in values:
                    values.append(val)
        return values

    def findSquare(self,v):
        square = 0
        if v >= 3:
            square = 3
            if v >= 6:
                square = 6
        return square

    def win(self):
        for i in range(9):
            for j in range(9):
                self.tiles[i][j].validate()
        self.draw()
        StdDraw.show(1000000)

    def draw(self):
        StdDraw.clear()
        for i in range(10):
            StdDraw.line(0.05,0.05+0.1*i,0.95,0.05+0.1*i)
            StdDraw.line(0.05+0.1*i,0.05,0.05+0.1*i,0.95)
        for i in range(9):
            for j in range(9):
                self.tiles[i][j].draw(0.1+0.1*i,0.9-0.1*j)
        StdDraw.show(0.001)

    def run(self,n):
        if n >= len(self.empty):
            print("end")
            self.win()
        else:
            a = self.empty[n]
            x = a[0]
            y = a[1]
            poten = self.potenVals(x,y)
            while len(poten) > 0:
                self.tiles[x][y].setTestValue(poten[0])
                self.draw()
                self.run(n+1)
                for i in range(n+1,len(self.empty)):
                    w = self.empty[i]
                    u = w[0]
                    v = w[1]
                    self.tiles[u][v].setTestValue(None)
                poten.pop(0)

if __name__ == "__main__":
    s = Sodoku("Sodoku.txt")
    s.run(0)
            










                    
        
