function execute() {
    return Response.success([
        {title: "Truyện ma", input: "https://truyenc.com/tim-truyen-ma", script: "gen.js"},
        {title: "Truyện 18+", input: "https://truyenc.com/tim-truyen-18", script: "gen.js"},
        {title: "Truyện cười", input: "https://truyenc.com/tim-truyen-cuoi", script: "gen.js"},
        {title: "Truyện audio", input: "https://truyenc.com/tim-truyen-audio", script: "gen.js"},
        {title: "Chưa phân loại", input: "https://truyenc.com/tim-truyen-chua-phan-loai", script: "gen.js"}
    ]);
}