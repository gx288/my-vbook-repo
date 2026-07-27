function execute(url) {
    var doc = Http.get(url).html();
    var title = doc.select("h2").first().text().replace("Truyện ", "").trim();
    var author = doc.select("h3.h6 b").text();
    var cover = doc.select("img.story-image").attr("src");
    if (!cover) cover = doc.select("img.fluid-img").attr("src");
    var desc = doc.select(".d-none.d-sm-block p").text();
    if (!desc) desc = doc.select(".page-content p").first().text();
    
    var genres = [];
    var genreEls = doc.select("h6 a.badge");
    for (var i = 0; i < genreEls.size(); i++) {
        genres.push({
            title: genreEls.get(i).text(),
            link: genreEls.get(i).attr("href")
        });
    }

    return Response.success({
        name: title,
        cover: cover,
        author: author,
        description: desc,
        genres: genres,
        detail: "Tác giả: " + author + "<br>Thể loại: " + genres.map(g => g.title).join(", "),
        host: "https://truyenc.com"
    });
}
