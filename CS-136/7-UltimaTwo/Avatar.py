#
# Author: River Sheppard
#
# Description: Manages the player character, contains their data, a function to
# draw them and then some getters and setters
#
import StdDraw
from Tile import Tile
import picture

class Avatar :

    # Constructor for the avatar class
    #
    # Input parameters x and y are the initial integer positions of the
    #    avatar within the world
    def __init__(self, x, y, hp, damage, torch):
        self.x = x
        self.y = y
        self.hp = hp
        self.dmg = damage
        self.radi = torch
        self.timer = 500

        ##### YOUR CODE HERE #####
        pass

    # Mutator method to set the avatar to a new location
    #
    # Input parameters are the new integer x and y position
    def setLocation(self, x, y):
        self.x = x
        self.y = y

        ##### YOUR CODE HERE #####
        pass

    # Accessor method
    #
    # Returns the x position of the avatar
    def getX(self):

        #####YOUR CODE HERE #####
        return self.x
    
    # Accessor method
    #
    # Returns the y position of the avatar
    def getY(self):

        ##### YOUR CODE HERE #####
        return self.y
    
    # Accessor method
    #
    # Returns the current radius of the torch
    def getTorchRadius(self):

        ##### YOUR CODE HERE #####
        return self.radi

    #returns the number of hit points the player has remaining
    def getHitPoints(self):
        return self.hp

    #returns the amount of damage the player deals to monters
    def getDamage(self):
        return self.dmg

    #decreases the players hit points by the input amount of damage
    def incurDamage(self, damage):
        self.hp -= int(damage)
        if damage > 0:
            self.timer = 0

    # Make our torch more powerful
    #
    # Increases the radius of the torch
    def increaseTorch(self):
        self.radi += 0.5

        ##### YOUR CODE HERE #####
        pass
    
    # Make our torch less powerful
    #
    # Decreases the radius of the torch
    def decreaseTorch(self):
        if self.radi >= 2.5:
            self.radi -= 0.5

        #####YOUR CODE HERE #####
        pass

    # Draw the avatar
    #
    # Uses the avatar's current position to place and draw the avatar
    #    on the canvas
    def draw(self):
        p = picture.Picture("avatar.gif")
        x = (self.x+0.5)*Tile.SIZE
        y = (self.y+0.5)*Tile.SIZE
        StdDraw.picture(p,x,y)
        if self.timer < 100:
            StdDraw.text(x,y,str(self.hp))

        ##### YOUR CODE HERE #####
        pass

# Main code to test the avatar class    
if __name__ == "__main__":
    # Create an avatar at 5,5
    avatar = Avatar(5, 5, 10, 3, 4)
    print("%d %d %.1f" %(avatar.getX(), avatar.getY(), avatar.getTorchRadius()))
    # Change the avatar's position
    avatar.setLocation(1, 4)
    print("%d %d %.1f" %(avatar.getX(), avatar.getY(), avatar.getTorchRadius()))
    # Increase the torch radius
    avatar.increaseTorch()
    print("%d %d %.1f" %(avatar.getX(), avatar.getY(), avatar.getTorchRadius()))
    # Decrease the torch radius 6 times to make sure it doesn't go below 2.0
    for i in range(0, 6):
        avatar.decreaseTorch()
        print("%d %d %.1f" %(avatar.getX(), avatar.getY(), avatar.getTorchRadius()))
