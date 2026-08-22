import urllib.request
from bs4 import BeautifulSoup

url = 'https://sayhentai.cfd/truyen/nhat-ky-o-tro-khong-che.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    title = soup.select_one("h1").text.strip() if soup.select_one("h1") else "NO_TITLE"
    print("Title:", title)
    
    cover = None
    if soup.select_one(".movie-thumb"):
        cover = soup.select_one(".movie-thumb").get("data-src") or soup.select_one(".movie-thumb").get("src")
    print("Cover:", cover)
    
    author = "Đang cập nhật"
    print("Author:", author)
    
    desc = soup.select_one("[itemprop=description]").text.strip() if soup.select_one("[itemprop=description]") else ""
    # remove #Tags if they are inside
    if soup.select_one(".the_tag_list"):
        soup.select_one(".the_tag_list").decompose()
    desc = soup.select_one("[itemprop=description]").text.strip() if soup.select_one("[itemprop=description]") else ""
    print("Desc:", desc[:100], "...")
    
    genres = soup.find_all('a', href=lambda x: x and '/the-loai/' in x)
    print("Genres:", [g.text.strip() for g in genres])
except Exception as e:
    print(e)
