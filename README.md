# Rollo showcase

Ảnh hiển thị trong app Rollo. Đổi ảnh ở đây thì app tự cập nhật, không cần ra bản mới.

| Thư mục | Hiện ở đâu |
|---|---|
| `home/` | Ảnh bìa trang chủ. Có nhiều ảnh thì mỗi lần mở app chọn ngẫu nhiên 1 ảnh. |
| `settings/` | Dải ảnh trượt đầu màn Cài đặt, theo thứ tự tên file. |

## Thêm / đổi ảnh

1. Mở thư mục `home` hoặc `settings` trên trang GitHub → **Add file → Upload files** → kéo ảnh vào → **Commit changes**.
2. Khoảng 1 phút sau GitHub tự nén ảnh và đăng lên (xem tab **Actions**).
3. App nhận ảnh mới ở lần mở kế tiếp (có thể chậm thêm vài phút do bộ nhớ đệm).

- Đặt tên `01.jpg`, `02.jpg`… để quyết định thứ tự. Xoá file là ảnh biến mất khỏi app.
- Nhận JPG, PNG, HEIC, WebP. Ảnh to cỡ nào cũng được: tự thu về tối đa 1200 × 1800 px.
- Ảnh dọc tỉ lệ 2:3 hiển thị đẹp nhất.
- Thông tin EXIF (vị trí GPS, máy chụp) bị xoá khỏi bản đăng lên, nhưng **file gốc trong repo vẫn còn** và repo này công khai. Nên xoá vị trí trước khi upload (iPhone: Chia sẻ → Tuỳ chọn → tắt Vị trí).

Ảnh được đăng tại `https://hnaht95.github.io/rollo-showcase/manifest.json`.
