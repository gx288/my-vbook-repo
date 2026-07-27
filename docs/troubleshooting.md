# Các vấn đề thường gặp và cách xử lý (Troubleshooting)

## 1. Lỗi không kết nối được Chrome khi dùng subagent (Ví dụ báo lỗi 'connection to Chrome could not be established')
- **Nguyên nhân:** Subagent /browser hoặc Selenium cần kết nối với Chrome thông qua chế độ Remote Debugging, nhưng Chrome chưa được mở hoặc bị trùng port.
- **Cách xử lý:** 
  1. Thay vì dùng browser, yêu cầu AI dùng Python + BeautifulSoup (như lệnh Invoke-WebRequest) để tải thẳng file HTML về phân tích. Cách này nhanh, ổn định và không cần mở trình duyệt.
  2. Nếu bắt buộc phải dùng trình duyệt (cho các trang chặn bot bằng Cloudflare hoặc có render JS phức tạp), hãy mở Chrome của bạn bằng cờ: --remote-debugging-port=9222 và đảm bảo tắt hết các phiên bản Chrome đang chạy ngầm trước đó.

## 2. Lỗi Font chữ / Unicode khi đọc HTML (Ví dụ: UnicodeEncodeError)
- **Nguyên nhân:** Lỗi khi console (cmd/powershell) cố in các ký tự tiếng Việt (UTF-8) ra màn hình với bảng mã cũ.
- **Cách xử lý:** 
  1. Xuất dữ liệu thẳng ra một file .json thay vì in ra màn hình.
  2. Dùng biến môi trường $env:PYTHONIOENCODING="utf-8" khi chạy script Python.

## 3. Tool đóng gói ExtensionMaker.jar báo lỗi không chạy được
- **Nguyên nhân:** Thiếu Java hoặc file thư viện JavaFX không đúng đường dẫn.
- **Cách xử lý:** 
  1. Cài đặt Java 11 trở lên (JDK 11+).
  2. Đảm bảo thư mục javafx-sdk-win64 nằm cùng cấp với file un.bat và ExtensionMaker.jar. Nếu chạy file un.bat bị văng, hãy mở cmd tại thư mục chứa file, gõ lệnh un.bat để xem dòng lỗi cụ thể.
