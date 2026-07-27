import os
import json
import urllib.request
import zipfile

# 1. Create directories
os.makedirs('dasactruyen/src', exist_ok=True)

# 2. Download icon
try:
    urllib.request.urlretrieve('https://dasactruyen.com/favicon.ico', 'dasactruyen/icon.png')
except:
    pass

# 3. Write JS files
js_home = '''function execute() {
    return Response.success([
        {title: "Mới cập nhật", input: "https://dasactruyen.com/index.php/danh-sach-truyen/", script: "gen.js"},
        {title: "Đã hoàn thành", input: "https://dasactruyen.com/index.php/trang_thai/da-hoan-thanh/", script: "gen.js"}
    ]);
}'''

js_genre = '''function execute() {
    return Response.success([
        {title: "Bách hợp", input: "https://dasactruyen.com/index.php/the_loai/bach-hop/", script: "gen.js"},
        {title: "Idol", input: "https://dasactruyen.com/index.php/the_loai/idol/", script: "gen.js"},
        {title: "Nam", input: "https://dasactruyen.com/index.php/the_loai/nam/", script: "gen.js"},
        {title: "Femdom", input: "https://dasactruyen.com/index.php/the_loai/femdom/", script: "gen.js"},
        {title: "Harem", input: "https://dasactruyen.com/index.php/the_loai/harem/", script: "gen.js"},
        {title: "Incenst", input: "https://dasactruyen.com/index.php/the_loai/incenst/", script: "gen.js"},
        {title: "Dân Quốc", input: "https://dasactruyen.com/index.php/the_loai/dan-quoc/", script: "gen.js"},
        {title: "Ngôn tình", input: "https://dasactruyen.com/index.php/the_loai/ngon-tinh/", script: "gen.js"},
        {title: "Hệ Thống", input: "https://dasactruyen.com/index.php/the_loai/he-thong/", script: "gen.js"}
    ]);
}'''

js_gen = '''function execute(url, page) {
    if (!page) page = '1';
    
    var finalUrl = url;
    if (page !== '1') {
        if (finalUrl.indexOf('?') !== -1) {
            finalUrl = finalUrl + '&page=' + page;
        } else {
            // Check if it already has trailing slash
            if (finalUrl.slice(-1) !== '/') finalUrl += '/';
            finalUrl = finalUrl + 'page/' + page + '/';
        }
    }

    var doc = Http.get(finalUrl).html();
    var els = doc.select('.box-full-right-item, .item-comic, .col-6.col-md-3, article.card-custom');
    var list = [];
    
    for (var i = 0; i < els.size(); i++) {
        var e = els.get(i);
        var linkEl = e.select('a').first();
        if (linkEl.size() > 0) {
            var link = linkEl.attr('href');
            var title = '';
            
            var titleEl = e.select('.box-full-right-title');
            if (titleEl.size() > 0) {
                title = titleEl.first().text().trim();
            }
            if (title === '') {
                titleEl = e.select('h2.entry-title');
                if (titleEl.size() > 0) title = titleEl.first().text().trim();
            }
            if (title === '') {
                title = e.select('img').attr('alt').trim();
            }
            if (title === '') title = 'Không rõ tên';

            var cover = e.select('img').attr('src');
            
            if (link.indexOf('http') === -1) {
                link = 'https://dasactruyen.com' + link;
            }
            
            list.push({
                name: title,
                link: link,
                cover: cover,
                description: '',
                host: 'https://dasactruyen.com'
            });
        }
    }
    
    var next = (parseInt(page) + 1).toString();
    var hasNext = doc.select('a.next.page-numbers').size() > 0;
    if (!hasNext) {
        next = '';
    }
    
    return Response.success(list, next);
}'''

js_detail = '''function execute(url) {
    var doc = Http.get(url).html();
    var title = doc.select("h1.entry-title").first().text().trim();
    if (!title || title === "Đăng nhập") {
        title = doc.select("title").text().split("-")[0].trim();
    }
    
    var authorEl = doc.select(".item-author a");
    var author = "Chưa cập nhật";
    if (authorEl.size() > 0) {
        author = authorEl.first().text().trim();
    } else {
        var a2 = doc.select("div.author");
        if (a2.size() > 0) {
            author = a2.first().text().replace("Tác giả:", "").trim();
        }
    }
    
    var cover = doc.select("img.img-fluid").first().attr("src");
    if (!cover) {
        cover = doc.select("div.comic-image img").attr("src");
    }
    
    var descEl = doc.select(".entry-content, .comic-description").first();
    var desc = "";
    if (descEl.size() > 0) {
        desc = descEl.text().trim();
    }
    
    return Response.success({
        name: title,
        cover: cover,
        author: author,
        description: desc,
        detail: "Tác giả: " + author,
        host: "https://dasactruyen.com"
    });
}'''

js_toc = '''function execute(url) {
    var doc = Http.get(url).html();
    var els = doc.select("ul.chapter-list-ul li a");
    var list = [];
    
    if (els.size() === 0) {
        els = doc.select("a");
    }
    
    for (var i = 0; i < els.size(); i++) {
        var e = els.get(i);
        var link = e.attr("href");
        if (link && link.indexOf("/chuong") !== -1) {
            var name = e.text().trim();
            if (name !== "Đọc Từ Đầu" && name !== "") {
                if (link.indexOf("http") === -1) {
                    link = "https://dasactruyen.com" + link;
                }
                var exists = false;
                for (var j=0; j<list.length; j++) { if(list[j].url === link) exists = true; }
                if (!exists) {
                    list.push({
                        name: name,
                        url: link,
                        host: "https://dasactruyen.com"
                    });
                }
            }
        }
    }
    
    // Sort array by chapter name (e.g., "Chương 1", "Chương 2") if they are backwards
    // Often wordpress outputs desc.
    if (list.length > 1) {
        // Just reverse if first chapter name has bigger number than last
        // Simplest way is to just let vBook handle it, but if it's strictly backward:
        var first = list[0].name;
        var last = list[list.length-1].name;
        // Basic check
        if (first.indexOf("Chương") !== -1 && last.indexOf("Chương") !== -1) {
            var numFirst = parseInt(first.replace(/\\D/g, ""));
            var numLast = parseInt(last.replace(/\\D/g, ""));
            if (numFirst > numLast) {
                list.reverse();
            }
        } else {
             // force reverse because wordpress usually desc
             list.reverse();
        }
    }
    
    return Response.success(list);
}'''

js_chap = '''function execute(url) {
    var doc = Http.get(url).html();
    var content = doc.select(".entry-content, .chapter-content, .story-content");
    content.select("script").remove();
    content.select("iframe").remove();
    content.select("a").remove();
    
    var html = content.html();
    if (!html) html = "Không lấy được nội dung chương. Hoặc nội dung bị khóa.";
    html = html.replace(/&nbsp;/g, " ");

    return Response.success(html);
}'''

js_search = '''function execute(key, page) {
    if (!page) page = '1';
    var finalUrl = "https://dasactruyen.com/?s=" + key;
    if (page !== '1') {
        finalUrl = "https://dasactruyen.com/page/" + page + "/?s=" + key;
    }
    
    var doc = Http.get(finalUrl).html();
    var els = doc.select('article');
    var list = [];
    
    for (var i = 0; i < els.size(); i++) {
        var e = els.get(i);
        var linkEl = e.select('a').first();
        if (linkEl.size() > 0) {
            var link = linkEl.attr('href');
            var title = '';
            var titleEl = e.select('h2.entry-title');
            if (titleEl.size() > 0) {
                title = titleEl.first().text().trim();
            } else {
                title = e.select('img').attr('alt').trim();
            }
            if (!title) title = 'Không rõ tên';
            
            var cover = e.select('img').attr('src');
            if (link.indexOf('http') === -1) {
                link = 'https://dasactruyen.com' + link;
            }
            list.push({
                name: title,
                link: link,
                cover: cover,
                description: '',
                host: 'https://dasactruyen.com'
            });
        }
    }
    
    var next = (parseInt(page) + 1).toString();
    var hasNext = doc.select('a.next.page-numbers').size() > 0;
    if (!hasNext) next = '';
    
    return Response.success(list, next);
}'''

# Write scripts
base_dir = 'dasactruyen/src'
with open(os.path.join(base_dir, 'home.js'), 'w', encoding='utf-8') as f: f.write(js_home)
with open(os.path.join(base_dir, 'genre.js'), 'w', encoding='utf-8') as f: f.write(js_genre)
with open(os.path.join(base_dir, 'gen.js'), 'w', encoding='utf-8') as f: f.write(js_gen)
with open(os.path.join(base_dir, 'detail.js'), 'w', encoding='utf-8') as f: f.write(js_detail)
with open(os.path.join(base_dir, 'toc.js'), 'w', encoding='utf-8') as f: f.write(js_toc)
with open(os.path.join(base_dir, 'chap.js'), 'w', encoding='utf-8') as f: f.write(js_chap)
with open(os.path.join(base_dir, 'search.js'), 'w', encoding='utf-8') as f: f.write(js_search)

# Write plugin.json for dasactruyen
ext_json = {
  "metadata": {
    "name": "Dạ Sắc Truyện",
    "author": "Antigravity",
    "version": 1,
    "source": "https://dasactruyen.com",
    "regexp": "dasactruyen\\\\.com",
    "description": "Đọc truyện trên Dạ Sắc Truyện",
    "local": "vi",
    "type": "novel",
    "locale": "vi_VN"
  },
  "script": {
    "home": "home.js",
    "detail": "detail.js",
    "toc": "toc.js",
    "chap": "chap.js",
    "genre": "genre.js",
    "search": "search.js"
  }
}
with open('dasactruyen/plugin.json', 'w', encoding='utf-8') as f:
    json.dump(ext_json, f, indent=2, ensure_ascii=False)

# Package Zip
if os.path.exists('dasactruyen/plugin.zip'):
    os.remove('dasactruyen/plugin.zip')
with zipfile.ZipFile('dasactruyen/plugin.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk('dasactruyen'):
        if 'plugin.zip' in files:
            files.remove('plugin.zip')
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, 'dasactruyen')
            zf.write(file_path, arcname)

# Update root plugin.json
with open('plugin.json', 'r', encoding='utf-8') as f:
    repo_data = json.load(f)

# Update existing version to 4
for item in repo_data['data']:
    item['version'] = 4

# Check if dasactruyen exists
exists = False
for item in repo_data['data']:
    if item['name'] == "Dạ Sắc Truyện":
        exists = True
        break
if not exists:
    repo_data['data'].append({
      "name": "Dạ Sắc Truyện",
      "author": "Antigravity",
      "version": 4,
      "source": "https://dasactruyen.com",
      "regexp": "dasactruyen\\\\.com",
      "description": "Đọc truyện trên Dạ Sắc Truyện",
      "local": "vi",
      "type": "novel",
      "locale": "vi_VN",
      "path": "https://cdn.jsdelivr.net/gh/gx288/my-vbook-repo@master/dasactruyen/plugin.zip",
      "icon": "https://cdn.jsdelivr.net/gh/gx288/my-vbook-repo@master/dasactruyen/icon.png"
    })

with open('plugin.json', 'w', encoding='utf-8') as f:
    json.dump(repo_data, f, indent=2, ensure_ascii=False)

print("Build complete for dasactruyen!")
