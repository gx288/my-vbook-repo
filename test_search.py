import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def test_truyenc(key):
    url = f'https://truyenc.com/tim-truyen?key={urllib.parse.quote(key)}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.select('.d-flex.mb-3')
        print("Truyenc items:", len(items))
    except Exception as e:
        print("Truyenc fail:", e)

def test_dasac(key):
    url = f'https://dasactruyen.com/?s={urllib.parse.quote(key)}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.select('article')
        print("Dasac items:", len(items))
    except Exception as e:
        print("Dasac fail:", e)

test_truyenc('incest')
test_dasac('incest')
