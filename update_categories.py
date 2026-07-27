from bs4 import BeautifulSoup
import json
import zipfile
import os

with open('user_categories.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')
genres = []
for a in links:
    title = a.find('span').text.strip()
    href = a.get('href')
    genres.append({
        'title': title,
        'input': href,
        'script': 'gen.js'
    })

# Write to genre.js
genre_js = "function execute() {\n    return Response.success([\n"
for i, g in enumerate(genres):
    comma = "," if i < len(genres)-1 else ""
    genre_js += f"        {{title: \"{g['title']}\", input: \"{g['input']}\", script: \"gen.js\"}}{comma}\n"
genre_js += "    ]);\n}"

with open('truyenc/src/genre.js', 'w', encoding='utf-8') as f:
    f.write(genre_js)

# Update version in root plugin.json
with open('plugin.json', 'r', encoding='utf-8') as f:
    repo_data = json.load(f)
repo_data['data'][0]['version'] = 3
with open('plugin.json', 'w', encoding='utf-8') as f:
    json.dump(repo_data, f, indent=2, ensure_ascii=False)

# Update version in extension plugin.json
with open('truyenc/plugin.json', 'r', encoding='utf-8') as f:
    ext_data = json.load(f)
ext_data['metadata']['version'] = 3
with open('truyenc/plugin.json', 'w', encoding='utf-8') as f:
    json.dump(ext_data, f, indent=2, ensure_ascii=False)

# Repackage zip
if os.path.exists('truyenc/plugin.zip'):
    os.remove('truyenc/plugin.zip')
with zipfile.ZipFile('truyenc/plugin.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk('truyenc'):
        if 'plugin.zip' in files:
            files.remove('plugin.zip')
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, 'truyenc')
            zf.write(file_path, arcname)

print(f"Added {len(genres)} categories and updated version to 3")
