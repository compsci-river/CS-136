#
#River Sheppard
#CSI 136
#Description: The program determines the frequency that each digit occurs in a specific
#location. It takes a file and reads a list of numbers from it, it also takes a target index
#and creates a list that counts the number of times each digit occurs in the given position
#and then it prints a formated display of the data
#Results:
#LibraryBooks.txt, [0, 3056, 1606, 1018, 801, 640, 560, 502, 503, 452]
#Is definitly similar to the Benford distribution, because it is a limited data set it is
#not a great match, but the data mostly follows the rule excepting 8s which which occur more
#often than 7s
#LiveJournal.txt, [0, 982, 276, 30, 38, 50, 91, 94, 121, 197]
#Doesn't really fit with the Benford rule, it decreases too much by the 2s and then it
#starts to grow at the end again which is a clear deviation from the rule.
#SunSpots.txt, [87, 868, 369, 307, 318, 305, 257, 193, 196, 173]
#Includes zero which is not allowed for by the rule although the rest of the data looks
#pretty good.
#

import sys

class Benford:
    #The constructor, doesn't hold anthing here, just used to construct the class
    def __init__(self):
        pass

#Counts the digits of a number that is passed in, uses a for loop that divides by ten
#each time until the result is less than one
#Inputs: int num, the number whose digits are being counted
#Return values: int count, the number of digits counted to be in num
    def countDigits(self, num):
        count = 1
        while int(num) >= 1:
            num = num / 10
            if num >= 1:
                count += 1
        return count

#Finds the value of the digit n spaces from the back, first it divides by 10 to the power of
#the position it is looking for and then uses an int cast to truncate it. Then it uses the
#modulus(%)operator and devides by ten because then the last digit is the returned remainder
#Inputs: int n, the position from the back of the target digit. int num, the number that
#the digit is being found in
#Return values: int digitBack, the digit that was found in the target position of num
    def nthDigitBack(self, n, num):
        reducedNum = int(num/pow(10,n))
        digitBack = reducedNum%10
        return digitBack

#Finds the value of the digit n spaces from the front, first it checks to make sure that the
#number is long enough to contain the digit, then it flips n so that it is the distance from
#the back, and then calls nthDigitBack using the new targetN
#Inputs: int n, the position from the front of the target digit. int num, the number that
#the digit is being found in
#Return values: int digitBack, the digit that was found in the target position of num
    def nthDigit(self, n, num):
        if n > self.countDigits(num)-1:
            return -1
        count = self.countDigits(num)
        targetN = count - 1 - n
        digitBack = self.nthDigitBack(targetN, num)
        return digitBack

#First it uses nth digit to find the digit in the nth position of num and then it adds one to
#that index in the array.
#Inputs: int n, the position from the front of the target digit. int num, the number that
#the digit is being found in. int [] tally, the array where the count is added to
#Return values: int [] tally, the updated array where the count is added to
    def nthDigitTally1(self, n, num, tally):
        d = self.nthDigit(n, num)
        if d == -1:
            return tally
        tally[d] += 1
        return tally

#Creates an empty int list ten long, and then loops through a list of ints using
#nthDigitTally1 to count the number of times each number occurs in position n, and then
#saving the count to the new list
#Inputs: int n, the position of the target digit. int [] nums, the list of number which is
#being checked
#Return values: int [] tally, the total count of the digits in position n of the list of
#numbers
    def nthDigitTally(self, n, nums):
        tally = [0,0,0,0,0,0,0,0,0,0]
        for num in nums:
            tally = self.nthDigitTally1(n, num, tally)
        return tally

#Reads through a file adding the numbers to a list, the first number is the amount of other
#numbers in the file and then it loops that many times adding the number to a list.
#Inputs: string fName, the name of the file to read.
#Return values: int [] nums, the list of numbers created from the file
    def readMysteriousNumbers(self, fName):
        nums = []
        with open(fName, 'r') as f:
            count = int(f.readline())
            for i in range(0,count):
                nums.append(int(f.readline()))
        return nums

#Runs nthDigitTally based on the system arguments and then prints the tally out in a
#formatted method
if __name__ == '__main__':
    ben = Benford()
    nums = ben.nthDigitTally(int(sys.argv[1]), ben.readMysteriousNumbers(sys.argv[2]))
    for i in range(0,len(nums)):
        print(str(i) + "s: " + str(nums[i]))

