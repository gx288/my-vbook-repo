import urllib.request
from bs4 import BeautifulSoup

url = 'https://sayhentai.cfd/doc-truyen/nhat-ky-o-tro-khong-che/chapter-114.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    # Typical image containers for comic sites
    imgs = soup.select('.page-chapter img')
    if not imgs:
        imgs = soup.select('.reading-content img')
    if not imgs:
        imgs = soup.select('#chapter-content img')
    if not imgs:
        imgs = soup.select('.chapter-detail img')
    if not imgs:
        imgs = soup.select('#image-container img')
    if not imgs:
        imgs = soup.select('.image-container img')
        
    print(f"Found {len(imgs)} images.")
    if imgs:
        print("First 3 images:")
        for img in imgs[:3]:
            print(img.get('data-src') or img.get('src') or img.get('data-original'))
            
except Exception as e:
    print(e)
