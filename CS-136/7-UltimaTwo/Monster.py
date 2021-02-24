# 
# Author: River Sheppard
# 
# Description:
#

from enum import Enum, auto
import time
import StdDraw
import picture
import random
from Tile import Tile

class MonsterType(Enum):
    INVALID = auto()
    SKELETON = auto()
    ORC = auto()
    BAT = auto()
    SLIME = auto()

class Monster:

    # Construct a new monster
    # 
    # param world	- the world the monster moves about in
    # param code	- the string code that distinguishes types of monsters
    # param x		- the x position of the monster
    # param y		- the y position of the monster
    # param hp		- hit points - damage sustained by the monster
    # param damage	- damage the monster causes
    # param sleepMs	- delay between time monster moves
    def __init__(self, world, code, x, y, hp, damage, sleepMs):
        self.world = world
        self.c = code
        self.x = x
        self.y = y
        self.hp = hp
        self.dmg = damage
        self.sleep = sleepMs
        l = self.codeC(self.c)
        self.name = l[0]
        self.timer = 5

        ##### YOUR CODE HERE #####
        pass

    #Gets the monster file name based on the input code
    def codeC(self,c):
        l = [None]
        if c == "SK":
            l = ["skeleton.gif"]
        elif c == "OR":
            l = ["orc.gif"]
        elif c == "SL":
            l = ["slime.gif"]
        elif c == "BA":
            l = ["bat.gif"]
        return l

    # The avatar has attacked a monster!
    #
    # param points	- number of hit points to be subtracted from monster
    def incurDamage(self, points):
        self.hp -= int(points)
        if points > 0:
            self.timer = 0

        ##### YOUR CODE HERE #####
        pass

    #
    # Draw this monster at its current location
    def draw(self):
        p = picture.Picture(self.name)
        x = (self.x+0.5)*Tile.SIZE
        y = (self.y+0.5)*Tile.SIZE
        StdDraw.picture(p,x,y)
        if self.timer < 3:
            StdDraw.text(x,y,str(self.hp))

        ##### YOUR CODE HERE #####
        pass

    #
    # Get the number of hit points the monster has ramaining
    # 
    # return the number of hit points
    def getHitPoints(self):

        ##### YOUR CODE HERE #####
        return self.hp

    #
    # Get the amount of damage a monster causes
    # 
    # return amount of damage monster causes
    def getDamage(self):

        ##### YOUR CODE HERE #####
        return self.dmg

    #
    # Get the x position of the monster
    # 
    # return x position
    def getX(self):

        ##### YOUR CODE HERE #####
        return self.x

    #
    # Get the y position of the monster
    # 
    # return y position
    def getY(self):

        ##### YOUR CODE HERE #####
        return self.y

    #
    # Set the new location of the monster
    # 
    # param x the new x location
    # param y the new y location
    def setLocation(self, x, y):
        self.x = x
        self.y = y

        ##### YOUR CODE HERE #####
        pass

    #
    # Thread that moves the monster around periodically
    def run(self):
        while self.hp > 0:
            di = random.randint(1,4)
            x = self.x
            y = self.y
            if di == 1:
                y += 1
            elif di == 2:
                x += 1
            elif di == 3:
                y -= 1
            elif di == 4:
                x -= 1
            self.world.monsterMove(x,y,self)
            self.timer += 1
            time.sleep(self.sleep)

        ##### YOUR CODE HERE #####
        pass
