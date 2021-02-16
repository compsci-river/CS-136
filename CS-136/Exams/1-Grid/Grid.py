#
# Author: River Sheppard
#
# Description: Paint running down a grid, it is stopped if it runs into a color
#although it will try to go around it. It drips using a recursive method.
#

import color
import StdDraw
import sys

class Grid:

    # Constructor for the Grid class
    #
    # If it is instantiated with a file, the width and height should be
    #     sent in as 0's
    # Input parameters are integer width and height, or a string for a filename
    #     that contains initialization data
    def __init__(self, width=0, height=0, filename=""):
        if width != 0 and height != 0:
            self.width = width
            self.height = height
            self.colors = [[None for i in range(height)] for j in range(width)]
        elif filename != "":
            with open(filename, 'r') as f:
            # Read in the first line of text
                line = f.readline().split()
                # Translate that line to width and height
                self.width = int(line[0])
                self.height = int(line[1])
                self.colors = [[None for i in range(self.height)] for j in range(self.width)]
                # Read in the rest of the file and parse into color blocks
                line = f.read().split()
                for i in range(0, len(line), 5):
                    red = float(line[i+2])
                    green = float(line[i+3])
                    blue = float(line[i+4])
                    colr = color.Color(int(red*255), int(green*255), int(blue*255))
                    self.colors[int(line[i])][int(line[i+1])] = colr
                f.close()                             

    #Takes an x,y position and checks to see if it occurs on the grid
    #Inputs: x,y the position
    #Outputs: Boolean if it is on the grid
    def validPos(self,x,y):
        if x >= 0 and y >= 0 and x < self.getWidth() and y < self.getHeight():
            return True
        else:
            return False
    # Return the color at the specified (x, y) location.
    #
    # Input parameters are the integer x and y location in a grid
    #
    # Returns None if no color has been set at the given location.
    # Returns None if the (x, y) location is out of range.
    def getColor(self, x, y):
        if self.validPos(x,y):
            return self.colors[x][y]
        else:
            return None
            
    
    # Sets the color at the specified (x,y) location.
    #
    # Input parameters are the integer x and y location in a grid and
    #     c, a parameter of type color that specifies the color  the
    #     location is to be set to
    #
    # Does nothing if the (x, y) location is out of range.
    def setColor(self, x, y, c):
        if self.validPos(x,y):
            self.colors[x][y] = c

    # Return the width of the grid
    #
    # Returns an integer width
    def getWidth(self):
        return self.width
    
    # Return the height of the grid
    #
    # Returns an integer height
    def getHeight(self):
        return self.height
    
    # Return the number of the column (x-coordinate) that has the most colored grid locations.
    # In the event of a tie, returns the leftmost column with the maximum value.
    #
    # Uses two for loops to run through the columns and then check if there is a
    # color at each spot in the column, adds to the count if there is, and if the
    # count is greater than the maxCount it stores the new maxCount along with the
    # xPos it occured at
    #
    # Returns an integer value for the correct column
    def getMaxColumn(self):
        xPos = 0
        maxCount = 0
        for i in range(0,self.getWidth()):
            count = 0
            for j in range(0,self.getHeight()):
                if self.getColor(i,j) != None:
                    count += 1
            if count > maxCount:
                maxCount = count
                xPos = i
        return xPos
        
    # Recursive method to "drip" paint down the grid. Detailed instructions
    #  for how the drip should behave are on the printed exam sheet.
    #
    # Input parameters are the initial integer x and y location in the grid
    # to start the drip, and the parameter c or type color, which determines
    # the color assigned to the drip
    #
    #Checks if the spot it is in is empty if it is it will set the color to c
    #then it will check the spot below it if it is empty it will call drip with
    #those cordinates, if not it will try the spots on either side of the one
    #below it if they are empty it will call drip on those
    #
    # Returns no values
    def drip(self, x, y, c):
        if self.getColor(x,y) == None:
            self.setColor(x,y,c)
            if self.validPos(x,y-1) and self.getColor(x,y-1) == None:
                self.drip(x,y-1,c)
            else:
                if self.validPos(x-1,y-1) and self.getColor(x-1,y-1) == None:
                    self.drip(x-1,y-1,c)
                if self.validPos(x+1,y-1) and self.getColor(x+1,y-1) == None:
                    self.drip(x+1,y-1,c)
            
    
    # Draw the grid
    #
    # Has no input parameters or return values
    def draw(self):
        StdDraw.clear()
        StdDraw.show(1)

        # Draw the colored boxes of the grid
        for x in range(0, self.width):
            for y in range(0, self.height):
                if self.colors[x][y] != None:
                    StdDraw.setPenColor(self.colors[x][y])
                    StdDraw.filledRectangle(x / self.width, 
                                y / self.height, 
                                1 / self.width, 
                                1 / self.height)
            
        # Draw a grid on top of things
        StdDraw.setPenColor(StdDraw.BLACK)
        for x in range(0, self.width):
            StdDraw.rectangle(x / self.width, 0, self.width, 1)
        for y in range(0, self.height):
            StdDraw.rectangle(0, y / self.height, 1, self.height)
        StdDraw.show(1)

# Test code for the Grid class
#
# There are several sections of code, you can uncomment them one
#  at a time to test your code in parts.
#
# You will not be graded on code in this section, so if you wish to add
#    more tests, feel free.
if __name__ == "__main__":
##    # Test main code, part 1  
##    g = Grid(8, 8)
##    g.setColor(0, 0, StdDraw.RED)
##    g.setColor(7, 7, StdDraw.BLUE)
##    g.setColor(4, 2, StdDraw.GREEN)
##    g.setColor(4, 4, StdDraw.GREEN)
##    print("Grid size = " + str(g.getWidth()) + " x " + str(g.getHeight()))
##    print("Color @ (0,0) = " + str(g.getColor(0, 0)))
##    print("Color @ (1,1) = " + str(g.getColor(1, 1)))
##    print("Max column = " + str(g.getMaxColumn()))
##    g.draw()
##        
##    # Test main code, part 2
##    g = Grid(0, 0, "grid1.txt")
##    g.draw()
                    
##    # Test main code, part 3 
##    g = Grid(0, 0, "grid1.txt")
##    g.drip(8, 5, StdDraw.ORANGE)   # 3a  
##    g.drip(1, 6, StdDraw.ORANGE)   # 3b
##    g.drip(2, 10, StdDraw.ORANGE)  # 3c
##    g.drip(6, 8, StdDraw.ORANGE)   # 3d       
##    g.draw()
##    
    # Test main code, final
    g = Grid(0, 0, "grid1.txt")
    g.drip(11, 13, StdDraw.ORANGE)            
    g.drip(2, 13, StdDraw.GRAY)
    g.drip(1, 13, StdDraw.MAGENTA)
    g.drip(4, 13, StdDraw.CYAN)
    g.drip(5, 13, StdDraw.PINK)
    g.drip(5, 13, StdDraw.BLACK)
    g.draw()
    print("Max column = " + str(g.getMaxColumn()))
##pass
