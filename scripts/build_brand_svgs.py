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
    ("70+", "Clients served"),
    ("25+", "Countries"),
    ("4", "Production apps"),
]


def gradient(t):
    return (f'<linearGradient id="g" x1="0" y1="0" x2="1" y2="0">'
            f'<stop offset="0" stop-color="{t["g1"]}"/><stop offset=".55" stop-color="{t["g2"]}"/>'
            f'<stop offset="1" stop-color="{t["g3"]}"/></linearGradient>')


def proof_strip(t):
    w, h, n = 1280, 132, len(PROOF)
    col = w / n
    cells = []
    for i, (num, label) in enumerate(PROOF):
        cx = col * i + col / 2
        cells.append(
            f'<text x="{cx:.0f}" y="66" text-anchor="middle" font-size="40" font-weight="800" fill="url(#g)">{num}</text>'
            f'<text x="{cx:.0f}" y="96" text-anchor="middle" font-size="15" font-weight="600" fill="{t["muted"]}">{label}</text>')
        if i:
            cells.append(f'<line x1="{col * i:.0f}" y1="34" x2="{col * i:.0f}" y2="100" stroke="{t["line"]}"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="Career summary: ' + ", ".join(f"{a} {b.lower()}" for a, b in PROOF) + '">'
            f'<defs>{gradient(t)}</defs>'
            f'<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="18" fill="{t["bg2"]}" stroke="{t["line"]}"/>'
            f'<g font-family="{FONT}">{"".join(cells)}</g></svg>\n')


def divider(t):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="8" viewBox="0 0 1280 8" role="presentation">'
            f'<defs>{gradient(t)}</defs><rect x="0" y="3" width="1280" height="2" rx="1" fill="url(#g)"/></svg>\n')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, t in THEMES.items():
        (OUT / f"proof-strip-{name}.svg").write_text(proof_strip(t))
        (OUT / f"divider-{name}.svg").write_text(divider(t))
    print(f"wrote brand SVGs to {OUT}")


if __name__ == "__main__":
    main()
