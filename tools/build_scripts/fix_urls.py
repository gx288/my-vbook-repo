import json

with open('plugin.json', 'r', encoding='utf-8') as f:
    repo_data = json.load(f)

for item in repo_data['data']:
    if 'jsdelivr.net' in item['path']:
        item['path'] = item['path'].replace('cdn.jsdelivr.net/gh/gx288/my-vbook-repo@master', 'raw.githack.com/gx288/my-vbook-repo/master')
        item['icon'] = item['icon'].replace('cdn.jsdelivr.net/gh/gx288/my-vbook-repo@master', 'raw.githack.com/gx288/my-vbook-repo/master')
        # Ensure version is bumped to 5 to trigger vBook update
        item['version'] = 5

with open('plugin.json', 'w', encoding='utf-8') as f:
    json.dump(repo_data, f, indent=2, ensure_ascii=False)
