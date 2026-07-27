function execute(key, page) {
    if (!page) page = '1';
    var finalUrl = "https://dasactruyen.com/?s=" + key;
    if (page !== '1') {
        finalUrl = "https://dasactruyen.com/page/" + page + "/?s=" + key;
    }
    
    var doc = Http.get(finalUrl).html();
    var els = doc.select('article');
    var list = [];
    
    for (var i = 0; i < els.size(); i++) {
        var e = els.get(i);
        var linkEl = e.select('a').first();
        if (linkEl.size() > 0) {
            var link = linkEl.attr('href');
            var title = '';
            var titleEl = e.select('h2.entry-title');
            if (titleEl.size() > 0) {
                title = titleEl.first().text().trim();
            } else {
                title = e.select('img').attr('alt').trim();
            }
            if (!title) title = 'Không rõ tên';
            
            var cover = e.select('img').attr('src');
            if (link.indexOf('http') === -1) {
                link = 'https://dasactruyen.com' + link;
            }
            list.push({
                name: title,
                link: link,
                cover: cover,
                description: '',
                host: 'https://dasactruyen.com'
            });
        }
    }
    
    var next = (parseInt(page) + 1).toString();
    var hasNext = doc.select('a.next.page-numbers').size() > 0;
    if (!hasNext) next = '';
    
    return Response.success(list, next);
}