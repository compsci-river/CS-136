#River Sheppard
#BMIS375

import glob
import csv
import sys

class Observation:
    def __init__(s,_ObsID,_QSetID,_QOneVal,_QTwoVal,_QThreeVal,_QFourVal,_BigSkyScore,_BigforkScore):
        s.ObsID = _ObsID
        s.QSetID = _QSetID
        s.QOneVal = _QOneVal
        s.QTwoVal = _QTwoVal
        s.QThreeVal = _QThreeVal
        s.QFourVal = _QFourVal
        s.BigSkyScore = _BigSkyScore
        s.BigforkScore = _BigforkScore

class ScoredCSV:
    def __init__(s,_fName):
        s.fName _fName
        s.observations = []

class inputCSV:
    def __init__(s,_fName):
        s.fName = _fName
        with open(s.fName, newline='') as csvfile:
            reader = csv.reader(csvfile,
