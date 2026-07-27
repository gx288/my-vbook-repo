import urllib.request
from bs4 import BeautifulSoup

url = 'https://dasactruyen.com/?s=incest'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select('.box-full-right-item, .post-item')
    print("Found search items:", len(items))
except Exception as e:
    print(e)
