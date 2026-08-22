import os

with open('sayhentai/src/genre.js', 'w', encoding='utf-8') as f:
    f.write('''function execute() {
    var doc = Http.get("https://sayhentai.cfd/").html();
    var allLinks = doc.select("a");
    
    var list = [];
    var added = {};
    for (var i = 0; i < allLinks.size(); i++) {
        var e = allLinks.get(i);
        var href = e.attr("href");
        if (href && href.indexOf("/the-loai/") !== -1) {
            var title = e.text().trim();
            // Bỏ qua các thể loại rác hoặc trùng
            if (title && !added[title]) {
                added[title] = true;
                if (href.indexOf("http") === -1) {
                    href = "https://sayhentai.cfd" + href;
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
}''')
