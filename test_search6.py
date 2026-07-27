import urllib.request
from bs4 import BeautifulSoup
import re

url = 'https://truyenc.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    for line in html.split('\n'):
        if 'timkiem' in line.lower() or 'search' in line.lower() or 'tim' in line.lower():
            print(line.strip()[:200])
except Exception as e:
    print(e)
