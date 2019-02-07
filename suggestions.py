import urllib.request 
import requests 
import xml.etree.ElementTree as et
from bs4 import BeautifulSoup

def encode_keyword(keyword: str) -> str:
    string = keyword.replace(' ', '%20')
    return string

def suggestions():
    keyword = str(encode_keyword(input("Please type a keyword: ")))
    lang = str(input("Please type a language you want to perform search in: "))
    url = f'https://www.google.com/complete/search?q={keyword}&hl={lang}&client=xml'
    xml = requests.get(url).text
    tree = et.fromstring(xml)
    
    for suggestion in tree.findall('CompleteSuggestion'):
        value = suggestion.find('suggestion')
        s = value.get('data')
        print(s)