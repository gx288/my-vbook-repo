import urllib.request
from bs4 import BeautifulSoup

url = 'https://truyenc.com/truyen/em-linh-cung-lop-1177'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    list = []
    
    # Simulate current toc.js
    els = soup.select('.story-chapters-main a')
    for e in els:
        link = e.get('href')
        if link and '/truyen/' in link:
            name = e.text.strip()
            if name != 'Đọc truyện' and name != '':
                list.append({'name': name, 'url': link})
                
    if len(list) == 0:
        els = soup.select('a')
        for e in els:
            link = e.get('href')
            if link and '/truyen/' in link and '/chuong-' not in link and '/phan-' in link:
                name = e.text.strip()
                if name != 'Đọc truyện' and name != '':
                    exists = False
                    for j in list:
                        if j['url'] == link:
                            exists = True
                    if not exists:
                        list.append({'name': name, 'url': link})
                        
    for l in list:
        print("TOC:", l['name'], "->", l['url'])
except Exception as e:
    print(e)
