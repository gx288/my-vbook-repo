function execute(url) {
    var doc = Http.get(url).html();
    
    var title = doc.select("h1").first().text().trim();
    if (!title) title = doc.select(".post-title h1").first().text().trim();
    
    var cover = doc.select(".summary_image img").first().attr("data-src");
    if (!cover) cover = doc.select(".summary_image img").first().attr("src");
    if (!cover) cover = doc.select(".movie-thumb").first().attr("data-src");
    if (!cover) cover = doc.select(".movie-thumb").first().attr("src");
    
    var author = "Đang cập nhật";
    var authorEl = doc.select(".author-content").first();
    if (authorEl && authorEl.text()) author = authorEl.text().trim();
    
    var descEl = doc.select("[itemprop=description]").first();
    var desc = "";
    if (descEl) {
        var descHtml = descEl.html();
        // Remove .the_tag_list using regex to avoid jsoup mutation
        descHtml = descHtml.replace(/<div class="the_tag_list">.*?<\/div>/g, "");
        var tempDoc = Html.parse(descHtml);
        desc = tempDoc.text().trim();
        // if Html.parse is not available, we can just use string operations but usually it's fine.
        // Actually, just get text of descEl, and replace the tagList text if needed.
        // Or simply:
        desc = descEl.text().trim();
        var tagListEl = descEl.select(".the_tag_list").first();
        if (tagListEl) {
            var tagText = tagListEl.text();
            desc = desc.replace(tagText, "").trim();
        }
    }
    if (!desc) {
        var summary = doc.select(".summary__content").first();
        if (summary) desc = summary.text().trim();
    }
    
    var genres = [];
    var genreEls = doc.select(".genres-content a");
    if (genreEls.size() === 0) genreEls = doc.select("a");
    for (var i = 0; i < genreEls.size(); i++) {
        var g = genreEls.get(i);
        var href = g.attr("href");
        if (href && (href.indexOf("/the-loai/") !== -1 || href.indexOf("m_genre=") !== -1)) {
            var gTitle = g.text().trim();
            if (gTitle.indexOf("Thể loại ") !== -1) {
                gTitle = gTitle.substring(gTitle.indexOf("Thể loại ") + 9).trim();
            }
            if (gTitle) {
                genres.push({
                    title: gTitle,
                    link: href.startsWith("http") ? href : "https://www.lxmanga.quest" + href
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
        host: "https://www.lxmanga.quest"
    });
}
