import urllib.request
from bs4 import BeautifulSoup

url = 'https://truyenc.com/truyen/em-linh-cung-lop-1177'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    # EXACT logic from toc.js
    els = soup.select(".story-chapters-main a")
    for e in els:
        print("A-TAG:", e)
        
except Exception as e:
    print(e)
