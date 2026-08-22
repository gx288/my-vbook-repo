import json
import os
import zipfile

with open('sayhentai/src/home.js', 'w', encoding='utf-8') as f:
    f.write('''function execute() {
    return Response.success([
        {title: "Mới cập nhật", input: "https://sayhentai.cfd/danh-sach?order_by=update_time", script: "gen.js"},
        {title: "Đọc nhiều nhất", input: "https://sayhentai.cfd/danh-sach?order_by=view", script: "gen.js"},
        {title: "Mới đăng", input: "https://sayhentai.cfd/danh-sach?order_by=new", script: "gen.js"}
    ]);
}''')

# Bump version to 15
with open('plugin.json', 'r', encoding='utf-8') as f:
    root_data = json.load(f)
for item in root_data['data']:
    if item['name'] == 'SayHentai':
        item['version'] = 15
with open('plugin.json', 'w', encoding='utf-8') as f:
    json.dump(root_data, f, indent=2, ensure_ascii=False)

with open('sayhentai/plugin.json', 'r', encoding='utf-8') as f:
    say_data = json.load(f)
say_data['metadata']['version'] = 15
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

print("Updated home.js and bumped to V15")
