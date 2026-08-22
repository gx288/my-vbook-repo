function execute(url, page) {
    if (!page) page = '1';
    
    var fetchUrl = url;
    if (page !== '1') {
        if (url.indexOf('?') !== -1) {
            var parts = url.split('?');
            fetchUrl = parts[0] + "page/" + page + "/?" + parts[1];
        } else {
            fetchUrl = url + (url.endsWith('/') ? "" : "/") + "page/" + page + "/";
        }
    }
    
    var doc = Http.get(fetchUrl).html();
    var els = doc.select(".page-item-detail");
    if (els.size() === 0) els = doc.select(".item");
    if (els.size() === 0) els = doc.select("article");
    
    var list = [];
    for (var i = 0; i < els.size(); i++) {
        var e = els.get(i);
        var a = e.select("a").first();
        var img = e.select("img").first();
        if (a && img) {
            var link = a.attr("href");
            if (link.indexOf("http") === -1) {
                link = "https://hentaivn.casa" + link;
            }
            var cover = img.attr("data-src");
            if (!cover) cover = img.attr("src");
            
            var desc = "";
            var chapterSpan = e.select(".chapter, .episode, .status, .viewsCount span").first();
            if (chapterSpan) {
                desc = chapterSpan.text().trim();
            }
            
            list.push({
                name: a.attr("title") || a.text().trim(),
                link: link,
                cover: cover,
                description: desc,
                host: "https://hentaivn.casa"
            });
        }
    }
    
    var next = "";
    if (list.length > 0) {
        next = (parseInt(page) + 1).toString();
    }
    
    return Response.success(list, next);
}
