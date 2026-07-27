import urllib.request
from bs4 import BeautifulSoup

url = 'https://dasactruyen.com/index.php/truyen-chu/incest-bi-mat-cua-toi-va-me-la-co-giao-day-nhac/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

print("Elements with title:")
for el in soup.find_all(text=lambda t: t and 'Incest' in t):
    parent = el.parent
    print(f"Parent tag: {parent.name}, class: {parent.get('class')}")
    if parent.name not in ['title', 'script']:
        print(f"Text: {parent.text.strip()[:100]}")
        
print("Let's look at the description:")
desc = soup.find('div', class_='story-detail-info') or soup.find('div', class_='summary') or soup.find('div', class_='post-content')
if desc:
    print("Desc class:", desc.get('class'))
    print(desc.text.strip()[:200])

