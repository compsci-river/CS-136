#
#River Sheppard
#Lab 4: Mind Reader
#Description: A game where the computer tries to guess what the player will choose next between heads and tails. It
#does so by creating a dictionary where each entry's key is a code of four entrys, and stored there is a list of
#what the player has choosen after that sequence in the past. Then it forms its guesses based on the patterns it
#finds
#

import random

class MindReader:
    #Constructor, holds the dictionary
    def __init__(self):
        self.hashDict = {}

    #Adds to the dictionary, checks the hashCodes list to see if the first is a valid code, then it checks if it is
    #already in the dictionary if it is than it updates the entry with the new player entry, if it is not in the
    #dictionary it creates a new entry based on the player's entry, then it cycles the hashCode list so that it is
    #ready for a new entry
    #Inputs: List hashCodes, a list that is four long, the first item holds the last four entries, the second holds
    #the last three and so on. String playerGuess, the newest entry by the player
    #Outputs: List hashCodes, the cycled list ready to have the player entry added
    def hashUpdate(self, hashCodes, playerGuess):
        hashCode = hashCodes[0]
        values = []
        if len(hashCode) == 4:
            if self.hashDict.get(hashCode) == None:
                if playerGuess == "H":
                    values = [1,0]
                elif playerGuess == "T":
                    values = [0,1]
                self.hashDict[hashCode] = values
            else:
                values = self.hashDict[hashCode]
                if playerGuess == "H":
                    values[0] += 1
                elif playerGuess == "T":
                    values[1] += 1
        hashCodes[0] = hashCodes[1]
        hashCodes[1] = hashCodes[2]
        hashCodes[2] = hashCodes[3]
        hashCodes[3] = ""
        return hashCodes
        
    #Gets the player input and checks to make sure it is valid, it uses hashUpdate() to update the dictionary and
    #then it adds the player entry to the hashCodes list
    #Inputs: List hashCodes, the list containing strings defining the previous stretch of player entries
    #Outputs: List hashCodes, now cycled and updated with the new player entry
    def playerEntry(self, hashCodes):
        entry = input("Enter H for heads or T for tails: ").upper()
        while entry != "H" and entry != "T":
            entry = input("That was not a valid response. \nEnter H for heads or T for tails: ").upper()
        hashCodes = self.hashUpdate(hashCodes, entry)
        for i in range(0,len(hashCodes)):
            hashCodes[i] += entry
        return hashCodes

    #Gets the computer's guess, if the current hashCode exists in the dictionary it will return the value that has
    #been more common in the past, if the values occur at eqaul frequency or if the hashCode does not exist in the
    #dictionary it will return a random choice between the variables
    #Inputs: String hashCode, the last four entries by the player
    #Outputs: String, it returns the letter that it determines is more likely
    def compGuess(self, hashCode):
        guess = -1
        values = self.hashDict.get(hashCode)
        if values != None:
            if values[0] > values[1]:
                guess = 0
            elif values[0] < values[1]:
                guess = 1
            else:
                guess = random.randint(0,1)
        else:
            guess = random.randint(0,1)
        if guess == 0:
            return "H"
        elif guess == 1:
            return "T"

    #Loops until someone wins, compares the player entry with the computer guess adds points to the one who deserves
    #them, checks if someone wins.
    #Inputs: null
    #Outputs: null
    def runReader(self):
        hashCodes = ["","","",""]
        playerPoints = 0
        compPoints = 0
        hashCode = hashCodes[0]
        while playerPoints < 25 and compPoints < 25:
            guess = self.compGuess(hashCode)
            hashCodes = self.playerEntry(hashCodes)
            playerGuess = hashCodes[3]
            hashCode = hashCodes[0]
            if guess == playerGuess:
                compPoints += 1
            else:
                playerPoints +=1
            print("Computer predicted: " + guess + ". Player chose: " + playerGuess + ".")
            print("Computer: " + str(compPoints) + ". Player: " + str(playerPoints) + ".")
        if playerPoints == 25:
            print("Player wins!!!")
        elif compPoints == 25:
            print("Computer wins!!!")
        else:
            print("Something went wrong")

if __name__ == "__main__":
    #runs the program
    mindReader = MindReader()
    mindReader.runReader()
                
