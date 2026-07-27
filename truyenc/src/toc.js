function execute(url) {
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
}