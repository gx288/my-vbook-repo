function execute(url) {
    var doc = Http.get(url).html();
    
    var imgs = doc.select(".reading-content img");
    if (imgs.size() === 0) {
        imgs = doc.select(".page-chapter img");
    }
    if (imgs.size() === 0) {
        imgs = doc.select("#chapter-content img");
    }
    if (imgs.size() === 0) {
        imgs = doc.select(".imageload img");
    }
    
    var list = [];
    for (var i = 0; i < imgs.size(); i++) {
        var e = imgs.get(i);
        var imgUrl = e.attr("data-src");
        if (!imgUrl) imgUrl = e.attr("src");
        if (!imgUrl) imgUrl = e.attr("data-original");
        
        if (imgUrl) {
            imgUrl = imgUrl.trim();
            list.push(imgUrl);
        }
    }
    
    return Response.success(list);
}
