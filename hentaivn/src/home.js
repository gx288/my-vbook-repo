function execute() {
    return Response.success([
        {title: "Cập nhật", input: "https://hentaivn.casa/?m_orderby=latest", script: "gen.js"},
        {title: "Đọc nhiều", input: "https://hentaivn.casa/?m_orderby=views", script: "gen.js"},
        {title: "Đánh giá", input: "https://hentaivn.casa/?m_orderby=rating", script: "gen.js"}
    ]);
}
