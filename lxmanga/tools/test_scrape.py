import requests
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

def test_dump():
    url = "https://www.lxmanga.quest/truyen-hentai/?m_orderby=rating"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    r = requests.get(url, headers=headers)
    with open("list.html", "w", encoding="utf-8") as f:
        f.write(r.text)

if __name__ == "__main__":
    test_dump()
