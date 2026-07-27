import urllib.request
from bs4 import BeautifulSoup

url = 'https://dasactruyen.com/?s=incest'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

items = soup.find_all('article') or soup.find_all('div', class_='comic-item') or soup.find_all('h2', class_='entry-title')
if items:
    print("Found items via entry-title/article:", len(items))
    for i in items[:2]:
        print(i.prettify()[:100])
