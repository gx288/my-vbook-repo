function execute() {
    return Response.success([
        {title: "Truyện Sex", input: "https://truyenc.com/truyen-sex", script: "gen.js"},
        {title: "Truyện 18+", input: "https://truyenc.com/tim-truyen-18", script: "gen.js"}
    ]);
}
