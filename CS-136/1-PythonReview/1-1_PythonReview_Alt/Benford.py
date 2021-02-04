#
#River Sheppard
#CSI 136
#Description:
#

import sys

class Benford:
    def __init__(self):
        pass

    def countDigits(self, num):
        count = 1
        while num >= 1:
            num = num / 10
            if num >= 1:
                count += 1
        return count

    def nthDigitBack(self, n, num):
        if n > self.countDigits(num)-1:
            return -1
        strNum = str(num)
        char = strNum[-n - 1]
        digitBack = int(char)
        return digitBack

    def nthDigit(self, n, num):
        if n > self.countDigits(num)-1:
            return -1
        strNum = str(num)
        char = strNum[n]
        digitBack = int(char)
        return digitBack

    def nthDigitTally1(self, n, num, tally):
        d = self.nthDigit(n, num)
        if d == -1:
            return tally
        tally[d] += 1
        return tally

    def nthDigitTally(self, n, nums):
        tally = [0,0,0,0,0,0,0,0,0,0]
        for num in nums:
            tally = self.nthDigitTally1(n, num, tally)
        return tally

    def readMysteriousNumbers(self, fName):
        nums = []
        with open(fName, 'r') as f:
            count = int(f.readline())
            for i in range(0,count):
                nums.append(int(f.readline()))
        return nums

if __name__ == '__main__':
    ben = Benford()
    nums = ben.nthDigitTally(int(sys.argv[1]), ben.readMysteriousNumbers(sys.argv[2]))
    for i in range(0,len(nums)):
        print(str(i) + "s: " + str(nums[i]))

