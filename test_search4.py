import urllib.request
from bs4 import BeautifulSoup

url = 'https://truyenc.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    for input in soup.find_all('input'):
        print(input)
except Exception as e:
    print(e)
