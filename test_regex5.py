import urllib.request
import json
import zipfile
import io

url = 'https://raw.githubusercontent.com/dat-bi/ext-vbook/main/123ds/plugin.zip'
try:
    req = urllib.request.urlopen(url)
    zip_data = req.read()
    with zipfile.ZipFile(io.BytesIO(zip_data)) as z:
        with z.open('plugin.json') as f:
            data = json.loads(f.read().decode('utf-8'))
            print("Regexp:", data.get('metadata', {}).get('regexp'))
except Exception as e:
    print(e)
