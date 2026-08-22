import json
import os
import zipfile

def add_desc(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_code = '''            var cover = img.attr("data-src");
            if (!cover) cover = img.attr("src");
            
            list.push({
                name: a.attr("title") || a.text().trim(),
                link: link,
                cover: cover,
                description: "",
                host: "https://sayhentai.cfd"
            });'''
            
    new_code = '''            var cover = img.attr("data-src");
            if (!cover) cover = img.attr("src");
            
            var desc = "";
            var chapterSpan = e.select(".viewsCount span").first();
            if (chapterSpan) {
                desc = chapterSpan.text().trim();
            }
            
            list.push({
                name: a.attr("title") || a.text().trim(),
                link: link,
                cover: cover,
                description: desc,
                host: "https://sayhentai.cfd"
            });'''
            
    if old_code in content:
        content = content.replace(old_code, new_code)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated", filepath)
    else:
        print("Could not find code to replace in", filepath)

add_desc('sayhentai/src/gen.js')
add_desc('sayhentai/src/search.js')

# Bump version to 13
with open('plugin.json', 'r', encoding='utf-8') as f:
    root_data = json.load(f)
for item in root_data['data']:
    if item['name'] == 'SayHentai':
        item['version'] = 13
with open('plugin.json', 'w', encoding='utf-8') as f:
    json.dump(root_data, f, indent=2, ensure_ascii=False)

with open('sayhentai/plugin.json', 'r', encoding='utf-8') as f:
    say_data = json.load(f)
say_data['metadata']['version'] = 13
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
print("Bumped version to 13 and repacked")
