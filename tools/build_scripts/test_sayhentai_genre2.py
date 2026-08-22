import urllib.request
from bs4 import BeautifulSoup

url = 'https://sayhentai.cfd/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    genres = soup.select('.genres a, .the-loai a, .category a, ul.submenu li a')
    print(f"Selector count: {len(genres)}")
except Exception as e:
    print(e)
