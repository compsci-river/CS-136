import Benford
import sys

#py -m testingBenford 0 TestData.txt

ben = Benford.Benford()



nums = ben.nthDigitTally(int(sys.argv[1]), ben.readMysteriousNumbers(sys.argv[2]))

print(nums)
