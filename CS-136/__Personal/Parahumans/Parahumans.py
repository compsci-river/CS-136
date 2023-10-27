import requests
from bs4 import BeautifulSoup

def run():
    response = requests.get(url="https://en.wikipedia.org/wiki/Special:Random",)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find(id='firstHeading')
    print(title.string)

run()

