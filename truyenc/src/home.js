function execute() {
    return Response.success([
        {title: "Trang chủ", input: "https://truyenc.com", script: "gen.js"},
        {title: "Truyện 18+", input: "https://truyenc.com/tim-truyen-18", script: "gen.js"},
        {title: "Truyện ma", input: "https://truyenc.com/tim-truyen-ma", script: "gen.js"}
    ]);
}