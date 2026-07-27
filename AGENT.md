# vBook Plugin Development Guidelines (AGENT.md)

This file contains critical, hard-earned knowledge for developing vBook extensions in this repository. Any AI agent (or human) working on this project MUST read and strictly follow these rules to avoid repeating past critical failures.

## 1. Biểu thức chính quy (RegExp) trong `plugin.json`
- **Mục đích:** `regexp` dùng để vBook nhận diện URL thuộc về plugin nào. Nó được dùng ở 2 nơi:
  1. Khi bấm vào chương truyện (chỉ kiểm tra khớp một phần - Matcher.find).
  2. **Khi dùng trình duyệt web tích hợp của vBook** (kiểm tra khớp TOÀN BỘ URL - Matcher.matches).
- **Quy tắc bắt buộc:** Để vBook hiện nút "Tải xuống / Mở bằng Plugin" trên trình duyệt, `regexp` BẮT BUỘC phải bao phủ toàn bộ URL, tức là phải có `.*` ở hai đầu.
  - VÍ DỤ ĐÚNG: `".*truyenc\\.com.*"`
  - VÍ DỤ SAI: `"truyenc\\.com"` (sẽ không nhận diện được trên trình duyệt).
- **LỖI CHẾT NGƯỜI VỚI BACKSLASH (`\`):**
  - Trong file JSON lưu trên ổ đĩa, chuỗi regex CHỈ ĐƯỢC PHÉP CÓ 2 DẤU GẠCH CHÉO: `".*truyenc\\.com.*"`.
  - Nếu dùng Python `json.dump` để tạo file, **phải dùng raw string** `r".*truyenc\.com.*"`. Nếu viết `".*truyenc\\\\.com.*"` trong code Python, file JSON sẽ bị lưu thành 4 dấu gạch chéo (`\\\\`), khiến vBook dịch ra lỗi (tìm chuỗi có chứa dấu gạch chéo thật) và báo lỗi *"Phần mở rộng trang này chưa được cài đặt"*.

## 2. Quản lý Cache (CDN & vBook)
- **Truy cập từ Việt Nam:** GitHub raw bị chặn bởi các nhà mạng VN. Dự án sử dụng `raw.githack.com` để thay thế.
- **Cache của CDN:** `raw.githack.com` lưu cache khá cứng. Khi dev và cần update gấp cho vBook nhận diện bản mới, cách tốt nhất là **bump version** trong file `plugin.json` lên 1 đơn vị.
- **Cache của vBook (LỖI DATABASE):**
  - Khi người dùng mở 1 truyện, vBook sẽ lưu (cache) toàn bộ danh sách URL của các chương truyện đó vào Database nội bộ.
  - Nếu file `toc.js` bị lỗi trả về sai URL chương, vBook sẽ lưu URL sai đó lại. Dù sau đó bạn có fix `toc.js` đúng đi nữa, người dùng bấm vào chương ĐÃ LƯU vẫn sẽ bị lỗi.
  - **Cách xử lý:** Luôn dặn người dùng phải **Vuốt từ trên xuống ở màn hình mục lục để tải lại danh sách chương**, hoặc xóa truyện khỏi thư viện thêm lại.

## 3. Cấu trúc Code và Đóng gói (Packaging)
- Cấu trúc 1 plugin gồm: `thư_mục_plugin/plugin.json`, `thư_mục_plugin/src/...`, và `thư_mục_plugin/plugin.zip`.
- **Zip là file quan trọng nhất:** vBook KHÔNG đọc thư mục `src`, vBook chỉ tải và giải nén file `plugin.zip`. Mọi thay đổi trong `src` BẮT BUỘC phải được nén lại vào `plugin.zip`.
- **Đồng bộ Phiên bản:** Khi nâng cấp bản mới, phải cập nhật `version` ở cả 2 nơi:
  1. File `plugin.json` gốc ở ngoài cùng repo.
  2. File `thư_mục_plugin/plugin.json` (nằm bên trong và được đóng gói vào ZIP).
- **Code sạch:** Mọi file script Python phục vụ test hay build phải được để trong thư mục `tools/`. Không vứt lung tung ngoài thư mục gốc.

## 4. Gỡ lỗi vBook cơ bản
- Nếu lỗi *"Lỗi tải chương"* -> Lỗi do `chap.js` (ví dụ: selector sai, hoặc HTML rỗng gây ra lỗi khi gọi hàm `.replace()`).
- Nếu lỗi *"Phần mở rộng trang này chưa được cài đặt..."* khi bấm vào chương -> Lỗi do URL của chương đó không khớp (match) với `regexp` của plugin, HỌC lại quy tắc số 1 và 2.
