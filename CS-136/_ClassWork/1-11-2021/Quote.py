##
##  River Sheppard - In class work
##  Code for a null terminated linked list. Each node of the linked 
##  list is a Card class defined within Quote.
##  Web Exercise 4.3.1
##

class Card:

    def __init__(self, word):
        self.word = word
        self.next = None

class Quote:

    # constructor - create an empty quote
    def __init__(self):
        self.start = None

    # add the word w to the end of the quote
    def addWord(self, w):
        newWord = Card(w)

        # degenerate case when w is first word
        if self.start == None:
            self.start = newWord

        # otherwise, traverse list until card points to last word
        else :
            card = self.start
            while card.next != None: 
                card = card.next
            # add card for new word to end of list
            card.next = newWord

    # number of words in the quote
    def count(self):
        total = 0
        if self.start != None:
            total += 1
        card = self.start
        while card.next != None:
            card = card.next
            total += 1
        return total

    # return the ith word where i = 0 is first word in quote
    def getWord(self, i):
        # check for less than i words in quote or invalid index
        if self.count() < i or i < 0:
            throw ("index out of bounds")

        card = self.start
        for count in range(0, i):
            card = card.next
        return card.word

    # insert w after the ith word, where i = 0 is the first word 
    def insertWord(self, i, w):
        # check for less than i words in quote or invalid index
        if self.count() < i or i < 0:
            throw ("index out of bounds");

        # make Card for the new word, place it after the ith card
        newWord = Card(w)
        card = self.start
        for j in range(0, i) :
            card = card.next
        #Makes it so the new word points to the next card
        newWord.next = card.next
        #Changes the .next for the previous to the new word
        card.next = newWord

    # string representation of the quote   
    def toString(self):
        s = ""
        card = self.start
        while card.next != None:
            s = s + card.word + " "
            card = card.next
        s = s + card.word + " "
        return s

if __name__ == "__main__":
    q = Quote()
    q.addWord("A")
    q.addWord("rose")
    q.addWord("is")
    q.addWord("a")
    q.addWord("rose.")
    print(q.toString())
    print(q.count())
    print(q.getWord(1))
    q.insertWord(2, "just")
    print(q.toString())
    print(q.count())
