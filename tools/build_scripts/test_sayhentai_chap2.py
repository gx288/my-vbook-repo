import urllib.request
from bs4 import BeautifulSoup

url = 'https://sayhentai.cfd/doc-truyen/nhat-ky-o-tro-khong-che/chapter-114.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    # Let's find the parent of large groups of images
    imgs = soup.find_all('img')
    print(f"Total images on page: {len(imgs)}")
    for img in imgs[:10]:
        print(f"Parent: {img.parent.name}, class: {img.parent.get('class')}")
        print("Src:", img.get('src') or img.get('data-src'))
        
except Exception as e:
    print(e)
