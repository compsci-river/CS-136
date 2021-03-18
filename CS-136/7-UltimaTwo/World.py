#
# Author: River Sheppard
#
# Description: Controls the ultima world, reads it in from a file and then
# manages the player and monsters. Allows the player to interact with the world.
#

from Tile import Tile
from Avatar import Avatar
from Monster import Monster
import math
import sys
import StdDraw
import threading

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
            self.avatar = Avatar(int(l[0]),int(l[1]),int(l[2]),int(l[3]),float(l[4]))
            self.tiles = [[None for i in range(self.height)] for j in range(self.width)]
            for i in range(self.height-1,-1,-1):
                l = f.readline().split()
                for j in range(0,self.width):
                    self.tiles[j][i] = Tile(l[j])
                    #print(self.tiles[j][i].name)
            self.mons = []
            for line in f:
                l = line.split()
                if len(l) == 6:
                    m = Monster(self,l[0],int(l[1]),int(l[2]),int(l[3]),int(l[4]),int(l[5]))
                    t = threading.Thread(target=m.run)
                    self.mons.append(m)
                    t.start()
        f.close()
        self.lock = threading.Lock()
        StdDraw.setCanvasSize(self.width * Tile.SIZE, self.height * Tile.SIZE)
        StdDraw.setXscale(0.0, self.width * Tile.SIZE)
        StdDraw.setYscale(0.0, self.height * Tile.SIZE)
        StdDraw.setFontSize(12)
        StdDraw.setPenColor(StdDraw.RED)


    #Checks to see if the entered x,y position exists on the grid of tiles
    #Returns true if it does false if not
    def validPos(self,x,y):
        if x>=0 and x<=self.width-1 and y>=0 and y<=self.height-1:
            return True
        else:
            return False

    # Accept keyboard input and performs the appropriate action
    # 
    # Input parameter is a character that indicates the action to be taken
    def handleKey(self, ch):
        x = self.avatar.getX()
        y = self.avatar.getY()
        if ch == "w":
            self.avatarMove(x,y+1)
        elif ch == "s":
            self.avatarMove(x,y-1)
        elif ch == "a":
            self.avatarMove(x-1,y)
        elif ch == "d":
            self.avatarMove(x+1,y)
        elif ch == "+":
            self.avatar.increaseTorch()
        elif ch == "-":
            if self.avatar.getTorchRadius() >= 2.5:
                self.avatar.decreaseTorch()
        
                    

        ##### YOUR CODE HERE ####
        pass
    
    # Draw all the lit tiles
    #
    # Only action is to draw all the components associated with the world
    def draw(self):
        self.avatar.timer += 10
        self.setLit(False)
        x = self.light(self.avatar.getX(),self.avatar.getY(),self.avatar.getTorchRadius())
        for i in range(0,self.width):
            for j in range(0,self.height):
                self.tiles[i][j].draw(i,j)
        self.avatar.draw()
        for m in self.mons:
            m.draw()
    
    # Light the world
    #
    # Input parameters are the x and y position of the avatar and the
    #    current radius of the torch.
    #    Calls the recursive lightDFS method to continue the lighting
    # Returns the total number of tiles lit
    def light(self, x, y, r):
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

    def avatarAlive(self):
        if self.avatar.getHitPoints() > 0:
            return True
        return False

    def monsterMove(self,x,y,monster):
        if self.validPos(x,y):
            if self.tiles[x][y].isPassable():
                check = False
                for m in self.mons:
                    if m.getX() == x and m.getY() == y:
                        check = True
                if not check:
                    if self.avatar.getX() == x and self.avatar.getY() == y:
                        self.avatar.incurDamage(monster.dmg)
                    else:
                        monster.setLocation(x,y)
                        monster.incurDamage(self.tiles[x][y].getDamage())

    #Gets input from handleKey to what would happen if the player moved to that
    #and then applies those effects
    def avatarMove(self,x,y):
        if self.validPos(x,y):
            if self.tiles[x][y].isPassable():
                check = False
                for m in self.mons:
                    if m.getX() == x and m.getY() == y:
                        check = True
                        m.incurDamage(self.avatar.dmg)
                if not check:
                    self.avatar.setLocation(x,y)
                    self.avatar.incurDamage(self.tiles[x][y].getDamage())

    #Gets the number of monsters remaining and returns it as an int
    def getNumMonsters(self):
        c = 0
        for m in self.mons:
            if m.getHitPoints() > 0:
                c += 1
            else:
                self.mons.remove(m)
        return c
                
            
    
# Main code to test the world class
if __name__ == "__main__":
    n = "10x10_full.txt"
    if len(sys.argv) > 1:
        n = sys.argv[1]
    world0 = World(n)
    world0.draw()
    #print(world0.light(3,4,10))
    #world0.draw()
    StdDraw.show()
