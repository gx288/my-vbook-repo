# Quá Trình Thực Hiện (Walkthrough) - Dự án Truyenc

## Mục Tiêu
Tạo một Extension đọc truyện từ 	ruyenc.com chuẩn 100% vBook, với đầy đủ tính năng: Đọc chi tiết, lấy danh sách chương, đọc nội dung, tìm kiếm và duyệt danh mục thể loại.

## Các Bước Triển Khai

1. **Khởi tạo dự án độc lập:**
   - Tạo thư mục riêng biệt tại d:\AT\github\vbook-project\my-vbook-repo.
   - Setup các thư mục docs/, 	ools/, 	ruyenc/src/.

2. **Khởi tạo mã nguồn vBook Extension:**
   - Bóc tách CSS selector của web 	ruyenc.com thông qua request thô thay vì dùng Selenium vì lý do tính ổn định và bảo mật.
   - Viết các file cơ bản: home.js, gen.js, detail.js, 	oc.js, chap.js.
   - Thêm tính năng Thể loại (genre.js) và Tìm kiếm (search.js).

3. **Cấu trúc & Fix Bug Thực tế:**
   - Sửa lỗi vBook parse JSON bị treo bằng cách chuẩn hóa toàn bộ file JSON sang định dạng UTF-8 without BOM qua Python Script.
   - Thay đổi các cú pháp hiện đại ES6 trong detail.js sang thuần ES5 (ví dụ sửa hàm map(g => g.title) thành map(function(g) {return g.title;})) để tương thích trọn vẹn với Android JS Engine cũ (Rhino).
   - Tổ chức file plugin.json ở root đúng chuẩn { "metadata": {}, "data": [] } để vBook đọc nhận ngay lập tức, và trỏ path chính xác tới file ZIP.

4. **Đóng gói và Đẩy lên GitHub:**
   - Dùng Python nén các file JS theo chuẩn DEFLATED để vBook không bị kẹt khi giải nén.
   - git init, dd, commit và push toàn bộ mã nguồn lên Remote Repository công khai (Public) của user tại gx288/my-vbook-repo.
   - Setup phiên bản ersion: 2 để kích hoạt tính năng **Auto-update** trên app vBook.

5. **Kết quả cuối cùng:**
   - User không cần tải bằng tay, chỉ cần dán link Github Raw vào vBook.
   - Nhận thông báo cập nhật qua app bằng cách ấn nút xoay tròn mỗi khi Github Repo cập nhật Version mới.
