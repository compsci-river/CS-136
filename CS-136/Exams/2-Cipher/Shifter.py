# Name        : River Sheppard
# Description : Shifts the text the given number of places and stores it to a
#Result

from Result import Result

class Shifter:

    
    # Construct a new shifter object, setting its input cipher text and the shift amount.
    # NOTE: this method shouldn't do any decipherment, that is the job of the run method.
    #   It should create an additional attribute to store the final result of deciphering.
    #
    # Input parameters: words, the list of words to decipher
    #                   cipher, the result of this attempt at deciphering
    #                   shift, the integer indicating how many characters to shift by
    # Return values: none
    def __init__(self, words, cipher = "", shift = 0):
        self.words = words
        self.cipher = cipher
        self.shift = shift
        self.result = None
    
    # Rotate the given character to the right the given number of positions.
    # Works only for lowercase letters a-z, leaves the space character unshifted.
    # You should NOT need to change this method.
    #
    # Input parameters: ch, the character to be shifted
    # Return values: the character resulting from the shift
    def rotateChar(self, ch):
        num = ord(ch)
        if num == 32:
            return " "
        num += self.shift
        if num > 122:
            num -= 26
        return chr(num)

    # Actually perform the shifting of the cipher text to get a possible plain text and
    #   stores this in the attribute holding a Result. 
    #
    # Input parameters: none
    # Return values: none
    def run(self):
        #print("running")
        deciphered = ""
        for i in range(len(self.cipher)):
            deciphered += self.rotateChar(self.cipher[i])
        percent = self.words.inVocabPercent(deciphered)
        self.result = Result(deciphered,percent,self.shift)

    
    # Return a Result object containing the plain text decipherment as well as the
    # percent of words that are in-vocabulary with respect to our word list.
    #
    # Input parameters: none
    # Return values: The result of the deciphering, a Result object that holds the percentage of
    #   deciphered words found in the words dictionary
    def getResult(self):
        return self.result
