import json

with open('plugin.json', 'r', encoding='utf-8') as f:
    repo_data = json.load(f)

for item in repo_data['data']:
    item['path'] = item['path'].replace('/master/', '/main/')
    item['icon'] = item['icon'].replace('/master/', '/main/')

with open('plugin.json', 'w', encoding='utf-8') as f:
    json.dump(repo_data, f, indent=2, ensure_ascii=False)
