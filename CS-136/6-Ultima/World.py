#
# Author: 
#
# Description:
#

from Tile import Tile
from Avatar import Avatar
import math
import sys
import StdDraw

class World:

    # Constructor for the world
    #
    # Input parameter is a file name holding the configuration information
    #    for the world to be created
    #    The constructor reads in file data, stores it in appropriate
    #    attributes and sets up the window within which to draw.
    #    It also initializes the lighting in the world.
    def __init__(self, filename):
        with open(filename,'r') as f:
            l = f.readline().split()
            self.width = int(l[0])
            self.height = int(l[1])
            l = f.readline().split()
            self.player = Avatar(int(l[0]),int(l[1]))
            self.tiles = [[None for i in range(self.height)] for j in range(self.width)]
            for i in range(self.height-1,-1,-1):
                l = f.readline().split()
                for j in range(0,self.width):
                    self.tiles[j][i] = Tile(l[j])
                    #print(self.tiles[j][i].name)
        f.close()
        StdDraw.setCanvasSize(self.width * 16, self.height * 16)
        StdDraw.setXscale(0.0, self.width * 16)
        StdDraw.setYscale(0.0, self.height * 16)

        ##### YOUR CODE HERE #####
        pass

    def validPos(self,x,y):
        if x>=0 and x<=self.width-1 and y>=0 and y<=self.height-1:
            return True
        else:
            return False

    # Accept keyboard input and performs the appropriate action
    # 
    # Input parameter is a character that indicates the action to be taken
    def handleKey(self, ch):
        x = self.player.getX()
        y = self.player.getY()
        if ch == "w":
            if self.validPos(x,y+1):
                if self.tiles[x][y+1].isPassable():
                    self.player.setLocation(x,y+1)
        elif ch == "s":
            if self.validPos(x,y-1):
                if self.tiles[x][y-1].isPassable():
                    self.player.setLocation(x,y-1)
        elif ch == "a":
            if self.validPos(x-1,y):
                if self.tiles[x-1][y].isPassable():
                    self.player.setLocation(x-1,y)
        elif ch == "d":
            if self.validPos(x+1,y):
                if self.tiles[x+1][y].isPassable():
                    self.player.setLocation(x+1,y)
        elif ch == "+":
            self.player.increaseTorch()
        elif ch == "-":
            if self.player.getTorchRadius() >= 2.5:
                self.player.decreaseTorch()
        
                    

        ##### YOUR CODE HERE ####
        pass
    
    # Draw all the lit tiles
    #
    # Only action is to draw all the components associated with the world
    def draw(self):
        self.setLit(False)
        x = self.light(self.player.getX(),self.player.getY(),self.player.getTorchRadius())
        for i in range(0,self.width):
            for j in range(0,self.height):
                self.tiles[i][j].draw(i,j)
        self.player.draw()

        ##### YOUR CODE HERE #####
        pass
    
    # Light the world
    #
    # Input parameters are the x and y position of the avatar and the
    #    current radius of the torch.
    #    Calls the recursive lightDFS method to continue the lighting
    # Returns the total number of tiles lit
    def light(self, x, y, r):

        ##### YOUR CODE HERE #####
        return self.lightDFS(x,y,x,y,r)

    def dist(self,x,y,xOne,yOne):
        xDist = (xOne - x)**2
        yDist = (yOne - y)**2
        return math.sqrt(xDist+yDist)
    
    # Recursively light from (x, y) limiting to radius r
    #
    # Input parameters are (x,y), the position of the avatar,
    #    (currX, currY), the position that we are currently looking
    #    to light, and r, the radius of the torch.
    # Returns the number of tiles lit
    def lightDFS(self, x, y, currentX, currentY, r):
        #print("hi")
        if not self.validPos(currentX,currentY):
            return 0
        elif self.dist(x,y,currentX,currentY) >= r:
            return 0
        elif self.tiles[currentX][currentY].getLit():
            return 0
        elif self.tiles[currentX][currentY].isOpaque():
            self.tiles[currentX][currentY].setLit(True)
            return 1
        else:
            #print("hello")
            self.tiles[currentX][currentY].setLit(True)
            c = 1
            c += self.lightDFS(x,y,currentX,currentY+1,r)
            c += self.lightDFS(x,y,currentX,currentY-1,r)
            c += self.lightDFS(x,y,currentX-1,currentY,r)
            c += self.lightDFS(x,y,currentX+1,currentY,r)
            return c
        

        ##### YOUR CODE HERE ####
        return 0
            
    # Turn all the lit values of the tiles to a given value. Used
    #    to reset lighting each time the avatar moves or the torch
    #    strength changes
    #
    # Input paramter is a boolean value, generally False, to turn off
    #    the light, but is flexible to turn the light on in some future
    #    version
    def setLit(self, value):
        for i in range(0,self.width):
            for j in range(0,self.height):
                self.tiles[i][j].setLit(value)

        ##### YOUR CODE HERE #####
        pass
    
# Main code to test the world class
if __name__ == "__main__":
    n = "30x20.txt"
    if len(sys.argv) > 1:
        n = sys.argv[1]
    world0 = World(n)
    world0.draw()
    #print(world0.light(3,4,10))
    #world0.draw()
    StdDraw.show()
