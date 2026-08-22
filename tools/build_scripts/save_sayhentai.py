import urllib.request

url = 'https://sayhentai.cfd/truyen/nhat-ky-o-tro-khong-che.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    with open('tools/build_scripts/sayhentai_detail.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Saved HTML")
except Exception as e:
    print(e)
