# Quy trình tự động cào trang web bằng AI (AI Scraping Workflow)

## Mục tiêu
Tạo ra một quy trình nhất quán để mỗi khi bạn đưa một trang web truyện mới, AI (Agent) có thể tự phân tích, viết script tự động cào dữ liệu và đóng gói thành Extension cho vBook.

## Các bước quy trình:
1. **Lấy HTML thay vì dùng Selenium:** Trừ khi trang web bắt buộc phải render JS/Cloudflare, AI sẽ tải file HTML tĩnh trực tiếp qua PowerShell (Invoke-WebRequest) hoặc lệnh cURL để tránh các lỗi kết nối của Selenium.
2. **Phân tích với BeautifulSoup:** AI sẽ tạo một script Python ngắn dùng BeautifulSoup và lưu dữ liệu bóc tách được (tiêu đề, link, ảnh) ra một tệp .json.
3. **Viết Script cho vBook (JS):** Từ dữ liệu đã bóc tách, AI tự động viết các tệp:
   - home.js: Phân tích trang chủ.
   - detail.js: Lấy thông tin truyện (tên, tác giả, mô tả).
   - 	oc.js: Lấy danh sách chương.
   - chap.js: Lấy nội dung chữ/ảnh của chương.
4. **Cập nhật Cấu trúc Extension:** AI sẽ tự động tạo thư mục, lưu ảnh icon.png, tạo file plugin.json (metadata) và đưa các script JS vào thư mục src.
5. **Đóng gói (Packaging):** Sử dụng ExtensionMaker.jar có sẵn trong thư mục 	ools để đóng gói thành tệp plugin.zip. Cuối cùng, AI tự động thêm dòng khai báo mới vào plugin.json gốc ở root repository.
