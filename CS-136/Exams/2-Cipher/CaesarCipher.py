# Name        : River Sheppard
# Description : Opens the input files creates a dictionary and uses the other
#classes to decipher the second file, uses threads to try all of the shift
#options at once

import sys
from Words import Words
from Shifter import Shifter
import threading

# This is the calling program to run the CeasarCipher code. It checks for valid
# input files, reads those files into appropriate instantiated objects, and
# launches a thread for each of the 26 Shifters to test all shift possibilities.
if len(sys.argv) < 2:
    print("CaesarCipher <word file> <cipher file>")
else:
    words = Words(sys.argv[1])
    cipher = ""
    if words.getSize() == 0:
        print("Word file not found!")
    else:
        print("Loaded", words.getSize(), "words.")
        
        try:
            f = open(sys.argv[2])
            cipher = f.readline()
            f.close();
        except:
            print("Cipher file not found!")
        print("Loaded cipher of length", len(cipher))

        shifts = []
        #creates threads for a shift 0-26
        for i in range(26):
            shifts.append(Shifter(words,cipher,i))
            a = threading.Thread(target=shifts[i].run)
            a.start()

        running = True
        #waits until all of the shifts created by the threads have a valid result
        while running:
            running = False
            for s in shifts:
                if s.getResult() == None:
                    running = True
        #prints all of the results
        for s in shifts:
            print(s.getResult().toString())

