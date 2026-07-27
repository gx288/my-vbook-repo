function execute(url, page) {
    if (!page) page = '1';
    
    var finalUrl = url;
    if (page !== '1') {
        if (finalUrl.indexOf('?') !== -1) {
            finalUrl = finalUrl + '&page=' + page;
        } else {
            // Check if it already has trailing slash
            if (finalUrl.slice(-1) !== '/') finalUrl += '/';
            finalUrl = finalUrl + 'page/' + page + '/';
        }
    }

    var doc = Http.get(finalUrl).html();
    var els = doc.select('.box-full-right-item, .item-comic, .col-6.col-md-3, article.card-custom');
    var list = [];
    
    for (var i = 0; i < els.size(); i++) {
        var e = els.get(i);
        var linkEl = e.select('a').first();
        if (linkEl.size() > 0) {
            var link = linkEl.attr('href');
            var title = '';
            
            var titleEl = e.select('.box-full-right-title');
            if (titleEl.size() > 0) {
                title = titleEl.first().text().trim();
            }
            if (title === '') {
                titleEl = e.select('h2.entry-title');
                if (titleEl.size() > 0) title = titleEl.first().text().trim();
            }
            if (title === '') {
                title = e.select('img').attr('alt').trim();
            }
            if (title === '') title = 'Không rõ tên';

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
    if (!hasNext) {
        next = '';
    }
    
    return Response.success(list, next);
}