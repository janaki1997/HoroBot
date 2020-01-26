import requests
from bs4 import BeautifulSoup

def get_description(zodiac): 
    url = "https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/" + zodiac
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id='daily')
    desc = results.find(class_='margin-top-xs-0')
    return(desc.get_text())