import json
import os
import zipfile

def fix_script(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace .item fallback
    content = content.replace(
'''    var els = doc.select(".item");
    if (els.size() === 0) {
        els = doc.select("article");
    }''', 
'''    var els = doc.select(".page-item-detail");
    if (els.size() === 0) els = doc.select("article");
    if (els.size() === 0) els = doc.select(".item"); // Fallback to sidebar if really nothing else'''
    )
    
    # Replace chapter selector
    content = content.replace(
'''            var chapterSpan = e.select(".viewsCount span").first();
            if (chapterSpan) {
                desc = chapterSpan.text().trim();
            }''',
'''            var chapterSpan = e.select(".status").first();
            if (!chapterSpan) chapterSpan = e.select(".episode").first();
            if (!chapterSpan) chapterSpan = e.select(".viewsCount span").first();
            if (chapterSpan) {
                desc = chapterSpan.text().trim();
            }'''
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_script('sayhentai/src/gen.js')
fix_script('sayhentai/src/search.js')

# Bump version to 14
with open('plugin.json', 'r', encoding='utf-8') as f:
    root_data = json.load(f)
for item in root_data['data']:
    if item['name'] == 'SayHentai':
        item['version'] = 14
with open('plugin.json', 'w', encoding='utf-8') as f:
    json.dump(root_data, f, indent=2, ensure_ascii=False)

with open('sayhentai/plugin.json', 'r', encoding='utf-8') as f:
    say_data = json.load(f)
say_data['metadata']['version'] = 14
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

print("Bumped version to 14 and repacked")
