import urllib.request
from bs4 import BeautifulSoup

url = 'https://truyenc.com/truyen/em-linh-cung-lop-1177'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    els = soup.select(".story-chap-item")
    for e in els:
        if '1177' in e.get('href', ''):
            print("FOUND ONE!", e.get('href'))
except Exception as e:
    print(e)
