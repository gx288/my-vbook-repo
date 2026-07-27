import json
import os
import zipfile

def fix_regexp(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    if 'metadata' in data:
        data['metadata']['version'] = 9
        # Change regexp to cover full URL for browser recognition
        old_reg = data['metadata']['regexp']
        if 'truyenc' in old_reg:
            data['metadata']['regexp'] = ".*truyenc\\\\.com.*"
        elif 'dasactruyen' in old_reg:
            data['metadata']['regexp'] = ".*dasactruyen\\\\.com.*"
            
    if 'data' in data:
        for item in data['data']:
            item['version'] = 9
            if 'truyenc' in item['regexp']:
                item['regexp'] = ".*truyenc\\\\.com.*"
            elif 'dasactruyen' in item['regexp']:
                item['regexp'] = ".*dasactruyen\\\\.com.*"
                
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
