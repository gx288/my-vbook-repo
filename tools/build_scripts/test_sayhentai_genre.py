import urllib.request
from bs4 import BeautifulSoup

url = 'https://sayhentai.cfd/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    genres = soup.select('.genres a, .the-loai a, .category a, ul.submenu li a')
    if not genres:
        # try to find a link containing /the-loai/
        genres = soup.find_all('a', href=lambda x: x and '/the-loai/' in x)
        
    print(f"Found {len(genres)} genres.")
    for a in genres[:10]:
        print(a.text.strip(), "->", a.get('href'))
except Exception as e:
    print("Error:", e)
