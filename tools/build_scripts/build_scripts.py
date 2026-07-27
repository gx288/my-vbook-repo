import os
import json

js_home = '''function execute() {
    return Response.success([
        {title: "Trang chủ", input: "https://truyenc.com", script: "gen.js"},
        {title: "Truyện 18+", input: "https://truyenc.com/tim-truyen-18", script: "gen.js"},
        {title: "Truyện ma", input: "https://truyenc.com/tim-truyen-ma", script: "gen.js"}
    ]);
}'''

js_genre = '''function execute() {
    return Response.success([
        {title: "Truyện ma", input: "https://truyenc.com/tim-truyen-ma", script: "gen.js"},
        {title: "Truyện 18+", input: "https://truyenc.com/tim-truyen-18", script: "gen.js"},
        {title: "Truyện cười", input: "https://truyenc.com/tim-truyen-cuoi", script: "gen.js"},
        {title: "Truyện audio", input: "https://truyenc.com/tim-truyen-audio", script: "gen.js"},
        {title: "Chưa phân loại", input: "https://truyenc.com/tim-truyen-chua-phan-loai", script: "gen.js"}
    ]);
}'''

js_gen = '''function execute(url, page) {
    if (!page) page = '1';
    
    var finalUrl = url;
    if (url.indexOf('?') !== -1) {
        finalUrl = url + '&page=' + page;
    } else {
        finalUrl = url + '?page=' + page;
    }

    var doc = Http.get(finalUrl).html();
    var els = doc.select('.d-flex');
    var list = [];
    
    for (var i = 0; i < els.size(); i++) {
        var e = els.get(i);
        var titleEl = e.select('h2');
        if (titleEl.size() > 0) {
            var title = titleEl.first().text().trim();
            var linkEl = e.select('a.btn');
            if (linkEl.size() === 0) {
                linkEl = e.select('.mr-3 a');
            }
            if (linkEl.size() > 0) {
                var link = linkEl.first().attr('href');
                var cover = e.select('.mr-3 img').first().attr('src');
                var desc = e.select('p.mt-2').text();
                
                if (link.indexOf('http') === -1) {
                    link = 'https://truyenc.com' + link;
                }
                
                list.push({
                    name: title,
                    link: link,
                    cover: cover,
                    description: desc,
                    host: 'https://truyenc.com'
                });
            }
        }
    }
    
    var next = (parseInt(page) + 1).toString();
    var hasNext = doc.select('.pagination a[aria-label="Trang sau"]').size() > 0 || doc.select('.pagination a.page-link').text().indexOf(next) !== -1;
    if (!hasNext && list.length === 0) {
        next = '';
    } else if (list.length > 0 && doc.select('.pagination').size() === 0) {
        next = '';
    } else if (list.length === 0) {
        next = '';
    }
    
    return Response.success(list, next);
}'''

js_detail = '''function execute(url) {
    var doc = Http.get(url).html();
    var title = doc.select("h2").first().text().replace("Truyện ", "").trim();
    var author = doc.select("h3.h6").text().replace("Tác giả:", "").trim();
    var cover = doc.select("img.fluid-img").attr("src");
    
    var paragraphs = doc.select("p");
    var desc = "";
    for (var i = 0; i < paragraphs.size(); i++) {
        var pText = paragraphs.get(i).text().trim();
        if (pText.length > 50 && pText.indexOf("Tình trạng:") === -1 && pText.indexOf("Mới nhất:") === -1) {
            desc = pText;
            break;
        }
    }
    
    return Response.success({
        name: title,
        cover: cover,
        author: author,
        description: desc,
        detail: "Tác giả: " + author,
        host: "https://truyenc.com"
    });
}'''

js_toc = '''function execute(url) {
    var doc = Http.get(url).html();
    var els = doc.select(".story-chapters-main a");
    var list = [];
    
    for (var i = 0; i < els.size(); i++) {
        var e = els.get(i);
        var link = e.attr("href");
        if (link && link.indexOf("/truyen/") !== -1) {
            if (link.indexOf("http") === -1) {
                link = "https://truyenc.com" + link;
            }
            var name = e.text().trim();
            if (name !== "Đọc truyện" && name !== "") {
                list.push({
                    name: name,
                    url: link,
                    host: "https://truyenc.com"
                });
            }
        }
    }
    
    if (list.length === 0) {
        els = doc.select("a");
        for (var i = 0; i < els.size(); i++) {
            var e = els.get(i);
            var link = e.attr("href");
            if (link && link.indexOf("/truyen/") !== -1 && link.indexOf("/chuong-") === -1 && link.indexOf("/phan-") !== -1) {
                var name = e.text().trim();
                if (name !== "Đọc truyện" && name !== "") {
                    if (link.indexOf("http") === -1) {
                        link = "https://truyenc.com" + link;
                    }
                    var exists = false;
                    for (var j=0; j<list.length; j++) { if(list[j].url === link) exists = true; }
                    if (!exists) {
                        list.push({
                            name: name,
                            url: link,
                            host: "https://truyenc.com"
                        });
                    }
                }
            }
        }
    }
    
    return Response.success(list);
}'''

js_chap = '''function execute(url) {
    var doc = Http.get(url).html();
    var content = doc.select(".story-content");
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
    var doc = Http.get("https://truyenc.com/tim-kiem?q=" + key + "&page=" + page).html();
    var els = doc.select('.d-flex');
    var list = [];
    
    for (var i = 0; i < els.size(); i++) {
        var e = els.get(i);
        var titleEl = e.select('h2');
        if (titleEl.size() > 0) {
            var title = titleEl.first().text().trim();
            var linkEl = e.select('a.btn');
            if (linkEl.size() === 0) {
                linkEl = e.select('.mr-3 a');
            }
            if (linkEl.size() > 0) {
                var link = linkEl.first().attr('href');
                var cover = e.select('.mr-3 img').first().attr('src');
                var desc = e.select('p.mt-2').text();
                
                if (link.indexOf('http') === -1) {
                    link = 'https://truyenc.com' + link;
                }
                list.push({
                    name: title,
                    link: link,
                    cover: cover,
                    description: desc,
                    host: 'https://truyenc.com'
                });
            }
        }
    }
    
    var next = (parseInt(page) + 1).toString();
    var hasNext = doc.select('.pagination a[aria-label="Trang sau"]').size() > 0 || doc.select('.pagination a.page-link').text().indexOf(next) !== -1;
    if (!hasNext) next = '';
    
    return Response.success(list, next);
}'''

base_dir = 'truyenc/src'
with open(os.path.join(base_dir, 'home.js'), 'w', encoding='utf-8') as f: f.write(js_home)
with open(os.path.join(base_dir, 'genre.js'), 'w', encoding='utf-8') as f: f.write(js_genre)
with open(os.path.join(base_dir, 'gen.js'), 'w', encoding='utf-8') as f: f.write(js_gen)
with open(os.path.join(base_dir, 'detail.js'), 'w', encoding='utf-8') as f: f.write(js_detail)
with open(os.path.join(base_dir, 'toc.js'), 'w', encoding='utf-8') as f: f.write(js_toc)
with open(os.path.join(base_dir, 'chap.js'), 'w', encoding='utf-8') as f: f.write(js_chap)
with open(os.path.join(base_dir, 'search.js'), 'w', encoding='utf-8') as f: f.write(js_search)

import zipfile
import os
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
