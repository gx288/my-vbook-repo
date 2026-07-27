function execute(url) {
    var doc = Http.get(url).html();
    var els = doc.select("ul.chapter-list-ul li a");
    var list = [];
    
    if (els.size() === 0) {
        els = doc.select("a");
    }
    
    for (var i = 0; i < els.size(); i++) {
        var e = els.get(i);
        var link = e.attr("href");
        if (link && link.indexOf("/chuong") !== -1) {
            var name = e.text().trim();
            if (name !== "Đọc Từ Đầu" && name !== "") {
                if (link.indexOf("http") === -1) {
                    link = "https://dasactruyen.com" + link;
                }
                var exists = false;
                for (var j=0; j<list.length; j++) { if(list[j].url === link) exists = true; }
                if (!exists) {
                    list.push({
                        name: name,
                        url: link,
                        host: "https://dasactruyen.com"
                    });
                }
            }
        }
    }
    
    // Sort array by chapter name (e.g., "Chương 1", "Chương 2") if they are backwards
    // Often wordpress outputs desc.
    if (list.length > 1) {
        // Just reverse if first chapter name has bigger number than last
        // Simplest way is to just let vBook handle it, but if it's strictly backward:
        var first = list[0].name;
        var last = list[list.length-1].name;
        // Basic check
        if (first.indexOf("Chương") !== -1 && last.indexOf("Chương") !== -1) {
            var numFirst = parseInt(first.replace(/\D/g, ""));
            var numLast = parseInt(last.replace(/\D/g, ""));
            if (numFirst > numLast) {
                list.reverse();
            }
        } else {
             // force reverse because wordpress usually desc
             list.reverse();
        }
    }
    
    return Response.success(list);
}