#
#River Sheppard
#CSI 136
#Description: Uses StdDraw to creat a graph that represents the data found by the Benford
#script, the y-values on the side of the graph scale with the data and the precise value
# of each bucket is displayed at the top of each column
#

import sys
import StdDraw
import Benford

class Graph:
    #Constructor
    def __init__(self):
        pass

    #Counts the number of digits in an int
    def intLength(self, num):
        count = 1
        while int(num) >= 1:
            num = num / 10
            if num >= 1:
                count += 1
        return count

    #Finds the largest number in a list
    def greatestInt(self, intList):
        greatInt = 0
        for int in intList:
            if int > greatInt:
                greatInt = int
        return greatInt

    #Finds the number with which to scale the y-axis
    def graphHeight(self, num):
        intLen = self.intLength(num)
        height = 2 * pow(10,intLen-1)
        while num > height:
            height += pow(10,intLen-1)
        return height

    #Draws the blank graph before any data in used
    def graphDraw(self):
        StdDraw.setCanvasSize(600,600)
        StdDraw.setXscale(0,600)
        StdDraw.setYscale(0,600)

        StdDraw.line(50,50,50,550)
        StdDraw.line(50,50,550,50)
        
        StdDraw.line(45,550,55,550)
        StdDraw.line(48,425,52,425)
        StdDraw.line(45,300,55,300)
        StdDraw.line(48,175,52,175) 

        StdDraw.line(75,48,75,52)
        StdDraw.text(75,25, "0")
        StdDraw.line(125,48,125,52)
        StdDraw.text(125,25, "1")
        StdDraw.line(175,48,175,52)
        StdDraw.text(175,25, "2")
        StdDraw.line(225,48,225,52)
        StdDraw.text(225,25, "3")
        StdDraw.line(275,48,275,52)
        StdDraw.text(275,25, "4")
        StdDraw.line(325,48,325,52)
        StdDraw.text(325,25, "5")
        StdDraw.line(375,48,375,52)
        StdDraw.text(375,25, "6")
        StdDraw.line(425,48,425,52)
        StdDraw.text(425,25, "7")
        StdDraw.line(475,48,475,52)
        StdDraw.text(475,25, "8")
        StdDraw.line(525,48,525,52)
        StdDraw.text(525,25, "9")
        StdDraw.line(550,45,550,55)
        StdDraw.show(0.0)

    def advDraw(self, size, listSize):
        graphSize = size - 100
        xSplit = graphSize/listSize

        StdDraw.setCanvasSize(size,size)
        StdDraw.setXscale(0,size)
        StdDraw.setYscale(0,size)

        StdDraw.line(50,50,50,size - 50)
        StdDraw.line(50,50,size - 50,50)

        StdDraw.line(45,size - 50,55,size - 50)
        StdDraw.line(48,3*graphSize/4+50,52,3*graphSize/4+50)
        StdDraw.line(45,graphSize/2+50,55,graphSize/2+50)
        StdDraw.line(48,graphSize/4+50,52,graphSize/4+50)

        for i in range(0,listSize):
            posX = 50 + xSplit * (i + 0.5)
            StdDraw.line(posX,48,posX,52)
            StdDraw.text(posX,25, str(i))

        StdDraw.line(size - 50,45,size - 50,55)
        StdDraw.show(0.0)

    #Calls the graph and then adds the data points
    def graphing(self, size, intList):
        listSize = len(intList)
        if size < 20 * listSize + 100:
            size = 20 * listSize + 100

        self.advDraw(size, listSize)

        graphSize = size - 100
        height = self.graphHeight(self.greatestInt(intList))
        width = graphSize/len(intList)

        if height >= 100:
            StdDraw.text(25,size - 50, str(height))
            StdDraw.text(25,3*graphSize/4+50, str(int(3*height/4)))
            StdDraw.text(25,graphSize/2+50, str(int(height/2)))
            StdDraw.text(25,graphSize/4+50, str(int(height/4)))
        else:
            StdDraw.text(25,size - 50, str(height))
            StdDraw.text(25,3*graphSize/4+50, str(3*height/4))
            StdDraw.text(25,graphSize/2+50, str(height/2))
            StdDraw.text(25,graphSize/4+50, str(height/4))
        StdDraw.text(25,50, "0")
        
        for i in range(0,len(intList)):
            StdDraw.setPenColor(StdDraw.BLUE)
            posX = 50 + width * i
            posY = intList[i] / height * graphSize + 75
            stretch = intList[i]/height * graphSize
            StdDraw.filledRectangle(posX,50,width,stretch)
            StdDraw.setPenColor(StdDraw.BLACK)
            StdDraw.rectangle(posX,50,width,stretch)
            StdDraw.text(posX + width/2,posY, str(intList[i]))
        graphTime = True
        while graphTime:
            StdDraw.show(10)
            if StdDraw.hasNextKeyTyped():
                graphTime = False


if __name__ == "__main__":
    digit = int(sys.argv[1])
    fName = sys.argv[2]
    size = int(sys.argv[3])
    #size = 600
    graph = Graph()
    ben = Benford.Benford()
    nums = ben.nthDigitTally(digit, ben.readMysteriousNumbers(fName))
    graph.graphing(size, nums)











        
        
