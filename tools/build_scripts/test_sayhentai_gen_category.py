import urllib.request
from bs4 import BeautifulSoup

url = 'https://sayhentai.cfd/the-loai/action'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    els = soup.select(".item")
    if not els:
        els = soup.select("article")
        
    print(f"Found {len(els)} items.")
    if len(els) > 0:
        a = els[0].select_one("a")
        img = els[0].select_one("img")
        print("First item a:", a)
        print("First item img:", img)
except Exception as e:
    print("Error:", e)
