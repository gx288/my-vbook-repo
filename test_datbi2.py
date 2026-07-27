import urllib.request
import json

url = 'https://raw.githubusercontent.com/dat-bi/ext-vbook/main/plugin.json'
try:
    req = urllib.request.urlopen(url)
    data = json.loads(req.read().decode('utf-8'))
    for item in data['data'][:5]:
        print(f"Name: {item.get('name')}, Regexp: {item.get('regexp')}")
except Exception as e:
    print(e)
