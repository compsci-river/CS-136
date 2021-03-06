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

    def getTestValue(self):
        return self.testValue

    def setTestValue(self,value):
        self.testValue = value

    def draw(self,x,y):
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
        self.running = True
        with open(fName) as f:
            for i in range(9):
                line = f.readline().split()
                for j in range(9):
                    val = int(line[j])
                    self.tiles[j][i] = Tile(val)
                    if val == 0:
                        self.empty.append([j,i])
        f.close()
        self.draw()
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
        self.running = False
        self.draw()
        StdDraw.setPenColor(StdDraw.BLACK)
        StdDraw.text(0.5,0.025,"FINISHED")
        StdDraw.show(1000)

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
                self.tiles[i][j].draw(0.1+0.1*i,0.9-0.1*j)
        StdDraw.show(0.001)

    def run(self,n):
        if n >= len(self.empty):
            self.win()
            return
        else:
            a = self.empty[n]
            x = a[0]
            y = a[1]
            poten = self.potenVals(x,y)
            while len(poten) > 0 and self.running:
                self.tiles[x][y].setTestValue(poten[0])
                #self.draw()
                self.run(n+1)
                if self.running:
                    w = self.empty[n+1]
                    self.tiles[w[0]][w[1]].setTestValue(None)
                    poten.pop(0)
            return

if __name__ == "__main__":
    s = Sodoku("Sodoku.txt")
    s.run(0)
            










                    
        
