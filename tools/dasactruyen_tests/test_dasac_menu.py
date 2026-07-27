import urllib.request
from bs4 import BeautifulSoup
import re

url = 'https://dasactruyen.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

print("--- Checking Menus ---")
navs = soup.find_all(['ul', 'div'], class_=re.compile('menu|nav'))
for nav in navs:
    links = nav.find_all('a')
    if len(links) > 2:
        print(f"Found menu with {len(links)} links. First 3:")
        for l in links[:3]:
            print(f"  {l.text.strip()} : {l.get('href')}")
