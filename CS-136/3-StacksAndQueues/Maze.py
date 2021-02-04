#
#  Compilation:  javac Maze.java
#  Execution:    java Maze.java n
#  Dependencies: StdDraw.java
#
#  Generates a perfect n-by-n maze 
#  
#  Originally developed at Princeton
#  
#  @author Michele Van Dyne
#  
#  Modified to use Positions and cleaned up code a bit
#
#

import StdDraw
import random
from Position import Position

class Maze:

    def __init__(self, n):
        # dimension of maze
        self.n = n                            

        # is there a wall to north of cell i, j
        #    initialize as all walls are present
        self.north = [[True for i in range(n+2)] for j in range(n+2)]     
        self.east = [[True for i in range(n+2)] for j in range(n+2)]      
        self.south = [[True for i in range(n+2)] for j in range(n+2)]
        self.west = [[True for i in range(n+2)] for j in range(n+2)]

        # Start with all cells not visited
        # [[0 for i in range(cols)] for j in range(rows)]
        self.visited = [[False for i in range(n+2)] for j in range(n+2)]  # has a cell been visited
        # Mark all border cells as visited
        for i in range(0, n+2):
            self.visited[i][0] = True
            self.visited[i][n+1] = True
            self.visited[0][i] = True
            self.visited[n+1][i] = True

        StdDraw.setXscale(0, n+2)
        StdDraw.setYscale(0, n+2)
        # The position of where the maze starts
        self.start = Position(random.randint(1,n), random.randint(1, n))
        # The goal position
        self.finish = Position(random.randint(1,n), random.randint(1, n))
        
        self.generate(1, 1)
        self.clear()


    #
    # Starts with a totally walled off maze and randomly chooses walls to remove
    # such that there will be a path from start to finish. The function calls
    # itself recursively.
    # 
    # @param x the x position we are currently investigating
    # @param y the y position we are currently investigating
    #
    def generate(self, x, y):
        self.visited[x][y] = True

        # while there is an unvisited neighbor
        while (not self.visited[x][y+1]) or (not self.visited[x+1][y]) or (not self.visited[x][y-1]) or (not self.visited[x-1][y]):
            another = True
            while another:
                # pick random neighbor 
                r = random.randint(0,3)
                
                # if that node has not been investigated before, remove some walls
                #   and call itself using the appropriate neighbor
                if r == 0 and not self.visited[x][y+1]:
                    self.north[x][y] = False
                    self.south[x][y+1] = False
                    self.generate(x, y + 1)
                    another = False
                elif r == 1 and not self.visited[x+1][y]:
                    self.east[x][y] = False
                    self.west[x+1][y] = False
                    self.generate(x+1, y)
                    another = False
                elif r == 2 and not self.visited[x][y-1]:
                    self.south[x][y] = False
                    self.north[x][y-1] = False
                    self.generate(x, y-1)
                    another = False
                elif r == 3 and not self.visited[x-1][y]:
                    self.west[x][y] = False
                    self.east[x-1][y] = False
                    self.generate(x-1, y)
                    another = False

    #
    # Draw the maze.
    #
    def draw(self):
        self.start.draw(StdDraw.BLUE)
        self.finish.draw(StdDraw.BLACK)

        StdDraw.setPenColor(StdDraw.BLACK)
        for x in range(1,self.n+1):
            for y in range(1, self.n+1):
                if self.south[x][y]:
                    StdDraw.line(x, y, x+1, y)
                if self.north[x][y]:
                    StdDraw.line(x, y+1, x+1, y+1)
                if self.west[x][y]:
                    StdDraw.line(x, y, x, y+1)
                if self.east[x][y]:
                    StdDraw.line(x+1, y, x+1, y+1)
        StdDraw.show(5000)
    
    #
    # Accessor for the start Position
    # 
    # @return the start Position
    #
    def getStart(self):
    	return self.start
    
    #
    # Accessor for the finish Position
    # 
    # @return the finish Position
    #
    def getFinish(self):
    	return self.finish
    
    #
    # Check to see if there is no wall to the north
    # 
    # @param p the Position we are currently looking at
    # @return true if there is no wall to the north, false otherwise
    #
    def openNorth(self, p):
    	return not self.north[p.getX()][p.getY()]

    #
    # Check to see if there is no wall to the south
    # 
    # @param p the Position we are currently looking at
    # @return true if there is no wall to the south, false otherwise
    #
    def openSouth(self, p):
    	return not self.south[p.getX()][p.getY()]

    #
    # Check to see if there is no wall to the east
    # 
    # @param p the Position we are currently looking at
    # @return true if there is no wall to the east, false otherwise
    #
    def openEast(self, p):
    	return not self.east[p.getX()][p.getY()]

    #
    # Check to see if there is no wall to the west
    # 
    # @param p the Position we are currently looking at
    # @return true if there is no wall to the west, false otherwise
    #
    def openWest(self, p):
    	return not self.west[p.getX()][p.getY()]
    
    #
    # Check to see if a Position has been visited before so we don't visit 
    # it againg
    # 
    # @param p the Position we are currently looking at
    # @return true if we've been here before, false otherwise
    #
    def isVisited(self, p):
    	return self.visited[p.getX()][p.getY()]

    #
    # Sets a flag in a maze position once we have been there
    # 
    # @param p the Position we are currently at
    #
    def setVisited(self, p):
    	self.visited[p.getX()][p.getY()] = True
    
    #
    # Clear the maze from any visited markings so that we can try a
    # different solution
    #/
    def clear(self):
        for x in range(1, self.n+1):
            for y in range(1, self.n+1):
                self.visited[x][y] = False
        #self.start.draw(StdDraw.RED)
        #self.finish.draw(StdDraw.RED)

#
# A test main method so that we can make sure the maze is generating
# properly.
# 
# @param args the length of the sides of the maze
#
if __name__ == "__main__":
    import sys

    n = int(sys.argv[1])
    maze = Maze(n)
    maze.draw()
