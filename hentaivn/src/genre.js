function execute() {
    var doc = Http.get("https://hentaivn.casa/").html();
    var allLinks = doc.select("a");
    
    var list = [];
    var added = {};
    for (var i = 0; i < allLinks.size(); i++) {
        var e = allLinks.get(i);
        var href = e.attr("href");
        if (href && href.indexOf("/the-loai/") !== -1) {
            var title = e.text().trim();
            // Bỏ qua các thể loại rác hoặc trùng
            if (title && !added[title] && title.indexOf("img") === -1) {
                added[title] = true;
                if (href.indexOf("http") === -1) {
                    href = "https://hentaivn.casa" + href;
                }
                list.push({
                    title: title,
                    input: href,
                    script: "gen.js"
                });
            }
        }
    }
    return Response.success(list);
}