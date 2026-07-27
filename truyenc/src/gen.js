function execute(url, page) {
    if (!page) page = '1';
    var doc = Http.get(url + "?page=" + page).html();
    var el = doc.select(".card-full-left, .item-comic, .card");
    var novelList = [];
    for (var i = 0; i < el.size(); i++) {
        var e = el.get(i);
        var a = e.select("a").first();
        var img = e.select("img").first();
        if (a && img) {
            var title = a.attr("title") || img.attr("alt") || a.text();
            var link = a.attr("href");
            var cover = img.attr("src") || img.attr("data-src");
            if (link.indexOf("http") === -1) {
                link = "https://truyenc.com" + link;
            }
            novelList.push({
                name: title,
                link: link,
                cover: cover,
                description: "",
                host: "https://truyenc.com"
            });
        }
    }
    var next = parseInt(page) + 1;
    return Response.success(novelList, next.toString());
}
