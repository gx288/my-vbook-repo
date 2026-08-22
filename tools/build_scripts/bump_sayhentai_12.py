import json
import os
import zipfile

# Bump root version to 12
with open('plugin.json', 'r', encoding='utf-8') as f:
    root_data = json.load(f)

for item in root_data['data']:
    if item['name'] == 'SayHentai':
        item['version'] = 12

with open('plugin.json', 'w', encoding='utf-8') as f:
    json.dump(root_data, f, indent=2, ensure_ascii=False)

# Bump sayhentai version to 12
with open('sayhentai/plugin.json', 'r', encoding='utf-8') as f:
    say_data = json.load(f)
say_data['metadata']['version'] = 12
with open('sayhentai/plugin.json', 'w', encoding='utf-8') as f:
    json.dump(say_data, f, indent=2, ensure_ascii=False)

# Repack
ext_dir = 'sayhentai'
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

print('Bumped version to 12 and repacked zip')
