import urllib.request
from bs4 import BeautifulSoup
import re

url = 'https://truyenc.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.find_all('a', href=True):
        if 'tim' in a['href'] or 'search' in a['href']:
            print("Found link:", a['href'])
except Exception as e:
    print(e)
