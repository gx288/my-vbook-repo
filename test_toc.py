import urllib.request
from bs4 import BeautifulSoup

url = 'https://truyenc.com/truyen/em-linh-cung-lop-1177'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    print("--- OLD V1 SELECTOR: .story-chap-item ---")
    old_items = soup.select('.story-chap-item')
    for item in old_items:
        print("Href:", item.get('href'))
        
    print("\n--- NEW V2 SELECTOR: .story-chapters-main a ---")
    new_items = soup.select('.story-chapters-main a')
    for item in new_items:
        print("Href:", item.get('href'))
except Exception as e:
    print(e)
