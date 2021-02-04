import sys
import os
import StdDraw
from Point import Point

try:
    from Tour import Tour
except:
    print("Tour.py and/or the Tour constructor do not exist")

def getOutput(filename):
    distance = 0.0
    x = []
    y = []
    try:
        with open(filename, 'r') as f:
            lines = f.read().split()
            f.close()
        distance = float(lines[3])
        #print(len(lines))
        for i in range(4, len(lines), 2):
            str1 = lines[i]
            str2 = lines[i+1]
            str1 = str1[1:len(str1)-1]
            str2 = str2[0:len(str2)-1]
            #print(i, str1, str2)
            x.append(float(str1))
            y.append(float(str2))
    except:
        print("Output file does not exist")
    return distance, x, y

totalScore = 0.0

# Create an empty Tour object
score = 0.0
try:
    # define 4 points forming a square
    a = Point(100.0, 100.0)
    b = Point(500.0, 100.0)
    c = Point(500.0, 500.0)
    d = Point(100.0, 500.0)
    tour = Tour()       # Create an empty tour
    score += 2.0        # Compiles and runs
    score += 2.0        # __init__() works
    totalScore = score  
except:
    print("Tour class not implemented according to instructions")
finally:
    print("Score for program compilation and execution: " + str(score) + "/4.0")

# Test each method

# 1. insertInOrder()
score = 0.0
try:
    # first check to see if it is implemented
    tour.insertInOrder(a)
    score += 1
    # next insert three more points
    tour.insertInOrder(b)
    tour.insertInOrder(c)
    tour.insertInOrder(d)
except:
    print("insertInOrder not implemented according to API")
finally:
    print("Initial score for insertInOrder: " + str(score) + "/1.0")

totalScore += score
    
# 2. size()
score = 0.0
try:
    # first check to see if it is implemented
    result = tour.size()
    score += 1
    # next see if it gets correct results
    if result == 4:
        score += 1
except:
    print("size not implemented according to API")
finally:
    print("Score for size: " + str(score) + "/2.0")

totalScore += score
    
# 3. distance()
score = 0.0
try:
    # first check to see if it is implemented
    result = tour.distance()
    score += 1
    # next see if it gets correct results
    epsilon = 10E-5
    if abs(result - 1600) < epsilon:
        score += 1
except:
    print("distance not implemented according to API")
finally:
    print("Score for distance: " + str(score) + "/2.0")

totalScore += score
    
# 4. show()
score = 0.0
try:
    # first check to see if it is implemented
    tour.show()
    score += 2
    # next see if it gets correct results
except:
    print("show not implemented according to API")
finally:
    print("Score for show: " + str(score) + "/2.0")

totalScore += score
    
# 5. draw()
score = 0.0
try:
    # first check to see if it is implemented
    StdDraw.setCanvasSize(600,600)
    StdDraw.setXscale(0, 600)
    StdDraw.setYscale(0, 600)
    tour.draw()
    StdDraw.show(1000)
    score += 2
except:
    print("draw not implemented according to API")
finally:
    print("Score for draw: " + str(score) + "/2.0")
    print("NOTE: You should see a window with a square drawn in it.")
    print("      Points may be subtracted if this doesn't appear.")

totalScore += score
    
# 6. insertNearest()
score = 0.0
tour = Tour()
try:
    # first check to see if it is implemented
    tour.insertNearest(a)
    score += 1
    # next insert three more points
    tour.insertNearest(b)
    tour.insertNearest(c)
    tour.insertNearest(d)
except:
    print("insertNearest not implemented according to API")
finally:
    print("Initial score for insertNearest: " + str(score) + "/1.0")

totalScore += score
    
# 7. insertSmallest()
score = 0.0
tour = Tour()
try:
    # first check to see if it is implemented
    tour.insertSmallest(a)
    score += 1
    # next insert three more points
    tour.insertSmallest(b)
    tour.insertSmallest(c)
    tour.insertSmallest(d)
except:
    print("insertSmallest not implemented according to API")
finally:
    print("Initial score for insertSmallest: " + str(score) + "/1.0")

totalScore += score
    
# Now test all methods together using client programs
inOrderScore = 0.0
nearestScore = 0.0
smallestScore = 0.0
epsilon = 10E-5
try:
    # Insert in order
    result = os.system('py -m InOrderInsertion tsp100.txt > tsp100InOrder.out')
    if result == 0:
        distance, x, y = getOutput('tsp100InOrder.out')
        if (distance - 25547.32294) < epsilon:
            inOrderScore += 1.0
        if (x[len(x)-1] - 396.3891) < epsilon:
            inOrderScore += 1.0
        if (y[len(y)-1] - 185.0917) < epsilon:
            inOrderScore += 1.0
    print("Additional score for insertInOrder: " + str(inOrderScore) + "/3.0")

    # Insert nearest
    result = os.system('py -m NearestInsertion tsp100.txt > tsp100Nearest.out')
    if result == 0:
        distance, x, y = getOutput('tsp100Nearest.out')
        if (distance - 7389.929674) < epsilon:
            nearestScore += 1.0
        if (x[len(x)-1] - 371.5071) < epsilon:
            nearestScore += 1.0
        if (y[len(y)-1] - 590.0) < epsilon:
            nearestScore += 1.0
    print("Additional score for insertNearest: " + str(nearestScore) + "/3.0")

    #Insert smallest
    result = os.system('py -m SmallestInsertion tsp100.txt > tsp100Smallest.out')
    if result == 0:
        distance, x, y = getOutput('tsp100Smallest.out')
        if (distance - 25547.32294) < epsilon:
            smallestScore += 1.0
        if (x[len(x)-1] - 276.8106) < epsilon:
            smallestScore += 1.0
        if (y[len(y)-1] - 51.5341) < epsilon:
            smallestScore += 1.0
    print("Additional score for insertSmallest: " + str(smallestScore) + "/3.0")
except:
    print("Code fails on use of client")

totalScore += inOrderScore + nearestScore + smallestScore

print("Total Score: " + str(totalScore) + "/24.0")
print("Remember: This is not your final score. Your code will still be")
print("          checked for a proper header and comments on all methods,")
print("          in addition to a write up of results for test files")
print("          with different numbers of points.")
print("          The additional check accounts for the 6 remaining points.")
    




