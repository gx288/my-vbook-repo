import urllib.request
from bs4 import BeautifulSoup

url = 'https://truyenc.com/truyen/em-linh-cung-lop/phan-2-70132'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    content = soup.select('.story-content')
    if len(content) > 0:
        c = content[0]
        # remove script, iframe, a
        for s in c.select('script'): s.extract()
        for s in c.select('iframe'): s.extract()
        for s in c.select('a'): s.extract()
        print(c.prettify()[:500])
    else:
        print("NO .story-content FOUND")
except Exception as e:
    print(e)
