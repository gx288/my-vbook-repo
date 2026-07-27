import urllib.request
from bs4 import BeautifulSoup
import json

url = 'https://dasactruyen.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    print("Title:", soup.title.string if soup.title else "N/A")
    
    # Let's find categories
    categories = []
    for a in soup.find_all('a'):
        href = a.get('href')
        text = a.text.strip()
        if href and ('/the-loai' in href or '/tim-truyen' in href):
            if text and text not in [c['title'] for c in categories]:
                if not href.startswith('http'):
                    href = 'https://dasactruyen.com' + href
                categories.append({'title': text, 'input': href})
    print(f"Found {len(categories)} categories. Samples:")
    print(categories[:5])
    
    # Let's look for a generic story item wrapper
    wrappers = soup.select('.item-comic, .item, .card, .col-md-3, .story-item, figure')
    print(f"Found generic wrappers: {len(wrappers)}")
    
    # Print the first wrapper to analyze its structure
    if wrappers:
        print("--- Snippet of first wrapper ---")
        print(wrappers[0].prettify()[:1000])

except Exception as e:
    print(e)
