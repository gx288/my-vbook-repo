import urllib.request

url = 'https://sayhentai.cfd/favicon.ico'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response, open('sayhentai/icon.png', 'wb') as out_file:
        out_file.write(response.read())
    print("Downloaded icon")
except Exception as e:
    print(e)
