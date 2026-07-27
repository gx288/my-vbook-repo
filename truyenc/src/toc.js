function execute(url) {
    var doc = Http.get(url).html();
    var els = doc.select(".story-chapters-main a");
    var list = [];
    
    for (var i = 0; i < els.size(); i++) {
        var e = els.get(i);
        var link = e.attr("href");
        if (link && link.indexOf("/truyen/") !== -1) {
            if (link.indexOf("http") === -1) {
                link = "https://truyenc.com" + link;
            }
            var name = e.text().trim();
            if (name !== "Đọc truyện" && name !== "") {
                list.push({
                    name: name,
                    url: link,
                    host: "https://truyenc.com"
                });
            }
        }
    }
    
    if (list.length === 0) {
        els = doc.select("a");
        for (var i = 0; i < els.size(); i++) {
            var e = els.get(i);
            var link = e.attr("href");
            if (link && link.indexOf("/truyen/") !== -1 && link.indexOf("/chuong-") === -1 && link.indexOf("/phan-") !== -1) {
                var name = e.text().trim();
                if (name !== "Đọc truyện" && name !== "") {
                    if (link.indexOf("http") === -1) {
                        link = "https://truyenc.com" + link;
                    }
                    var exists = false;
                    for (var j=0; j<list.length; j++) { if(list[j].url === link) exists = true; }
                    if (!exists) {
                        list.push({
                            name: name,
                            url: link,
                            host: "https://truyenc.com"
                        });
                    }
                }
            }
        }
    }
    
    return Response.success(list);
}