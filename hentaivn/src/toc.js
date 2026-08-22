function execute(url) {
    var doc = Http.get(url).html();
    var mangaId = doc.select("#manga-chapters-holder").attr("data-id");
    
    if (mangaId) {
        doc = Http.post("https://hentaivn.casa/wp-admin/admin-ajax.php")
                  .params({
                      "action": "manga_get_chapters",
                      "manga": mangaId
                  }).html();
    }
    
    var els = doc.select(".wp-manga-chapter a");
    if (els.size() === 0) {
        els = doc.select(".chapter a");
    }
    if (els.size() === 0) {
        els = doc.select(".list-chapter a");
    }
    
    var list = [];
    for (var i = els.size() - 1; i >= 0; i--) {
        var e = els.get(i);
        var link = e.attr("href");
        if (link.indexOf("http") === -1) {
            link = "https://hentaivn.casa" + link;
        }
        var name = e.select(".chap-name").text().trim();
        if (!name) name = e.text().trim();
        
        list.push({
            name: name,
            url: link,
            host: "https://hentaivn.casa"
        });
    }
    
    return Response.success(list);
}
