import urllib.request
from bs4 import BeautifulSoup

url = 'https://truyenc.com/truyen/can-phong-cam-63'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    els = soup.select(".story-chap-item")
    print("Found .story-chap-item:", len(els))
    
    els2 = soup.select(".story-chapters-main a")
    print("Found .story-chapters-main a:", len(els2))
except Exception as e:
    print(e)
