import urllib.request
from bs4 import BeautifulSoup

url = 'https://dasactruyen.com/index.php/truyen-chu/incest-bi-mat-cua-toi-va-me-la-co-giao-day-nhac/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

print("Title string:", soup.title.string if soup.title else "N/A")
print("h1:", soup.find('h1').text.strip() if soup.find('h1') else "N/A")
print(soup.prettify()[:1000])
