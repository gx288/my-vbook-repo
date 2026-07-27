function execute(url) {
    var doc = Http.get(url).html();
    var title = doc.select("h2").first().text().replace("Truyện ", "").trim();
    var author = doc.select("h3.h6").text().replace("Tác giả:", "").trim();
    var cover = doc.select("img.fluid-img").attr("src");
    
    var paragraphs = doc.select("p");
    var desc = "";
    for (var i = 0; i < paragraphs.size(); i++) {
        var pText = paragraphs.get(i).text().trim();
        if (pText.length > 50 && pText.indexOf("Tình trạng:") === -1 && pText.indexOf("Mới nhất:") === -1) {
            desc = pText;
            break;
        }
    }
    
    return Response.success({
        name: title,
        cover: cover,
        author: author,
        description: desc,
        detail: "Tác giả: " + author,
        host: "https://truyenc.com"
    });
}