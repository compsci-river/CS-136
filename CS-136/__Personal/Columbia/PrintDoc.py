#River Sheppard

import fitz
import glob
import csv
import re

def printDoc(fName):
    text = ""
    with fitz.open(fName) as doc:
        for page in doc:
            text += page.get_text("text")
    print(text)
    st = text[text.find("GST/HST"):]
    st = st[st.find("\n")+1:]
    st = st[:st.find("\n")]
    print(st)

if __name__ == "__main__":
    printDoc(glob.glob("Print/*.PDF")[0])
