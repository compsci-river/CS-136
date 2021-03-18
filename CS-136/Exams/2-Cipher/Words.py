# Name        : River Sheppard
# Description : Stores a dictionary of words so that the cipher will be able to
#check if the words it has are real words

import sys

class Words:

    # Construct our word list, loading words from the given filename.
    # The file contains a single word on each line.
    # If the filename is not found, the object contains a data structure of
    # words with a length of 0.
    #
    # Input parameters: filename, the name of the file to read and store
    # Return values: none
    def __init__(self, filename):
        self.dict = {}
        try:
            with open(filename, 'r') as f:
                words = f.read().split()
                for w in words:
                    self.dict[w] = 1
            f.close()
        except:
            pass
                

    
    # Returns the number of words in this collection.
    #
    # Input parameters: none
    # Return values: The number of words in the data structure storing them
    def getSize(self):
        return len(self.dict)
    
    # Returns true if the given word is in our collection, false otherwise.
    #
    # Input parameters: A single string representing a "word"
    # Return values: True if "word" is in our dictionary, false otherwise.
    def inVocab(self, word):
        if self.dict.get(word) == 1:
            return True
        else:
            return False
    
    # Calculates the percent of words in the given sentence that are in our word list.
    # Words in the sentence are separated from each other by whitespace.
    # Returns a floating-point value in [0.0, 1.0] where 1.0 means 100% of words were in our list.
    #
    # Input parameters: A string representing a sentence of words
    # Return values: The percentage of words in the input string that were found in the dictionary.
    def inVocabPercent(self, sentence):
        words = sentence.split()
        count = 0
        for i in range(len(words)):
            wordInDict = self.inVocab(words[i])
            #print(wordInDict)
            if wordInDict:
                count += 1
        return count / len(words)


if __name__ == "__main__":
    s = "hi there my name is river gggggbbbb help"
    w = Words("words.txt")
    per = w.inVocabPercent(s)
    print(per)
    #print(w.dict)

