import urllib.request
from bs4 import BeautifulSoup

url = 'https://dasactruyen.com/index.php/truyen-chu/incest-bi-mat-cua-toi-va-me-la-co-giao-day-nhac/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

print("Title:", soup.find('h1').text.strip() if soup.find('h1') else "N/A")
author = soup.find('div', class_='author') or soup.find(text=lambda t: t and 'Tác giả' in t)
print("Author:", author.parent.text.strip() if author else "N/A")
print("Cover:", soup.find('img', class_='img-fluid').get('src') if soup.find('img', class_='img-fluid') else "N/A")
desc = soup.find('div', class_='summary-content') or soup.find('div', class_='desc') or soup.find('div', id='summary')
print("Description:", desc.text.strip()[:100] if desc else "N/A")

chaps = soup.find_all('li', class_='chapter') or soup.find_all('a', class_='chapter')
print(f"Found {len(chaps)} chapters using normal list")
if not chaps:
    # Try finding any link that looks like a chapter
    chaps = soup.find_all('a')
    chap_links = [a for a in chaps if a.get('href') and '/chuong' in a.get('href')]
    print(f"Found {len(chap_links)} chapter links via regex/contains")
    if chap_links:
        print("Sample:", chap_links[0].get('href'))
