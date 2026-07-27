import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def test_truyenc(param, key):
    url = f'https://truyenc.com/tim-truyen?{param}={urllib.parse.quote(key)}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.select('.d-flex.mb-3')
        print(f"Truyenc items with {param}:", len(items))
    except Exception as e:
        print("Truyenc fail:", e)

test_truyenc('keyword', 'incest')
