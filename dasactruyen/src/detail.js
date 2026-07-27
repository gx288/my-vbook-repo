function execute(url) {
    var doc = Http.get(url).html();
    var title = doc.select("h1.entry-title").first().text().trim();
    if (!title || title === "Đăng nhập") {
        title = doc.select("title").text().split("-")[0].trim();
    }
    
    var authorEl = doc.select(".item-author a");
    var author = "Chưa cập nhật";
    if (authorEl.size() > 0) {
        author = authorEl.first().text().trim();
    } else {
        var a2 = doc.select("div.author");
        if (a2.size() > 0) {
            author = a2.first().text().replace("Tác giả:", "").trim();
        }
    }
    
    var cover = doc.select("img.img-fluid").first().attr("src");
    if (!cover) {
        cover = doc.select("div.comic-image img").attr("src");
    }
    
    var descEl = doc.select(".entry-content, .comic-description").first();
    var desc = "";
    if (descEl.size() > 0) {
        desc = descEl.text().trim();
    }
    
    return Response.success({
        name: title,
        cover: cover,
        author: author,
        description: desc,
        detail: "Tác giả: " + author,
        host: "https://dasactruyen.com"
    });
}