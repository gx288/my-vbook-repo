function execute() {
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
}