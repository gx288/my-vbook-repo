import json
import os
import zipfile

# Fix search.js for dasactruyen
js_path = 'dasactruyen/src/search.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('"?s=" + key', '"?s=" + encodeURIComponent(key)')
js = js.replace('/?s=" + key', '/?s=" + encodeURIComponent(key)')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

def bump_and_repack():
    ext_dir = 'dasactruyen'
    json_path = os.path.join(ext_dir, 'plugin.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data['metadata']['version'] = 6
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    zip_path = os.path.join(ext_dir, 'plugin.zip')
    if os.path.exists(zip_path):
        os.remove(zip_path)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(ext_dir):
            if 'plugin.zip' in files:
                files.remove('plugin.zip')
            for file in files:
                fpath = os.path.join(root, file)
                arcname = os.path.relpath(fpath, ext_dir)
                zf.write(fpath, arcname)

bump_and_repack()

# Bump root plugin.json version
with open('plugin.json', 'r', encoding='utf-8') as f:
    repo_data = json.load(f)

for item in repo_data['data']:
    item['version'] = 6

with open('plugin.json', 'w', encoding='utf-8') as f:
    json.dump(repo_data, f, indent=2, ensure_ascii=False)
