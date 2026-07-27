import urllib.request
from bs4 import BeautifulSoup

url = 'https://dasactruyen.com/index.php/chuong/chuong-1-incest-bi-mat-cua-toi-va-me-la-co-giao-day-nhac/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

content = soup.find('div', class_='chapter-content') or soup.find('div', class_='story-content') or soup.find('div', class_='entry-content')
if content:
    print("Found content, class:", content.get('class'))
    print("Length:", len(content.text))
