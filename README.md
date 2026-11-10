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

- Tên file quyết định thứ tự: `01.jpg`, `02.jpg`… Xoá file là ảnh biến mất khỏi app. Xoá hết ảnh trong một thư mục thì app dùng lại ảnh có sẵn.
- Định dạng: JPG, PNG, HEIC, WebP, mỗi ảnh dưới 8MB. `home` tối đa 8 ảnh (thừa thì lấy 8 ảnh đầu theo tên); `settings` không giới hạn.
- Nên nén trước: ảnh dọc 2:3, khoảng 1200 × 1800 px, JPEG chất lượng ~80% (300–500KB).
- Repo này công khai và ảnh được đăng nguyên file: **xoá vị trí GPS trước khi upload** (iPhone: Chia sẻ → Tuỳ chọn → tắt Vị trí).

## Thông tin ảnh và số tim

Sửa file [`_data/photos.yml`](_data/photos.yml) (bấm biểu tượng bút chì trên GitHub): tiêu đề, film, ISO, tốc độ, khẩu, ống kính, máy, ngày, nơi chụp, số tim. Mục nào bỏ trống thì app đọc từ EXIF của ảnh (nếu còn). Màu chủ đạo app tự tính, không cần điền.

Danh sách ảnh app đọc: https://hnaht95.github.io/rollo-showcase/manifest.json
