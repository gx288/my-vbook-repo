function execute(url, page) {
    if (!page) page = '1';
    
    var finalUrl = url;
    if (url.indexOf('?') !== -1) {
        finalUrl = url + '&page=' + page;
    } else {
        finalUrl = url + '?page=' + page;
    }

    var doc = Http.get(finalUrl).html();
    var els = doc.select('.d-flex');
    var list = [];
    
    for (var i = 0; i < els.size(); i++) {
        var e = els.get(i);
        var titleEl = e.select('h2');
        if (titleEl.size() > 0) {
            var title = titleEl.first().text().trim();
            var linkEl = e.select('a.btn');
            if (linkEl.size() === 0) {
                linkEl = e.select('.mr-3 a');
            }
            if (linkEl.size() > 0) {
                var link = linkEl.first().attr('href');
                var cover = e.select('.mr-3 img').first().attr('src');
                var desc = e.select('p.mt-2').text();
                
                if (link.indexOf('http') === -1) {
                    link = 'https://truyenc.com' + link;
                }
                
                list.push({
                    name: title,
                    link: link,
                    cover: cover,
                    description: desc,
                    host: 'https://truyenc.com'
                });
            }
        }
    }
    
    var next = (parseInt(page) + 1).toString();
    var hasNext = doc.select('.pagination a[aria-label="Trang sau"]').size() > 0 || doc.select('.pagination a.page-link').text().indexOf(next) !== -1;
    if (!hasNext && list.length === 0) {
        next = '';
    } else if (list.length > 0 && doc.select('.pagination').size() === 0) {
        next = '';
    } else if (list.length === 0) {
        next = '';
    }
    
    return Response.success(list, next);
}