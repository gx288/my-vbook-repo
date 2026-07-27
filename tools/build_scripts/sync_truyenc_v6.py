import json
import os
import zipfile

def bump_inner(ext_dir, new_ver):
    json_path = os.path.join(ext_dir, 'plugin.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data['metadata']['version'] = new_ver
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

bump_inner('truyenc', 6)

# Clean up the test_search scripts
import glob
for f in glob.glob('test_search*.py'):
    os.remove(f)

