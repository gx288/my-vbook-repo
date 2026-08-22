import urllib.request
from bs4 import BeautifulSoup

url = 'https://sayhentai.cfd/the-loai/yuri'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    items = soup.select(".item")
    if not items:
        items = soup.select("article")
        
    print(f"Total items: {len(items)}")
    for item in items[:5]:
        print("-", item.select_one("a").get('title'))
except Exception as e:
    print("Error:", e)
