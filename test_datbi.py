import urllib.request
import json

url = 'https://raw.githubusercontent.com/dat-bi/ext-vbook/main/plugin.json'
try:
    data = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
    for item in data[:5]:
        print(f"Name: {item.get('name')}, Regexp: {item.get('regexp')}")
except Exception as e:
    print(e)
