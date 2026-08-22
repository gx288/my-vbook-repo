import urllib.request
from bs4 import BeautifulSoup

url = 'https://sayhentai.cfd/truyen/nhat-ky-o-tro-khong-che.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    print("--- Detail Info ---")
    print("Title:", soup.select_one('h1').text if soup.select_one('h1') else "No title")
    print("Cover:", soup.select_one('.info-image img')['src'] if soup.select_one('.info-image img') else "No cover")
    
    print("\n--- Chapters ---")
    chaps = soup.select('.list-chapters a')
    if not chaps:
        chaps = soup.select('.wp-manga-chapter a')
    if not chaps:
        chaps = soup.select('.chap-item a')
    if not chaps:
        chaps = soup.select('.chapter-list a')
        
    for i, chap in enumerate(chaps[:5]):
        print(chap.text.strip(), "->", chap.get('href'))
        
    print(f"Total chapters found: {len(chaps)}")
    if chaps:
        print("Saving first chap url to 'first_chap.txt'")
        with open('tools/build_scripts/first_chap.txt', 'w') as f:
            f.write(chaps[0].get('href'))
            
except Exception as e:
    print(e)
