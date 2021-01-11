#
#River Sheppard
#Scattergories
#

import random

class Scattergories:
    def __init__(self):
        pass
    
    def letter(self):
        letters = []
        with open("Letters.txt", 'r') as f:
            line = f.readline().split()
            for a in line:
                letters.append(a)
        f.close()
        return letters[random.randint(0,len(letters)-1)]

    def readCattergories(self):
        cattergories = []
        with open("Cattergories.txt", 'r') as f:
            for line in f:
                cattergories.append(f.readline())
        f.close()
        return cattergories

    def cattergory(self, cList):
        cattergories = self.readCattergories()
        if len(cList) == 0:
            return cattergories[random.randint(0,len(cattergories)-1)]
        check = True
        c = ""
        while check:
            c = cattergories[random.randint(0,len(cattergories)-1)]
            count = 0
            for cat in cList:
                if c == cat:
                    count += 1
            if count == 0:
                check = False
        return c

    def printOut(self):
        cList = []
        l = self.letter()
        print("The cattergories are:\n")
        while len(cList) < 12:
            c = self.cattergory(cList)
            cList.append(c)
            print(str(len(cList))+": "+c + "\n")
        print("The letter is: " + l)
        


if __name__ == '__main__':
    scat = Scattergories()
    scat.printOut()
