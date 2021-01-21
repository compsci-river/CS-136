#
#River Sheppard
#Lab 3: Maze
#

import sys
import StdDraw
from Maze import Maze
from Position import Position
from StackOfPositions import StackOfPositions
from QueueOfPositions import QueueOfPositions

class Solve:
    def __init__(self, n):
        self.size = n
        self.maze = Maze(n)

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

    def stackClear(self, start, finish, stack):
        while not stack.isEmpty():
            currentPos = stack.pop()
            if (not currentPos.equals(finish) and not currentPos.equals(start)):
                currentPos.draw(StdDraw.BOOK_LIGHT_BLUE)

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

    def queueClear(self, start, finish, queue):
        while not queue.isEmpty():
            currentPos = queue.dequeue()
            if (not currentPos.equals(finish) and not currentPos.equals(start)):
                currentPos.draw(StdDraw.LIGHT_GRAY)

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
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
    else:
        size = 12
    solve = Solve(size)
    solve.maze.draw()
    stackSteps = solve.stackSolve()
    print("It took " + str(stackSteps) + " steps for the stack to reach the finish")
    queueSteps = solve.queueSolve()
    print("It took " + str(queueSteps) + " steps for the queue to reach the finish")

