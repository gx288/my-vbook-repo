function execute(url) {
    var doc = Http.get(url).html();
    
    var title = doc.select("h1").first().text().trim();
    if (!title) title = doc.select(".post-title h1").first().text().trim();
    
    var cover = doc.select(".movie-thumb").first().attr("data-src");
    if (!cover) cover = doc.select(".movie-thumb").first().attr("src");
    if (!cover) cover = doc.select(".info-image img").first().attr("src");
    
    var author = "Đang cập nhật";
    var authorEl = doc.select(".author-content").first();
    if (authorEl.text()) author = authorEl.text().trim();
    
    var descEl = doc.select("[itemprop=description]").first();
    var tagList = descEl.select(".the_tag_list");
    if (tagList.size() > 0) tagList.remove();
    
    var desc = descEl.text().trim();
    if (!desc) desc = doc.select(".summary__content").first().text().trim();
    
    var genres = [];
    var genreEls = doc.select("a");
    for (var i = 0; i < genreEls.size(); i++) {
        var g = genreEls.get(i);
        var href = g.attr("href");
        if (href && href.indexOf("/the-loai/") !== -1) {
            var gTitle = g.text().trim();
            if (gTitle.indexOf("Thể loại ") !== -1) {
                gTitle = gTitle.substring(gTitle.indexOf("Thể loại ") + 9).trim();
            } else if (gTitle.startsWith("- ")) {
                continue; // Skip the side menu ones if they match
            }
            if (gTitle) {
                genres.push({
                    title: gTitle,
                    link: href
                });
            }
        }
    }
    
    return Response.success({
        name: title,
        cover: cover,
        author: author,
        description: desc,
        genres: genres,
        detail: "Tác giả: " + author,
        host: "https://sayhentai.cfd"
    });
}