function execute(url) {
    var doc = Http.get(url).html();
    var content = doc.select(".story-content");
    content.select("script").remove();
    content.select("iframe").remove();
    content.select("a").remove();
    
    var html = content.html();
    if (!html) html = "Không lấy được nội dung chương. Hoặc nội dung bị khóa.";
    html = html.replace(/&nbsp;/g, " ");

    return Response.success(html);
}