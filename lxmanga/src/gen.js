function execute(url, page) {
    if (!page) page = '1';
    
    var fetchUrl = url;
    if (page !== '1') {
        if (fetchUrl.indexOf("?") !== -1) {
            // It has parameters, we might need to insert /page/ before it, or just use ?page=
            // But from tests, Madara uses /page/2/
            var parts = fetchUrl.split("?");
            if (parts[0].endsWith("/")) {
                fetchUrl = parts[0] + "page/" + page + "/?" + parts[1];
            } else {
                fetchUrl = parts[0] + "/page/" + page + "/?" + parts[1];
            }
        } else {
            if (fetchUrl.endsWith("/")) {
                fetchUrl = fetchUrl + "page/" + page + "/";
            } else {
                fetchUrl = fetchUrl + "/page/" + page + "/";
            }
        }
    }
    
    var doc = Http.get(fetchUrl).html();
    var els = doc.select(".page-item-detail");
    if (els.size() === 0) els = doc.select("article");
    if (els.size() === 0) els = doc.select(".item");
    
    var list = [];
    for (var i = 0; i < els.size(); i++) {
        var e = els.get(i);
        var a = e.select("a").first();
        var img = e.select("img").first();
        if (a && img) {
            var link = a.attr("href");
            if (link.indexOf("http") === -1) {
                link = "https://www.lxmanga.quest" + link;
            }
            var cover = img.attr("data-src");
            if (!cover) cover = img.attr("src");
            
            var desc = "";
            var chapterSpan = e.select(".chapter, .episode, .chapter-item, .font-none").first();
            if (!chapterSpan) chapterSpan = e.select(".status").first();
            if (chapterSpan) {
                desc = chapterSpan.text().trim();
            }
            
            list.push({
                name: a.attr("title") || a.text().trim(),
                link: link,
                cover: cover,
                description: desc,
                host: "https://www.lxmanga.quest"
            });
        }
    }
    
    var next = "";
    if (list.length > 0) {
        next = (parseInt(page) + 1).toString();
    }
    
    return Response.success(list, next);
}
