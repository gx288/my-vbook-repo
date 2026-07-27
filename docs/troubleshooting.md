# Các Vấn Đề Thường Gặp & Cách Giải Quyết (Troubleshooting)

Tài liệu này ghi chú lại các lỗi điển hình gặp phải trong quá trình làm vBook Extension và cách xử lý triệt để.

## 1. Extension tải mãi không xong (Xoay tròn liên tục)
**Nguyên nhân:**
- File plugin.json (bên ngoài hoặc bên trong file zip) chứa mã ẩn **BOM (Byte Order Mark)** do hệ điều hành Windows tự chèn vào khi lưu file với chuẩn UTF-8.
- Trình phân giải JSON của Android trên app vBook không hiểu mã BOM này nên bị treo vòng lặp, dẫn tới tình trạng xoay tròn vô tận.
- **Hoặc** do cấu trúc script JS chứa lỗi cú pháp nghiêm trọng (ví dụ dùng chuẩn ES6 như hàm mũi tên =>) khiến JavaScript engine (Rhino) bị sập ngay khi nạp file.

**Cách giải quyết:**
- Luôn sử dụng thư viện chuẩn của ngôn ngữ lập trình (như json.dump trong Python) hoặc các Text Editor hỗ trợ ghi file UTF-8 without BOM.
- Tuyệt đối không dùng các cú pháp JS đời mới (ES6, ES7...) như =>, let, const. Hãy sử dụng chuẩn ES5 (ar, unction(x) { ... }).

## 2. Thêm nguồn vào vBook không báo lỗi nhưng không hiện gì
**Nguyên nhân:**
- File plugin.json nằm ở thư mục root (để khai báo kho lưu trữ) bị sai cấu trúc so với kỳ vọng của vBook.
- Dùng sai từ khóa url thay vì từ khóa đúng là path để trỏ tới file zip.
- Viết dưới dạng Mảng (Array) [ {...} ] thay vì dạng Đối tượng có Object chứa metadata và data: { "metadata": {...}, "data": [ {...} ] }.

**Cách giải quyết:**
- Sửa lại file root plugin.json theo đúng cấu trúc {"metadata": {}, "data": []}.
- Đổi khóa "url" thành "path".

## 3. Không quét được truyện hoặc lỗi danh sách
**Nguyên nhân:**
- Dùng chung các CSS selectors cơ bản của một web truyện tranh (ví dụ .item-comic, .card-full-left) để quét một web có cấu trúc khác.
- Phân trang hoặc cấu trúc web bị đổi class (ví dụ sang .d-flex).

**Cách giải quyết:**
- Dùng BeautifulSoup qua script Python để tải nguyên HTML thô của trang đích và kiểm tra kỹ bằng lệnh chọc sâu vào cấu trúc thẻ DOM thực tế.
- Tinh chỉnh các selector về đúng thẻ cha thực sự chứa dữ liệu. Luôn làm một số hàm fallback (dự phòng) như check từng thẻ  nếu class cha bị thay đổi (áp dụng cho danh sách chương 	oc.js).

## 4. Quá trình nâng cấp (Update)
**Nguyên nhân / Mong muốn:**
- Làm sao để không phải xóa đi tải lại mỗi khi cập nhật logic trên web?

**Cách giải quyết:**
- Chỉ cần tăng giá trị ersion bên trong thẻ metadata (của file extension json) và trong mảng data (của root json). App vBook sẽ tự động phát hiện phiên bản lớn hơn và hiện nút Update.
