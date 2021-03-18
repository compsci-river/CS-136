# Name        : River Sheppard
# Description : Result class to make the result printout easier

class Result:
    
    # Construct a new Result with the given text, in-vocabulary percent, and 
    # the shift amount that resulted in this deciphered text.
    #
    # Input parameters: text, the deciphered text
    #                   inVocabPercent, the floating point percentage of
    #                                   words that match dictionary words
    #                   shift, the integer value of the shift amount
    # Return values: none
    def __init__(self, text = "", inVocabPercent = 0.0, shift = 0):
        self.text = text
        self.percent = inVocabPercent
        self.shift = shift
    
    # Returns a String containing the details of this Result.
    # Format is three columns:
    #  1) The in-vocabulary percent, a floating-point number in [0.0, 1.0].
    #  2) The integer shift amount.
    #  3) The deciphered text. NOTE: this should be limited to at most 40 characters.
    # Example outputs:
    #  1.0000 12 it was the best of times it was the wors
    #  0.3333  1 xi lph iwt qthi du ixbth xi lph iwt ldgh
    # Hint: Look up string.format for creating formatted strings.
    #
    # Input paramters: none
    # Return values: a formatted string representing the result of a decipherment
    def toString(self):
        s = "%.4f" % self.percent
        return s+" "+str(self.shift)+" "+self.text[:40]

