"""Build the optimized README visuals from the untouched originals in assets/source/.

    python3 scripts/build_visual_assets.py

Deterministic steps only:
  1. Mask outdated live figures in the CLIVORA visual (Pillow).
  2. Add typography to empty regions via headless Chrome (HTML overlay, 1:1 pixels).
  3. Export high-quality WebP into assets/brand/ and assets/work/.

Requires Pillow with WebP support and google-chrome on PATH.
"""
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "source"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
FONTS = ("https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800"
         "&family=JetBrains+Mono:wght@500;600&display=swap")

# The live job count on clivora.io changes daily, so the generated visual must not
# freeze one (it showed 6,650+; the live site showed 1,205+ on 2026-09-25).
# (fill box, fill colour, replacement text, text colour, font size, text anchor point)
CLIVORA_MASKS = [
    ((906, 66, 941, 81), (206, 246, 243), "Live", (13, 110, 96), 11, (923, 73.5)),
    ((762, 401, 867, 419), (234, 252, 248), "Verified remote jobs ($0 fee)", (32, 38, 52), 11, (814, 410)),
    ((1201, 266, 1228, 279), (7, 62, 74), "Live", (190, 240, 230), 9, (1214.5, 272.5)),
    ((1482, 222, 1532, 241), (253, 253, 253), "Verified", (22, 27, 38), 17, (1484, 231.5)),
]


def mask_clivora(path_in, path_out):
    im = Image.open(path_in).convert("RGB")
    draw = ImageDraw.Draw(im)
    for box, fill, text, color, size, (x, y) in CLIVORA_MASKS:
        draw.rectangle(box, fill=fill)
        font = ImageFont.truetype(SERIF_BOLD, size)
        anchor = "lm" if text == "Verified" else "mm"
        draw.text((x, y), text, font=font, fill=color, anchor=anchor)
    im.save(path_out)


def page(img_path, w, h, css, body):
    return f"""<!doctype html><html><head><meta charset="utf-8"><link href="{FONTS}" rel="stylesheet">
<style>*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:{w}px;height:{h}px;overflow:hidden}}
body{{position:relative;font-family:Manrope,system-ui,sans-serif;background:url('{img_path.as_uri()}') 0 0/{w}px {h}px no-repeat}}
{css}</style></head><body>{body}</body></html>"""


HERO_CSS = """
.id{position:absolute;left:118px;top:118px;width:1000px}
.eyebrow{font-family:'JetBrains Mono',monospace;font-weight:600;font-size:21px;letter-spacing:.16em;text-transform:uppercase;color:VAR_EYEBROW}
h1{display:inline-block;font-size:104px;font-weight:800;letter-spacing:-.035em;line-height:1.02;margin-top:18px;
   background:linear-gradient(90deg,VAR_G1,VAR_G2 55%,VAR_G3);-webkit-background-clip:text;background-clip:text;color:transparent}
.role{font-size:32px;font-weight:700;color:VAR_INK;margin-top:14px;letter-spacing:-.01em;white-space:nowrap}
.stack{font-size:24px;font-weight:600;color:VAR_MUTED;margin-top:16px}
"""
HERO_BODY = """<div class="id">
<div class="eyebrow">Founder &amp; Principal Architect · CODCrafters</div>
<h1>Usman Ghias</h1>
<div class="role">Senior Odoo ERP Architect · Full-Stack Systems Engineer</div>
<div class="stack">Odoo 15–19 · Python · PostgreSQL · OWL · Enterprise integrations</div>
</div>"""
HERO_THEMES = {
    "light": dict(VAR_EYEBROW="#714B67", VAR_G1="#714B67", VAR_G2="#9333EA", VAR_G3="#168BD2",
                  VAR_INK="#202124", VAR_MUTED="#5F6368"),
    "dark": dict(VAR_EYEBROW="#D9A6CC", VAR_G1="#E2B8D8", VAR_G2="#C084FC", VAR_G3="#58B4EE",
                 VAR_INK="#F0F6FC", VAR_MUTED="#A8B3C1"),
}

ARCH_CSS = """
.lbl{position:absolute;top:22px;height:70px;display:flex;align-items:center;font-size:25px;font-weight:800;letter-spacing:-.01em;white-space:nowrap}
.p{color:#512B4E}.b{color:#0F5E96}
"""
ARCH_BODY = """<div class="lbl p" style="left:250px">Healthcare</div>
<div class="lbl p" style="left:820px">Automotive &amp; parts</div>
<div class="lbl b" style="left:1406px">Hospitality</div>"""

CLIVORA_CSS = """
.cap{position:absolute;left:52px;width:258px;height:66px;display:flex;align-items:center;gap:12px;padding:0 20px;
     font-size:17px;font-weight:700;color:#2A1F3D;white-space:nowrap}
.cap i{width:10px;height:10px;border-radius:50%;flex:none;background:linear-gradient(135deg,#9333EA,#168BD2)}
"""
CLIVORA_BODY = """<div class="cap" style="top:357px"><i></i>Web + Android</div>
<div class="cap" style="top:441px"><i></i>CRM · Projects · Invoices</div>
<div class="cap" style="top:526px"><i></i>Offline-first sync</div>"""


def render(html, w, h, out_png, workdir):
    html_file = workdir / (out_png.stem + ".html")
    html_file.write_text(html)
    subprocess.run(["google-chrome", "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    f"--window-size={w},{h}", "--force-device-scale-factor=1",
                    "--virtual-time-budget=6000", f"--screenshot={out_png}", html_file.as_uri()],
                   check=True, capture_output=True)


def to_webp(png, out, quality=90):
    out.parent.mkdir(parents=True, exist_ok=True)
    Image.open(png).convert("RGB").save(out, "WEBP", quality=quality, method=6)
    print(f"{out.relative_to(ROOT)}  {out.stat().st_size // 1024} KB")


def main():
    assert shutil.which("google-chrome"), "google-chrome is required"
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)

        for theme, tokens in HERO_THEMES.items():
            src = SRC / f"profile-hero-{theme}-source.png"
            w, h = Image.open(src).size
            css = HERO_CSS
            for k, v in tokens.items():
                css = css.replace(k, v)
            png = tmp / f"hero-{theme}.png"
            render(page(src, w, h, css, HERO_BODY), w, h, png, tmp)
            to_webp(png, ROOT / "assets/brand" / f"profile-hero-{theme}.webp")

        src = SRC / "odoo-enterprise-architecture-source.png"
        w, h = Image.open(src).size
        png = tmp / "arch.png"
        render(page(src, w, h, ARCH_CSS, ARCH_BODY), w, h, png, tmp)
        to_webp(png, ROOT / "assets/work/odoo-enterprise-architecture.webp")

        masked = tmp / "clivora-masked.png"
        mask_clivora(SRC / "clivora-product-ecosystem-source.png", masked)
        w, h = Image.open(masked).size
        png = tmp / "clivora.png"
        render(page(masked, w, h, CLIVORA_CSS, CLIVORA_BODY), w, h, png, tmp)
        to_webp(png, ROOT / "assets/work/clivora-product-ecosystem.webp")

        to_webp(SRC / "open-source-flow-source.png", ROOT / "assets/brand/open-source-flow.webp", quality=88)


if __name__ == "__main__":
    main()
