import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def try_url(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.select('.d-flex.mb-3')
        if len(items) > 0:
            print(url, "WORKS:", len(items))
    except Exception as e:
        pass

try_url('https://truyenc.com/tim-kiem?q=incest')
try_url('https://truyenc.com/tim-truyen?q=incest')
try_url('https://truyenc.com/?s=incest')
try_url('https://truyenc.com/tim-truyen?keyword=incest')
try_url('https://truyenc.com/tim-truyen?search=incest')
try_url('https://truyenc.com/tim-kiem?tu-khoa=incest')
