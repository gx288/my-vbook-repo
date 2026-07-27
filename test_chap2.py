import urllib.request
from bs4 import BeautifulSoup

url = 'https://truyenc.com/truyen/can-phong-cam/chuong-13-2381'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    content = soup.select('.story-content')
    if len(content) > 0:
        print("FOUND .story-content")
        print(content[0].prettify()[:200])
    else:
        print("NO .story-content FOUND")
except Exception as e:
    print(e)
