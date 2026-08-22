import urllib.request
from bs4 import BeautifulSoup

url = 'https://sayhentai.cfd/?s=me'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    items = soup.select('.item')
    print(f"Search ?s=me -> Found {len(items)} items.")
except Exception as e:
    print("Error ?s=me:", e)

url2 = 'https://sayhentai.cfd/tim-kiem?q=me'
req2 = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html2 = urllib.request.urlopen(req2).read().decode('utf-8')
    soup2 = BeautifulSoup(html2, 'html.parser')
    items2 = soup2.select('.item')
    print(f"Search /tim-kiem?q=me -> Found {len(items2)} items.")
except Exception as e:
    print("Error /tim-kiem?q=me:", e)
