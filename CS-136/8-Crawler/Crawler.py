#
#River Sheppard
#Crawler
#
#Description:
#

import re
import sys
import urllib.request

def control(pName,n):
    pDict = {}
    pDict = crawl(pName,n,pDict)
    s = ""
    for a in pDict:
        s += a
        s += " : "
        s += str(pDict[a])
        s += "\n"
    f = open("Links.txt", "w")
    f.write(s)
    f.close()

    printFile()

def printFile():
    f = open("Links.txt", "r")
    print(f.read())
    f.close()


def crawl(pName,n,pDict):
    if n <= 0:
        return pDict
    else:
        links = scrape(pName)
        for a in links:
            if a in pDict.keys():
                pDict[a] += 1
                #print("hi: "+a+"  "+str(pDict[a]))
            else:
                pDict[a] = 1
                #print("hi: "+a+" added on level: "+str(n))
                pDict = crawl(a,n-1,pDict) 
    return pDict

def scrape(pName):
    #print("scraping")
    links = []
    s = "href.*?"
    p = re.compile(s)
    try:
        page = urllib.request.urlopen(pName)
        results = str(page.read()).split()
        for a in results:
            if p.match(a):
                a = a.replace('href="','')
                i = a.find('"')
                b = a[:i]
                #s = '".*?'
                #a= re.sub('".*?','',a)
                links.append(b)
            
    except:
        print("fail on: "+pName)
        #print("",end = "")
    return links


if __name__ == "__main__":
    pName = "https://www.google.com/"
    n = 2
    if len(sys.argv) > 1:
        pName = sys.argv[1]
    if len(sys.argv) > 2:
        n = int(sys.argv[2])
    control(pName,n)
    
    
        
