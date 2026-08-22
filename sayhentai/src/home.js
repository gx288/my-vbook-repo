function execute() {
    return Response.success([
        {title: "Mới cập nhật", input: "https://sayhentai.cfd/danh-sach?order_by=update_time", script: "gen.js"},
        {title: "Đọc nhiều nhất", input: "https://sayhentai.cfd/danh-sach?order_by=view", script: "gen.js"},
        {title: "Mới đăng", input: "https://sayhentai.cfd/danh-sach?order_by=new", script: "gen.js"}
    ]);
}