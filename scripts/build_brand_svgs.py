"""Generate the static brand SVGs used by the profile README.

Run from the repository root:  python3 scripts/build_brand_svgs.py
Outputs light and dark variants into assets/brand/.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "brand"
FONT = "'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"

THEMES = {
    "light": dict(bg="#FFFFFF", bg2="#FAF7FB", line="#E8E1E8", ink="#202124", muted="#5F6368",
                  g1="#714B67", g2="#9333EA", g3="#168BD2"),
    "dark": dict(bg="#0D1117", bg2="#161B22", line="#30363D", ink="#F0F6FC", muted="#9DA7B3",
                 g1="#D9A6CC", g2="#C084FC", g3="#58B4EE"),
}

# Keep these figures in sync with https://usmanghias.co.uk and the Upwork overview.
PROOF = [
    ("6+", "Years in production"),
    ("91+", "Odoo implementations"),
    ("185+", "Projects delivered"),
    ("70+", "Clients"),
    ("25+", "Countries"),
    ("4", "Production applications"),
]


def gradient(t):
    return (f'<linearGradient id="g" x1="0" y1="0" x2="1" y2="0">'
            f'<stop offset="0" stop-color="{t["g1"]}"/><stop offset=".55" stop-color="{t["g2"]}"/>'
            f'<stop offset="1" stop-color="{t["g3"]}"/></linearGradient>')


def proof_strip(t):
    # 3 x 2 grid so the figures stay legible when GitHub scales the image down on phones.
    w, h, cols = 1280, 250, 3
    col = w / cols
    cells = []
    for i, (num, label) in enumerate(PROOF):
        cx, top = col * (i % cols) + col / 2, 18 + (i // cols) * 112
        cells.append(
            f'<text x="{cx:.0f}" y="{top + 54}" text-anchor="middle" font-size="46" font-weight="800" fill="url(#g)">{num}</text>'
            f'<text x="{cx:.0f}" y="{top + 86}" text-anchor="middle" font-size="19" font-weight="600" fill="{t["muted"]}">{label}</text>')
    for i in (1, 2):
        cells.append(f'<line x1="{col * i:.0f}" y1="32" x2="{col * i:.0f}" y2="{h - 32}" stroke="{t["line"]}"/>')
    cells.append(f'<line x1="40" y1="{h / 2:.0f}" x2="{w - 40}" y2="{h / 2:.0f}" stroke="{t["line"]}"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="Career summary: ' + ", ".join(f"{a} {b.lower()}" for a, b in PROOF) + '">'
            f'<defs>{gradient(t)}</defs>'
            f'<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="18" fill="{t["bg2"]}" stroke="{t["line"]}"/>'
            f'<g font-family="{FONT}">{"".join(cells)}</g></svg>\n')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, t in THEMES.items():
        (OUT / f"proof-strip-{name}.svg").write_text(proof_strip(t))
    print(f"wrote brand SVGs to {OUT}")


if __name__ == "__main__":
    main()
