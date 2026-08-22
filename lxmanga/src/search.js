function execute(key, page) {
    if (!page) page = '1';
    
    var fetchUrl = "https://www.lxmanga.quest/?s=" + encodeURIComponent(key) + "&post_type=wp-manga";
    if (page !== '1') {
        fetchUrl = "https://www.lxmanga.quest/page/" + page + "/?s=" + encodeURIComponent(key) + "&post_type=wp-manga";
    }
    
    var doc = Http.get(fetchUrl).html();
    var els = doc.select(".page-item-detail");
    if (els.size() === 0) els = doc.select(".c-tabs-item__content");
    if (els.size() === 0) els = doc.select("article");
    
    var list = [];
    for (var i = 0; i < els.size(); i++) {
        var e = els.get(i);
        var a = e.select("h3 a, .post-title h3 a, h4 a, .post-title h4 a, a").first();
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
