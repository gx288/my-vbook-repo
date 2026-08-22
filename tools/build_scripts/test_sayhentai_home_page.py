import urllib.request
from bs4 import BeautifulSoup

url = 'https://sayhentai.cfd/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    page_nav = soup.select('.page-nav a, .pagination a, .nav-links a')
    for a in page_nav:
        print(a.text.strip(), "->", a.get('href'))
except Exception as e:
    print("Error:", e)
