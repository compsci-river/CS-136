#
# Defines the class for a position (in this case, in a 2D maze).
# DO NOT CHANGE THIS CODE
# 
# @author Michele Van Dyne
#
import color
import StdDraw

class Position:

    #
    # Constructor for the Position class
    # 
    # @param x the x position
    # @param y the y position
    #
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #
    # Accessor for the x position
    # 
    # @return the x position
    #
    def getX(self):
        return self.x

    #
    # Accessor for the y position
    # 
    # @return the y position
    #
    def getY(self):
        return self.y

    #
    # Draws the position as a circle
    # 
    # @param color the color that should be used to draw the position
    #
    def draw(self, col):
        StdDraw.setPenColor(col)
        StdDraw.filledCircle(self.x + 0.5, self.y + 0.5, 0.25)
        StdDraw.show(50)

    #
    # Checks to see if two positions are at the same location
    # 
    # @param p the position that "this" should be compared to
    # @return true if they are at the same location, false otherwise
    #
    def equals(self, p):
        if p.getX() == self.x and p.getY() == self.y:
            return True
        return False

    #
    # Method for converting a position to a String for printing
    # 
    # @return the String representation of the Position
    #
    def toString(self):
        return str(self.x) + ", " + str(self.y) + "\n"
