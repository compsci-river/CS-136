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

    #Finds the number with which so scal the y-axis
    def graphHeight(self, num):
        intLen = self.intLength(num)
        height = 5 * pow(10,intLen-1)
        if num > height:
            height = pow(10,intLen)
        return height

    #Draws the blank graph before any data in used
    def graphDraw(self):
        StdDraw.setCanvasSize(600,600)
        StdDraw.setXscale(0,600)
        StdDraw.setYscale(0,600)

        StdDraw.line(50,50,50,550)
        StdDraw.line(50,50,550,50)
        StdDraw.text(25,50, "0")
        
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

    #Calls the graph and then adds the data points
    def graphing(self, intList):
        self.graphDraw()

        height = self.graphHeight(self.greatestInt(intList))

        if height >= 100:
            StdDraw.text(25,550, str(height))
            StdDraw.text(25,425, str(int(3*height/4)))
            StdDraw.text(25,300, str(int(height/2)))
            StdDraw.text(25,175, str(int(height/4)))
        else:
            StdDraw.text(25,550, str(height))
            StdDraw.text(25,425, str(3*height/4))
            StdDraw.text(25,300, str(height/2))
            StdDraw.text(25,175, str(height/4)) 
        
        for i in range(0,len(intList)):
            StdDraw.setPenColor(StdDraw.BLUE)
            posX = 50 * (i + 1)
            posY = intList[i] / height * 500 + 75
            stretch = intList[i]/height * 500
            StdDraw.filledRectangle(posX,50,50,stretch)
            StdDraw.setPenColor(StdDraw.BLACK)
            StdDraw.rectangle(posX,50,50,stretch)
            StdDraw.text(posX + 25,posY, str(intList[i]))
        StdDraw.show(0.0)



if __name__ == "__main__":
    graph = Graph()
    ben = Benford.Benford()
    nums = ben.nthDigitTally(int(sys.argv[1]), ben.readMysteriousNumbers(sys.argv[2]))
    graph.graphing(nums)











        
        
