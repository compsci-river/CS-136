#
#River Sheppard
#Crawler
#
#Description: Crawls through a website and saves any links to a dictionary, then
#works recursivly to run through any new links. At the end the dictionary is
#written to a text file which is then printed to the screen
#

import re
import sys
import urllib.request

import ssl

#Starts the recursive loop and then manages writing the dictionary to a the file
#Inputs: string pName, the name of the webpage to start the crawl at. int n, the
#number of levels to crawl through
#Outputs: null
def control(pName,n):
    pDict = {}
    pDict = crawl(pName,n,pDict)
    #print("Dictionary created")
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
    pass

#Prints out the contents of the Links.txt file which is where the dictionary is
#written to
#Inputs: null
#Outputs: null
def printFile():
    f = open("Links.txt", "r")
    print(f.read())
    f.close()
    pass

#A recursive loop that takes a link and then adds any links found on its page to
#the dictionary, if they are new they get added to the dictionary, if they
#already exist in the dictionary increases the stored value by one calls itself
#on the new links
#Inputs: string pName, the name of the page to open. int n, the number of levels
#to crawl through. dictionary pDict, a dictionary of page names holding the
#number of times they are accessed.
#Outputs: dictionary pDict, a dictionary of page names holding the
#number of times they are accessed.
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

#Opens a page runs through it grabs any links and returns them contained in a
#list.
#Inputs: string pName, the name of the page to open.
#Outputs: list[string] links, a list containing the links found on the page
def scrape(pName):
    #print("scraping")
    links = []
    s = 'href=".*?"'
    p = re.compile(s)
    
    try:
        cxt = ssl.SSLContext()
        page = str(urllib.request.urlopen(pName,context=cxt).read())
        results = re.findall(p,page)
        for result in results:
            a = result.split('"')
            links.append(a[1])
    except:
        print("Failed to load: "+pName)
        #print("",end = "")
    #print(links)
    return links


if __name__ == "__main__":
    pName = "https://katie.mtech.edu/classes/csci136/index.php"
    n = 2
    if len(sys.argv) > 1:
        pName = sys.argv[1]
    if len(sys.argv) > 2:
        n = int(sys.argv[2])
    control(pName,n)
    
    
        
