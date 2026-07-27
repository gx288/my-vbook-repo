import json
import os

with open('plugin.json', 'r', encoding='utf-8') as f:
    repo_data = json.load(f)

repo_data['data'][0]['path'] = "https://cdn.jsdelivr.net/gh/gx288/my-vbook-repo@master/truyenc/plugin.zip"
repo_data['data'][0]['icon'] = "https://cdn.jsdelivr.net/gh/gx288/my-vbook-repo@master/truyenc/icon.png"

with open('plugin.json', 'w', encoding='utf-8') as f:
    json.dump(repo_data, f, indent=2, ensure_ascii=False)
