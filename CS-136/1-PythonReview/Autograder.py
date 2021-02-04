#
# Author: Michele Van Dyne
# Description: Tests the methods in the Benford class for Lab 1 and
#              provides a preliminary grade for the lab.
#

# Library imports
import sys
import os

# Initial test to make sure code exists
try:
    from Benford import Benford
except:
    print("Benford.py does not exist")
#finally:
#    print("Make sure your files and the class are named correctly")

# Function getOutput reads in a file to use as test data for the following
# test code
#
# @param filename    the string name of a file containing test data
# @return outputData a python list of the numeric data read from the file
#
def getOutput(filename):
    outputData = []
    try:
        with open(filename, 'r') as f:
            for i in range(0, 10):
                line = f.readline().split()
                outputData.append(int(line[1]))
            f.close()
        return outputData
    except:
        print("File does not exist")

# Create a Benford object
score = 0
totalScore = 0
try:
    ben = Benford()
    score += 2.0
    totalScore = score
except:
    print("Benford class not implemented according to instructions")

# Test each method

# 1. countDigits
score = 0
try:
    # first check to see if it is implemented
    result = ben.countDigits(123456)
    score += 1
    # next see if it gets the correct results on four tests
    if result == 6:
        score += 0.5
    result = ben.countDigits(0)
    if result == 1:
        score += 0.5
    result = ben.countDigits(999999)
    if result == 6:
        score += 0.5
    result = ben.countDigits(1234567890123456789012345678901234567890)
    if result == 40:
        score += 0.5
except:
    print("countDigits not implemented according to API")
finally:
    print("Score for countDigits: " + str(score) + "/3.0")

totalScore += score
    
# 2. nthDigitBack
score = 0
try:
    # first check to see if it is implemented
    result = ben.nthDigitBack(0, 123456)
    score += 1
    # next see if it gets correct results on four tests
    if result == 6:
        score += 0.5
    result = ben.nthDigitBack(5, 123456)
    if result == 1:
        score += 0.5
    result = ben.nthDigitBack(3, 123456)
    if result == 3:
        score += 0.5
    result = ben.nthDigitBack(0, 1234567890123456789012345678901234567890)
    if result == 0:
        score += 0.5
except:
    print("nthDigitBack not implemented according to API")
finally:
    print("Score for nthDigitBack: " + str(score) + "/3.0")

totalScore += score
    
# 3. nthDigit
score = 0
try:
    # first check to see if it is implemented
    result = ben.nthDigit(0, 123456)
    score += 1
    # next see if it gets correct results on four tests
    if result == 1:
        score += 0.5
    result = ben.nthDigit(5, 123456)
    if result == 6:
        score += 0.5
    result = ben.nthDigit(3, 1234567890123456789012345678901234567890)
    if result == 4:
        score += 0.5
    result = ben.nthDigit(0, 1234567890123456789012345678901234567890)
    if result == 1:
        score += 0.5
except:
    print("nthDigit not implemented according to API")
finally:
    print("Score for nthDigit: " + str(score) + "/3.0")

totalScore += score
    
# 4. nthDigitTally1
score = 0
try:
    tally = [0] * 10
    # first check to see if it is implemented
    tally = ben.nthDigitTally1(0, 123456, tally)
    score += 1
    # next see if it gets correct results on four tests
    if tally == [0, 1, 0, 0, 0, 0, 0, 0, 0 ,0]:
        score += 0.5
    tally = ben.nthDigitTally1(5, 123456, tally)
    if tally == [0, 1, 0, 0, 0, 0, 1, 0, 0 ,0]:
        score += 0.5
    tally = ben.nthDigitTally1(3, 1234567890123456789012345678901234567890, tally)
    if tally == [0, 1, 0, 0, 1, 0, 1, 0, 0 ,0]:
        score += 0.5
    tally = ben.nthDigitTally1(0, 1234567890123456789012345678901234567890, tally)
    if tally == [0, 2, 0, 0, 1, 0, 1, 0, 0 ,0]:
        score += 0.5
except:
    print("nthDigitTally1 not implemented according to API")
finally:
    print("Score for nthDigitTally1: " + str(score) + "/3.0")

totalScore += score
    
# 5. nthDigitTally
score = 0
nums = [123, 223, 323, 423, 523, 623456, 723, 823, 923]
try:
    # first check to see if it is implemented
    tally = ben.nthDigitTally(0, nums)
    score += 1
    # next see if it gets correct results on four tests
    if tally == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
        score += 0.5
    tally = ben.nthDigitTally(5, nums)
    if tally == [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]:
        score += 0.5
    tally = ben.nthDigitTally(1, nums)
    if tally == [0, 0, 9, 0, 0, 0, 0, 0, 0, 0]:
        score += 0.5
    tally = ben.nthDigitTally(10, nums)
    if tally == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
        score += 0.5
except:
    print("nthDigitTally not implemented according to API")
finally:
    print("Score for nthDigitTally: " + str(score) + "/3.0")

totalScore += score
    
# 6. readMysteriousNumbers
score = 0
try:
    # first check to see if it is implemented
    nums = ben.readMysteriousNumbers("TestData.txt")
    score += 1
    # next see if it gets correct results on four tests
    if len(nums) == 11:
        score += 0.5
    if nums == [12176, 5476, 543, 3490, 24892, 28619, 2595, 603, 2527, 1465, 1858]:
        score += 0.5
    nums = ben.readMysteriousNumbers("LibraryBooks.txt")
    if len(nums) == 9138:
        score += 0.5
    nums = ben.readMysteriousNumbers("SunSpots.txt")
    if len(nums) == 3073:
        score += 0.5
except:
    print("readMysteriousNumbers not implemented according to API")
finally:
    print("Score for readMysteriousNumbers: " + str(score) + "/3.0")

totalScore += score

# 7. test main and correct output on files
mainScore = 0
outputScore = 0
try:    
    result = os.system('py Benford.py 0 TestData.txt > TestData.out')
    if result == 0:
        mainScore += 2.0
    result = getOutput('TestData.out')
    if result == [0, 3, 4, 1, 0, 2, 1, 0, 0, 0]:
        outputScore += 0.5
    os.system('py Benford.py 0 LibraryBooks.txt > LibraryBooks.out')
    result = getOutput('LibraryBooks.out')
    if result == [0, 3056, 1606, 1018, 801, 640, 560, 502, 503, 452]:
        outputScore += 0.5
    os.system('py Benford.py 0 LiveJournal.txt > LiveJournal.out')
    result = getOutput('LiveJournal.out')
    if result == [0, 982, 276, 30, 38, 50, 91, 94, 121, 197]:
        outputScore += 0.5
    os.system('py Benford.py 0 SunSpots.txt > SunSpots.out')
    result = getOutput('SunSpots.out')
    if result == [87, 868, 369, 307, 318, 305, 257, 193, 196, 173]:
        outputScore += 0.5
except:
    print("Test main was not implemented correctly")
finally:
    print("Score for test main: " + str(mainScore) + "/2.0")
    print("Score for correct output: " + str(outputScore) + "/2.0")

totalScore += mainScore + outputScore

print("Total Score: " + str(totalScore) + "/24.0")
print("Remember: This is not your final score. Your code will still be")
print("          checked for a proper header and comments on all methods,")
print("          in addition to a write up of results for all test files.")
print("          The additional check accounts for the 6 remaining points.")
    




