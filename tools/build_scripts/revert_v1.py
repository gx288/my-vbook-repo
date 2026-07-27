import json
import os
import zipfile

# Revert toc.js to EXACTLY V1
toc_js = '''function execute(url) {
    var doc = Http.get(url).html();
    var els = doc.select(".story-chap-item");
    var list = [];
    for (var i = 0; i < els.size(); i++) {
        var e = els.get(i);
        var link = e.attr("href");
        if (link.indexOf("http") === -1) {
            link = "https://truyenc.com" + link;
        }
        list.push({
            name: e.select(".story-chap-name").text().trim(),
            url: link,
            host: "https://truyenc.com"
        });
    }
    return Response.success(list);
}'''

with open('truyenc/src/toc.js', 'w', encoding='utf-8') as f:
    f.write(toc_js)

# Revert chap.js to EXACTLY V1
chap_js = '''function execute(url) {
    var doc = Http.get(url).html();
    var content = doc.select(".story-content");
    content.select("script").remove();
    content.select("iframe").remove();
    content.select("a").remove();
    
    var html = content.html();
    
    // Clean up unnecessary things if any
    html = html.replace(/&nbsp;/g, " ");

    return Response.success(html);
}'''

with open('truyenc/src/chap.js', 'w', encoding='utf-8') as f:
    f.write(chap_js)

# Bump version to 8
def bump_and_repack():
    ext_dir = 'truyenc'
    json_path = os.path.join(ext_dir, 'plugin.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data['metadata']['version'] = 8
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

bump_and_repack()

# Bump root plugin.json version
with open('plugin.json', 'r', encoding='utf-8') as f:
    repo_data = json.load(f)

for item in repo_data['data']:
    item['version'] = 8

with open('plugin.json', 'w', encoding='utf-8') as f:
    json.dump(repo_data, f, indent=2, ensure_ascii=False)
