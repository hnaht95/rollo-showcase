# Rollo showcase

Ảnh hiển thị trong app Rollo. Đổi ảnh ở đây thì app tự cập nhật, không cần ra bản mới.

| Thư mục | Hiện ở đâu |
|---|---|
| `home/` | Ảnh bìa trang chủ. Có nhiều ảnh thì mỗi lần mở app chọn ngẫu nhiên 1 ảnh. |
| `settings/` | Dải ảnh trượt đầu màn Cài đặt, theo thứ tự tên file. |

## Thêm / đổi ảnh

1. Vào thư mục `home` hoặc `settings` → **Add file → Upload files** → kéo ảnh vào → **Commit changes**.
   - Upload thẳng: https://github.com/hnaht95/rollo-showcase/upload/main/home và https://github.com/hnaht95/rollo-showcase/upload/main/settings
2. Khoảng 1 phút sau GitHub Pages đăng xong (tab **Actions** hiện dấu xanh).
3. App nhận ảnh mới ở lần mở kế tiếp (có thể chậm thêm tới 10 phút do bộ nhớ đệm của GitHub).

### Đặt tên file = tiêu đề ảnh

- Tên file hiện làm tiêu đề ở màn xem ảnh: `Phố cổ buổi chiều.jpg` → "Phố cổ buổi chiều".
- Thêm số ở đầu để xếp thứ tự, app tự bỏ phần số: `01 - Phố cổ buổi chiều.jpg`, `02_Hồ_Tây.jpg` (dấu `_` thành dấu cách).
- File chỉ có số (`01.jpg`) thì không hiện tiêu đề.
- Không đặt tên bắt đầu bằng `_` hoặc `.` (GitHub Pages bỏ qua những file này).

### Ảnh

- Trang chủ: tỉ lệ **3:4**, khoảng 1200 × 1600 px. Cài đặt: tỉ lệ **2:3**, khoảng 1200 × 1800 px. JPEG chất lượng ~80%.
- Định dạng: JPG, PNG, HEIC, WebP, mỗi ảnh dưới 8MB. `home` tối đa 8 ảnh (thừa thì lấy 8 ảnh đầu theo tên); `settings` không giới hạn.
- Xoá file là ảnh biến mất khỏi app. Xoá hết ảnh trong một thư mục thì app dùng lại ảnh có sẵn.
- Repo này công khai và ảnh được đăng nguyên file: **xoá vị trí GPS trước khi upload** (iPhone: Chia sẻ → Tuỳ chọn → tắt Vị trí), nhưng giữ các thông tin EXIF khác.

## Thông số ảnh

App đọc thông số (ISO, tốc độ, khẩu, tiêu cự, tên film nếu chụp bằng Rollo) và tên máy từ **EXIF** của ảnh, hiện dưới tiêu đề. Khi nén ảnh, **giữ EXIF** và chỉ tắt vị trí. Ảnh không có EXIF thì chỉ hiện tiêu đề.

Màu chủ đạo app tự tính. Nút tim chỉ lưu trên máy người dùng, không hiện số.

Danh sách ảnh app đọc: https://hnaht95.github.io/rollo-showcase/manifest.json
