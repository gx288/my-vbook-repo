import os
import zipfile

# Create dir
os.makedirs('sayhentai/src', exist_ok=True)

# Write files
with open('sayhentai/plugin.json', 'w', encoding='utf-8') as f:
    f.write('''{
  "metadata": {
    "name": "SayHentai",
    "author": "Antigravity",
    "version": 1,
    "source": "https://sayhentai.cfd",
    "regexp": ".*sayhentai\\\\.cfd.*",
    "description": "Đọc truyện tranh hentai trên SayHentai",
    "local": "vi",
    "type": "comic",
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
}''')

with open('sayhentai/src/home.js', 'w', encoding='utf-8') as f:
    f.write('''function execute() {
    return Response.success([
        {title: "Mới cập nhật", input: "https://sayhentai.cfd/", script: "gen.js"}
    ]);
}''')

with open('sayhentai/src/gen.js', 'w', encoding='utf-8') as f:
    f.write('''function execute(url, page) {
    if (!page) page = '1';
    
    var fetchUrl = url;
    if (page !== '1') {
        if (fetchUrl.indexOf('?') !== -1) {
            fetchUrl = fetchUrl + "&page=" + page;
        } else {
            fetchUrl = fetchUrl + "?page=" + page;
        }
    }
    
    var doc = Http.get(fetchUrl).html();
    var els = doc.select(".item");
    if (els.size() === 0) {
        els = doc.select("article");
    }
    
    var list = [];
    for (var i = 0; i < els.size(); i++) {
        var e = els.get(i);
        var a = e.select("a").first();
        var img = e.select("img").first();
        if (a && img) {
            var link = a.attr("href");
            if (link.indexOf("http") === -1) {
                link = "https://sayhentai.cfd" + link;
            }
            var cover = img.attr("data-src");
            if (!cover) cover = img.attr("src");
            
            list.push({
                name: a.attr("title") || a.text().trim(),
                link: link,
                cover: cover,
                description: "",
                host: "https://sayhentai.cfd"
            });
        }
    }
    
    var next = "";
    if (list.length > 0) {
        next = (parseInt(page) + 1).toString();
    }
    
    return Response.success(list, next);
}''')

with open('sayhentai/src/detail.js', 'w', encoding='utf-8') as f:
    f.write('''function execute(url) {
    var doc = Http.get(url).html();
    
    var title = doc.select("h1").text().trim();
    if (!title) title = doc.select(".post-title h1").text().trim();
    
    var cover = doc.select(".info-image img").attr("src");
    if (!cover) cover = doc.select(".summary_image img").attr("src");
    
    var author = doc.select(".author-content").text().trim();
    if (!author) author = "Đang cập nhật";
    
    var desc = doc.select(".summary__content").text().trim();
    if (!desc) desc = doc.select(".description-summary").text().trim();
    
    var genres = [];
    var genreEls = doc.select(".genres-content a");
    for (var i = 0; i < genreEls.size(); i++) {
        var g = genreEls.get(i);
        genres.push({
            title: g.text().trim(),
            link: g.attr("href")
        });
    }
    
    return Response.success({
        name: title,
        cover: cover,
        author: author,
        description: desc,
        genres: genres,
        detail: "Tác giả: " + author,
        host: "https://sayhentai.cfd"
    });
}''')

with open('sayhentai/src/toc.js', 'w', encoding='utf-8') as f:
    f.write('''function execute(url) {
    var doc = Http.get(url).html();
    
    var els = doc.select(".chapter a");
    if (els.size() === 0) {
        els = doc.select(".wp-manga-chapter a");
    }
    if (els.size() === 0) {
        els = doc.select(".list-chapter a");
    }
    
    var list = [];
    for (var i = els.size() - 1; i >= 0; i--) {
        var e = els.get(i);
        var link = e.attr("href");
        if (link.indexOf("http") === -1) {
            link = "https://sayhentai.cfd" + link;
        }
        var name = e.select(".chap-name").text().trim();
        if (!name) name = e.text().trim();
        
        list.push({
            name: name,
            url: link,
            host: "https://sayhentai.cfd"
        });
    }
    
    return Response.success(list);
}''')

with open('sayhentai/src/chap.js', 'w', encoding='utf-8') as f:
    f.write('''function execute(url) {
    var doc = Http.get(url).html();
    
    var imgs = doc.select(".imageload img");
    if (imgs.size() === 0) {
        imgs = doc.select(".page-chapter img");
    }
    if (imgs.size() === 0) {
        imgs = doc.select(".reading-content img");
    }
    if (imgs.size() === 0) {
        imgs = doc.select("#chapter-content img");
    }
    
    var list = [];
    for (var i = 0; i < imgs.size(); i++) {
        var e = imgs.get(i);
        var imgUrl = e.attr("data-src");
        if (!imgUrl) imgUrl = e.attr("src");
        if (!imgUrl) imgUrl = e.attr("data-original");
        
        if (imgUrl) {
            // Loại bỏ khoảng trắng
            imgUrl = imgUrl.trim();
            list.push(imgUrl);
        }
    }
    
    return Response.success(list);
}''')

with open('sayhentai/src/genre.js', 'w', encoding='utf-8') as f:
    f.write('''function execute() {
    var doc = Http.get("https://sayhentai.cfd/").html();
    var els = doc.select(".genres a, .the-loai a, .category a, ul.submenu li a");
    if (els.size() === 0) {
        var allLinks = doc.select("a");
        for (var i = 0; i < allLinks.size(); i++) {
            var href = allLinks.get(i).attr("href");
            if (href && href.indexOf("/the-loai/") !== -1) {
                els.add(allLinks.get(i));
            }
        }
    }
    
    var list = [];
    var added = {};
    for (var i = 0; i < els.size(); i++) {
        var e = els.get(i);
        var title = e.text().trim();
        var link = e.attr("href");
        if (title && link && !added[title]) {
            added[title] = true;
            if (link.indexOf("http") === -1) {
                link = "https://sayhentai.cfd" + link;
            }
            list.push({
                title: title,
                input: link,
                script: "gen.js"
            });
        }
    }
    return Response.success(list);
}''')

with open('sayhentai/src/search.js', 'w', encoding='utf-8') as f:
    f.write('''function execute(key, page) {
    if (!page) page = '1';
    
    var fetchUrl = "https://sayhentai.cfd/?s=" + encodeURIComponent(key);
    if (page !== '1') {
        fetchUrl += "&page=" + page;
    }
    
    var doc = Http.get(fetchUrl).html();
    var els = doc.select(".item");
    if (els.size() === 0) {
        els = doc.select("article");
    }
    
    var list = [];
    for (var i = 0; i < els.size(); i++) {
        var e = els.get(i);
        var a = e.select("a").first();
        var img = e.select("img").first();
        if (a && img) {
            var link = a.attr("href");
            if (link.indexOf("http") === -1) {
                link = "https://sayhentai.cfd" + link;
            }
            var cover = img.attr("data-src");
            if (!cover) cover = img.attr("src");
            
            list.push({
                name: a.attr("title") || a.text().trim(),
                link: link,
                cover: cover,
                description: "",
                host: "https://sayhentai.cfd"
            });
        }
    }
    
    var next = "";
    if (list.length > 0) {
        next = (parseInt(page) + 1).toString();
    }
    
    return Response.success(list, next);
}''')

print("Created all files for sayhentai")

