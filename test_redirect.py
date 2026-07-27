import urllib.request

url = 'https://truyenc.com/truyen/em-linh-cung-lop/phan-2-70132'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    resp = urllib.request.urlopen(req)
    print("Final URL after redirects:", resp.geturl())
except Exception as e:
    print(e)
