import urllib.request
from bs4 import BeautifulSoup

url = 'https://truyenc.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    form = soup.find('form')
    if form:
        print("Form action:", form.get('action'))
        for input in form.find_all('input'):
            print(" Input name:", input.get('name'))
except Exception as e:
    print(e)
