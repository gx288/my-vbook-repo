import requests
from bs4 import BeautifulSoup
import json

base_url = "https://hentaivn.casa"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

def test_home():
    res = requests.get(base_url, headers=headers)
    with open("home.html", "w", encoding="utf-8") as f:
        f.write(res.text)
    
    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.select(".item")
    if len(items) == 0:
        items = soup.select("li.item")
    print(f"Home items found: {len(items)}")
    
    for item in items[:2]:
        a = item.select_one("a")
        img = item.select_one("img")
        print(f"Title: {a.get('title') if a else 'No title'}")
        print(f"Link: {a.get('href') if a else 'No link'}")
        print(f"Image: {img.get('src') if img else (img.get('data-src') if img else 'No img')}")

def test_detail(url):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    title = soup.select_one(".page-info h1")
    if title:
        title = title.text.strip()
        
    cover = soup.select_one(".page-ava img")
    if cover:
        cover = cover.get('src')
        
    print(f"Detail Title: {title}")
    print(f"Detail Cover: {cover}")
    
    desc = soup.select_one(".box-description")
    if desc: print("Found desc")
    
    toc = soup.select(".listing tr td a")
    print(f"TOC items: {len(toc)}")

if __name__ == '__main__':
    test_home()
    # test_detail(f"{base_url}/30206-doc-truyen-tsun-deres.html")
