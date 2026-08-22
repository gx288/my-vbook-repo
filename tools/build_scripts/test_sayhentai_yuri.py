import urllib.request
from bs4 import BeautifulSoup

url = 'https://sayhentai.cfd/the-loai/yuri'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    print("Page Title:", soup.title.string if soup.title else "No Title")
    
    item = soup.select_one(".item")
    if not item:
        item = soup.select_one("article")
    print("First item:", item.select_one("a").get('title') if item and item.select_one("a") else "None")
except Exception as e:
    print("Error:", e)
