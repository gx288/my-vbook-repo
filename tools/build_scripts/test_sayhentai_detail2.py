import urllib.request
from bs4 import BeautifulSoup

url = 'https://sayhentai.cfd/truyen/nhat-ky-o-tro-khong-che.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    title = soup.select_one("h1").text.strip() if soup.select_one("h1") else "NO_H1"
    print("Title:", title)
    
    cover = None
    for img in soup.find_all('img'):
        if 'lazy' in img.get('class', []) or 'thumb' in img.get('class', []):
            cover = img.get('data-src') or img.get('src')
            break
    print("Cover:", cover)
    
    author = "Đang cập nhật"
    print("Author:", author)
except Exception as e:
    print(e)
