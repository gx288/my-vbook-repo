import urllib.request
from bs4 import BeautifulSoup

url = 'https://dasactruyen.com/index.php/truyen-chu/incest-bi-mat-cua-toi-va-me-la-co-giao-day-nhac/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

print("Title:", soup.find('h1', class_='entry-title').text.strip())

desc_divs = soup.find_all('div', class_='entry-content') or soup.find_all('div', class_='comic-description')
if desc_divs:
    print("Desc length:", len(desc_divs[0].text))
    print(desc_divs[0].text.strip()[:100])

author_list = soup.select('.item-author a') or soup.select('div.author')
if author_list:
    print("Author:", author_list[0].text.strip())

# chapters
chaps = soup.select('.list-chapter a, ul.chapter-list a, .chapter-list a, ul.chapters li a')
print(f"Found {len(chaps)} chapters using css selectors.")
if not chaps:
    # let's look for any link containing '/chuong'
    chaps = soup.find_all('a', href=lambda href: href and '/chuong' in href)
    print(f"Found {len(chaps)} chapters using regex.")
    
for c in chaps[:2]:
    print(c.get('href'), c.text.strip())
