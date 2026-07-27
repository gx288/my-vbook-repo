import urllib.request
import re

url = 'https://truyenc.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    scripts = re.findall(r'<script.*?>.*?</script>', html, re.IGNORECASE | re.DOTALL)
    for s in scripts:
        if 'search' in s or 'tim' in s:
            print("Found script:")
            print(s[:200])
except Exception as e:
    print(e)
