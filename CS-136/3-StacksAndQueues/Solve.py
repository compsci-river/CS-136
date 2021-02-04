#
#River Sheppard
#Lab 3: Maze
#Description: Creates two ways to run through a maze based on the stack and
#queue data structures, it adds all the valid points to the active data
#structure and then advances to the next one offered by the data structure the\
#methods diverge by the order that the data stuctures offer new points

import sys
import StdDraw
from Maze import Maze
from Position import Position
from StackOfPositions import StackOfPositions
from QueueOfPositions import QueueOfPositions

class Solve:
    #Constructor
    def __init__(self, n):
        self.size = n
        self.maze = Maze(n)

    #Checks the points around the current one, adds the valid ones to the stack.
    #Checks in each direction, if there is not a wall and it has not been
    #visited yet it gets pushed onto the stack
    #Inputs: Position currentPos, the position to check arround.
    #StackOfPositions stack, the stack where new positions are stored.
    #Outputs:StackOfPositions stack, the stack where new positions are stored.
    def pushPos(self, currentPos, stack):
        start = self.maze.getStart()
        finish = self.maze.getFinish()
        if self.maze.openNorth(currentPos):
            testPos = Position(currentPos.getX(), currentPos.getY()+1)
            if not self.maze.isVisited(testPos):
                stack.push(testPos)
                if (not testPos.equals(finish)) and (not testPos.equals(start)):
                    testPos.draw(StdDraw.RED)

        if self.maze.openSouth(currentPos):
            testPos = Position(currentPos.getX(), currentPos.getY()-1)
            if not self.maze.isVisited(testPos):
                stack.push(testPos)
                if (not testPos.equals(finish)) and (not testPos.equals(start)):
                    testPos.draw(StdDraw.RED)

        if self.maze.openEast(currentPos):
            testPos = Position(currentPos.getX()+1, currentPos.getY())
            if not self.maze.isVisited(testPos):
                stack.push(testPos)
                if (not testPos.equals(finish)) and (not testPos.equals(start)):
                    testPos.draw(StdDraw.RED)

        if self.maze.openWest(currentPos):
            testPos = Position(currentPos.getX()-1, currentPos.getY())
            if not self.maze.isVisited(testPos):
                stack.push(testPos)
                if (not testPos.equals(finish)) and (not testPos.equals(start)):
                    testPos.draw(StdDraw.RED)

        return stack

    #Empties the stack and changes the color to used. loops through the stack
    #until empty, popping off the positions
    #Inputs: Position start, the start position of the maze. Position finish,
    #the finish position of the maze. StackOfPositions stack, the stack of
    #positions.
    #Outputs: null
    def stackClear(self, start, finish, stack):
        while not stack.isEmpty():
            currentPos = stack.pop()
            if (not currentPos.equals(finish) and not currentPos.equals(start)):
                currentPos.draw(StdDraw.BOOK_LIGHT_BLUE)

    #Loops through the stack until current position equals the finish. Pops the
    #stack to get the current position and then adds valid points using pushPos
    #Uses the stack data structure with pop to determine the order in which to
    #loop through the stack
    #Inputs: null
    #Outputs: Int steps, the number of loops it runs through to reach the end
    def stackSolve(self):
        stack = StackOfPositions()
        start = self.maze.getStart()
        finish = self.maze.getFinish()
        currentPos = start
        stack.push(currentPos)
        steps = 0
        while not currentPos.equals(finish):
            currentPos = stack.pop()
            if not currentPos.equals(finish):
                if not currentPos.equals(start):
                    currentPos.draw(StdDraw.BOOK_LIGHT_BLUE)
                self.maze.setVisited(currentPos)
                stack = self.pushPos(currentPos, stack)
            steps += 1
        self.maze.clear()
        self.stackClear(start, finish, stack)
        return steps

    #Checks the points around the current one, adds the valid ones to the queue.
    #Checks in each direction, if there is not a wall and it has not been
    #visited yet it gets enqueued into the queue
    #Inputs: Position currentPos, the position to check arround.
    #QueueOfPositions queue, the queue where new positions are stored.
    #Outputs:QueueOfPositions queue, the queue where new positions are stored.
    def enqueuePos(self, currentPos, queue):
        start = self.maze.getStart()
        finish = self.maze.getFinish()
        
        if self.maze.openNorth(currentPos):
            testPos = Position(currentPos.getX(), currentPos.getY()+1)
            if not self.maze.isVisited(testPos):
                queue.enqueue(testPos)
                if (not testPos.equals(finish)) and (not testPos.equals(start)):
                    testPos.draw(StdDraw.DARK_RED)

        if self.maze.openSouth(currentPos):
            testPos = Position(currentPos.getX(), currentPos.getY()-1)
            if not self.maze.isVisited(testPos):
                queue.enqueue(testPos)
                if (not testPos.equals(finish)) and (not testPos.equals(start)):
                    testPos.draw(StdDraw.DARK_RED)

        if self.maze.openEast(currentPos):
            testPos = Position(currentPos.getX()+1, currentPos.getY())
            if not self.maze.isVisited(testPos):
                queue.enqueue(testPos)
                if (not testPos.equals(finish)) and (not testPos.equals(start)):
                    testPos.draw(StdDraw.DARK_RED)

        if self.maze.openWest(currentPos):
            testPos = Position(currentPos.getX()-1, currentPos.getY())
            if not self.maze.isVisited(testPos):
                queue.enqueue(testPos)
                if (not testPos.equals(finish)) and (not testPos.equals(start)):
                    testPos.draw(StdDraw.DARK_RED)
        return queue

    #Empties the queue and changes the color to used. loops through the stack
    #until empty, popping off the positions
    #Inputs: Position start, the start position of the maze. Position finish,
    #the finish position of the maze. QueueOfPositions queue, the queue of
    #positions.
    #Outputs: null
    def queueClear(self, start, finish, queue):
        while not queue.isEmpty():
            currentPos = queue.dequeue()
            if (not currentPos.equals(finish) and not currentPos.equals(start)):
                currentPos.draw(StdDraw.LIGHT_GRAY)

    #Loops through the queue until current position equals the finish. dequeues
    #the stack to get the current position and then adds valid points using
    #pushPos(). Uses the stack data structure with pop to determine the order in
    #which to loop through the stack
    #Inputs: null
    #Outputs: Int steps, the number of loops it runs through to reach the end
    def queueSolve(self):
        queue = QueueOfPositions()
        start = self.maze.getStart()
        finish = self.maze.getFinish()
        currentPos = start
        queue.enqueue(currentPos)
        steps = 0
        
        while not currentPos.equals(finish):
            currentPos = queue.dequeue()
            if not currentPos.equals(finish):
                if not currentPos.equals(start):
                    currentPos.draw(StdDraw.LIGHT_GRAY)
                self.maze.setVisited(currentPos)
                queue = self.enqueuePos(currentPos, queue)
            steps += 1
        self.maze.clear()
        self.queueClear(start, finish, queue)
        return steps
        

if __name__ == "__main__":
    #Checks to see if a system arguement was given for the size
    size = 12
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
    #Creates and draws a maze
    solve = Solve(size)
    solve.maze.draw()
    #Runs both methods for solving the maze
    stackSteps = solve.stackSolve()
    print("It took " + str(stackSteps) + " steps for the stack to reach the finish")
    queueSteps = solve.queueSolve()
    print("It took " + str(queueSteps) + " steps for the queue to reach the finish")

