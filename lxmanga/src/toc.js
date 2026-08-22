function execute(url) {
    var doc = Http.get(url).html();
    
    var mangaId = doc.select("#manga-chapters-holder").attr("data-id");
    if (!mangaId) mangaId = doc.select(".rating-post-id").attr("value");
    if (!mangaId) mangaId = doc.select("#wp-manga-review-manga-id").attr("value");
    
    var els = doc.select(".wp-manga-chapter a");
    
    if (els.size() === 0 && mangaId) {
        var res = Http.post("https://www.lxmanga.quest/wp-admin/admin-ajax.php").params({
            "action": "manga_get_chapters",
            "manga": mangaId
        }).html();
        
        els = res.select(".wp-manga-chapter a");
        if (els.size() === 0) els = res.select("li.wp-manga-chapter a");
    }
    
    // Fallback if still empty, try to get from init-links
    if (els.size() === 0) {
        els = doc.select("#init-links a");
    }
    
    var list = [];
    for (var i = els.size() - 1; i >= 0; i--) {
        var e = els.get(i);
        var link = e.attr("href");
        if (link.indexOf("http") === -1) {
            link = "https://www.lxmanga.quest" + link;
        }
        var name = e.text().trim();
        // Avoid duplicate oneshot links if they use multiple buttons
        var isDuplicate = false;
        for (var j = 0; j < list.length; j++) {
            if (list[j].url === link) {
                isDuplicate = true;
                break;
            }
        }
        if (!isDuplicate) {
            list.push({
                name: name,
                url: link,
                host: "https://www.lxmanga.quest"
            });
        }
    }
    
    return Response.success(list);
}
