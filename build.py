"""Nén ảnh trong home/ và settings/ rồi xuất ra _site/ kèm manifest.json cho app Rollo.

- Thu nhỏ để vừa khung 1200 x 1800 px (đủ nét trên màn 3x), JPEG chất lượng 82.
- Xoá toàn bộ EXIF (vị trí GPS, máy chụp...), chỉ giữ hồ sơ màu.
- Tên file đầu ra là mã băm nội dung: đổi ảnh thì tên đổi, app biết để tải lại.
- Thứ tự hiển thị theo tên file gốc (01.jpg, 02.jpg...).
"""
import hashlib, json, shutil
from pathlib import Path
from PIL import Image, ImageOps

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pass

ROOT = Path(__file__).parent
OUT = ROOT / "_site"
SECTIONS = ["home", "settings"]
EXTS = {".jpg", ".jpeg", ".png", ".heic", ".heif", ".webp"}
MAX_W, MAX_H = 1200, 1800

shutil.rmtree(OUT, ignore_errors=True)
manifest = {"version": 1}
for section in SECTIONS:
    (OUT / section).mkdir(parents=True)
    files = sorted(p for p in (ROOT / section).iterdir() if p.suffix.lower() in EXTS)
    items = []
    for src in files:
        im = ImageOps.exif_transpose(Image.open(src))
        icc = im.info.get("icc_profile")
        im = im.convert("RGB")
        im.thumbnail((MAX_W, MAX_H), Image.LANCZOS)
        digest = hashlib.sha1(src.read_bytes()).hexdigest()[:12]
        name = f"{section}/{digest}.jpg"
        kw = {"quality": 82, "optimize": True, "progressive": True}
        if icc:
            kw["icc_profile"] = icc
        im.save(OUT / name, "JPEG", **kw)
        items.append(name)
        print(f"{src.relative_to(ROOT)} -> {name} {im.size[0]}x{im.size[1]} {(OUT / name).stat().st_size // 1024}KB")
    manifest[section] = items

(OUT / "manifest.json").write_text(json.dumps(manifest, indent=2))
(OUT / "index.html").write_text("<!doctype html><meta charset=utf-8><title>Rollo showcase</title><p>Images for the Rollo app.</p>")
print(json.dumps(manifest, indent=2))
