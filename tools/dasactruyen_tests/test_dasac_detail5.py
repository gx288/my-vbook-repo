import urllib.request
from bs4 import BeautifulSoup

url = 'https://dasactruyen.com/index.php/truyen-chu/incest-bi-mat-cua-toi-va-me-la-co-giao-day-nhac/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

chaps = soup.find_all('a', href=lambda href: href and '/chuong' in href)
if chaps:
    for c in chaps[:4]:
        if "Đọc Từ Đầu" not in c.text:
            print("Chap:", c.text.strip())
            p = c.parent
            print(" Parent:", p.name, p.get('class'))
            if p.parent:
                print(" GrandParent:", p.parent.name, p.parent.get('class'))
