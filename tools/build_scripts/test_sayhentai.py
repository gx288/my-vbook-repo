import urllib.request
from bs4 import BeautifulSoup

url = 'https://sayhentai.cfd/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    # Let's find some story links
    print("Title:", soup.title.string)
    
    # Try to find items. Typical class names: item, post-item, page-item, etc.
    items = soup.select('.item')
    if not items:
        items = soup.select('.page-item-detail')
    if not items:
        items = soup.select('article')
    if not items:
        items = soup.select('.manga-item')
        
    print(f"Found {len(items)} items using typical selectors.")
    if items:
        for i, item in enumerate(items[:3]):
            print(f"\n--- Item {i+1} ---")
            print(item.prettify()[:500])
            
except Exception as e:
    print(e)
