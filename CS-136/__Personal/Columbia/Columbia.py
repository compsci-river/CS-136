#River Sheppard

import fitz
import glob
import csv
import re

class InvoiceDoc:
    def __init__(s,fName):
        
        s.text = ""
        s.invoiceNum = ""
        s.date = ""
        s.orderNum = ""
        s.GST = ""
        with fitz.open(fName) as doc:
            for page in doc:
                s.text += page.get_text("text")
        s.splitStr = s.text.split("\n")
        s.randa = True
        s.pri = False
        if s.text[:20].find("Invoice") != -1:
            s.randa = False
        s.operate()

    def print(s):
        print("Invoice Number: " + s.invoiceNum + "\n")
        print(s.text)

    def getInvoiceNumRanda(s):
        index = s.text.find("\n")
        inNum = s.text[index-10:index]
        for i in range(10):
            if inNum[i] != " ":
                s.invoiceNum = inNum[i:]
                return

    def getInvoiceNumDelta(s):
        s.invoiceNum = s.splitStr[24]

    def getInvoiceDateRanda(s):
        index = s.text.find("Invoice Date:")
        index = s.text.find(":")+1
        st = s.text[index:]
        index = st.find("\n")
        st = st[:index]
        for i in range(len(st)):
            if st[i] != " ":
                s.date = st[i:]
                return
        s.date=st
        

    def getInvoiceDateDelta(s):
        st = re.findall("\d\d/\d\d/\d\d",s.text)
        s.date = st[0]

    def getOrderNumRanda(s):
        st = s.splitStr[6][1:]
        s.orderNum = st[:st.find(" ")]

    def getOrderNumDelta(s):
        s.orderNum = s.splitStr[25]

    def getGSTRanda(s):
        index = s.text.find("Goods, Harmonized and Servic")
        if index == -1:
            index = s.text.find("Goods and Services Tax")
        st = s.text[index:]
        st = st[st.find("  "):st.find("\n")]
        for i in range(8):
            if st[-i] == " ":
                s.GST = st[-i:]
                return

    def getGSTDelta(s):
        st = s.text[s.text.find("GST/HST"):]
        st = st[st.find("\n")+1:]
        s.GST = st[:st.find("\n")]

    def operate(s):
        if s.randa:
            s.getInvoiceNumRanda()
            s.getInvoiceDateRanda()
            s.getOrderNumRanda()
            s.getGSTRanda()
        else:
            s.getInvoiceNumDelta()
            s.getInvoiceDateDelta()
            s.getOrderNumDelta()
            s.getGSTDelta()
        if s.pri:
            s.print()

def write(docs,csvName):
    with open(csvName, 'w', newline='') as csvfile:
        writ = csv.writer(csvfile)
        writ.writerow(['Invoice Number',
                       'Invoice Date',
                       'Order Number',
                       'GST'])
        for doc in docs:
            #doc.print()
            writ.writerow([doc.invoiceNum,
                           doc.date,
                           doc.orderNum,
                           doc.GST])

def run(folderName,csvName):
    docs = []
    files = glob.glob(folderName+"/*.PDF")
    for fName in files:
        doc = InvoiceDoc(fName)
        docs.append(doc)
    write(docs,csvName)

if __name__ == "__main__":
    run("Files","Output.csv")
