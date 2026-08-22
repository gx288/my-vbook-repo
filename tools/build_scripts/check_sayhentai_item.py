import urllib.request
from bs4 import BeautifulSoup

url = 'https://sayhentai.cfd/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    item = soup.select_one(".item")
    if not item:
        item = soup.select_one("article")
        
    print(item.prettify())
except Exception as e:
    print(e)
