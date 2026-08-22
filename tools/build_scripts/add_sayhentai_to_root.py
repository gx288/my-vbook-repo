import json
import os

with open('plugin.json', 'r', encoding='utf-8') as f:
    root_data = json.load(f)

# check if SayHentai is in data
found = False
for item in root_data['data']:
    if item['name'] == 'SayHentai':
        found = True
        break

if not found:
    with open('sayhentai/plugin.json', 'r', encoding='utf-8') as f:
        say_data = json.load(f)
        
    ext_info = say_data['metadata']
    ext_info['path'] = "https://raw.githack.com/gx288/my-vbook-repo/main/sayhentai/plugin.zip"
    ext_info['icon'] = "https://raw.githack.com/gx288/my-vbook-repo/main/sayhentai/icon.png"
    
    root_data['data'].append(ext_info)
    
    with open('plugin.json', 'w', encoding='utf-8') as f:
        json.dump(root_data, f, indent=2, ensure_ascii=False)
    print("Added SayHentai to plugin.json")
else:
    print("Already in plugin.json")
