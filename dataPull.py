import requests
from bs4 import BeautifulSoup
import re
import selenium

#Function to pull specified url. Takes a url as arg in string format, returns the html of the url.
def teamPull (url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser').encode("utf-8") 
    return(soup)

def tablePull (soup):
    soup.find("")