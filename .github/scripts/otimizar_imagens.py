from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(".")
ASSETS = ROOT / "assets"
INDEX = ROOT / "index.html"
STYLES = ROOT / "styles.css"

total_before = 0
total_after = 0
converted = []

for path in sorted(ASSETS.iterdir()):
    if path.suffix.lower() not in {".jpg", ".jpeg"}:
        continue

    out = path.with_suffix(".webp")
    with Image.open(path) as im:
        im = ImageOps.exif_transpose(im)
        if im.mode not in ("RGB", "RGBA"):
            im = im.convert("RGB")
        im.save(out, "WEBP", quality=84, method=6)

    before = path.stat().st_size
    after = out.stat().st_size
    total_before += before
    total_after += after
    converted.append((path, out, before, after))

# Usa WebP nas imagens visíveis, mantendo JPG/JPEG originais no repositório.
html = INDEX.read_text(encoding="utf-8")
for src, out, _, _ in converted:
    old_rel = src.as_posix()
    new_rel = out.as_posix()
    html = html.replace(f'src="{old_rel}"', f'src="{new_rel}"')
    html = html.replace(f'data-img="{old_rel}"', f'data-img="{new_rel}"')
INDEX.write_text(html, encoding="utf-8")

css = STYLES.read_text(encoding="utf-8")
for src, out, _, _ in converted:
    old_rel = src.as_posix()
    new_rel = out.as_posix()
    css = css.replace(f"url('{old_rel}')", f"url('{new_rel}')")
    css = css.replace(f'url("{old_rel}")', f'url("{new_rel}")')
STYLES.write_text(css, encoding="utf-8")

# Remove os arquivos temporários usados somente nesta atualização.
for temp in [
    ROOT / ".github/workflows/otimizar-imagens.yml",
    ROOT / ".github/scripts/otimizar_imagens.py",
]:
    if temp.exists():
        temp.unlink()

print(f"Convertidas: {len(converted)} imagens")
print(f"Antes: {total_before} bytes")
print(f"WebP: {total_after} bytes")
if total_before:
    print(f"Redução: {(1 - total_after / total_before) * 100:.1f}%")
for src, out, before, after in converted:
    print(f"{src.name}: {before} -> {after} bytes")
