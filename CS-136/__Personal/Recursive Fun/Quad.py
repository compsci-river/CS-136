#
#River Sheppard
#
#

import math
import StdDraw

import LineUtils as u

class Quad:
    def __init__(self,pList):
        self.pOne = pList[0]
        self.pTwo = pList[1]
        self.pThree = pList[2]
        self.pFour = pList[3]

    def lines(self):
        lOne = u.Line(pOne,pTwo)
        lFive = u.Line(pOne,pFour)
        lFour = u.Line(pFour,pThree)
        lEight = u.Line(pTwo,pThree)
        lTwo = u.Line(lFive.getPoint(1/3),lEight.getPoint(1/3))
        lThree = u.Line(lFive.getPoint(2/3),lEight.getPoint(2/3))
        lSix = u.Line(lOne.getPoint(1/3),lFour.getPoint(1/3))
        lSeven = u.Line(lOne.getPoint(2/3),lFour.getPoint(2/3))
        lineList = [lOne,
                    lTwo,
                    lThree,
                    lFour,
                    lFive,
                    lSix,
                    lSeven,
                    lEight]
        return lineList

    def split(self):
        ls = self.lines
        ps = [self.pOne,
              ls[1].getStart(),
              ls[2].getStart(),
              self.pFour,
              ls[5].getStart(),
              ls[1].getPoint(1/3),
              ls[2].getPoint(1/3),
              ls[5].getEnd(),
              ls[6].getStart(),
              ls[1].getPoint(2/3),
              ls[2].getPoint(2/3),
              ls[6].getEnd(),
              self.pTwo,
              ls[1].getEnd(),
              ls[2].getEnd(),
              self.pThree]
        

class wild:
    def __init__(self):
        pass

    def hole(self,x,y):
        pass

    def cut(self,n,square):
        pass
