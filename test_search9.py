import urllib.request
import re

url = 'https://truyenc.com/scripts/custom.js'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    js = urllib.request.urlopen(req).read().decode('utf-8')
    if 'search' in js.lower() or 'tim' in js.lower():
        print("Found search in custom.js!")
        # Print lines with search
        for line in js.split('\n'):
            if 'search' in line.lower() or 'tim' in line.lower():
                print(line.strip()[:100])
except Exception as e:
    print(e)
