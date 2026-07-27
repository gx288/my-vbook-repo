import json
import os
import zipfile

def fix_regexp(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the 4 backslashes back to 2
    content = content.replace('"truyenc\\\\\\\\.com"', '"truyenc\\\\.com"')
    content = content.replace('"dasactruyen\\\\\\\\.com"', '"dasactruyen\\\\.com"')
    
    # Also fix version to 7 to force update
    data = json.loads(content)
    if 'metadata' in data:
        data['metadata']['version'] = 7
    if 'data' in data:
        for item in data['data']:
            item['version'] = 7
            item['regexp'] = item['regexp'].replace('\\\\', '\\')
            
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def repack(ext_dir):
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

fix_regexp('plugin.json')
fix_regexp('truyenc/plugin.json')
fix_regexp('dasactruyen/plugin.json')

repack('truyenc')
repack('dasactruyen')
