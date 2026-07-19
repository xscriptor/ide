import json
import os

PARENT = os.path.dirname(__file__)
DIST_DIR = os.path.join(PARENT, "themes")
os.makedirs(DIST_DIR, exist_ok=True)

with open(os.path.join(PARENT, "..", "..", "colors.json")) as f:
    palettes = json.load(f)


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


def blend(ha, hb, pct):
    ra, ga, ba = hex_to_rgb(ha)
    rb, gb, bb = hex_to_rgb(hb)
    return rgb_to_hex(
        round(ra + (rb - ra) * pct),
        round(ga + (gb - ga) * pct),
        round(ba + (bb - ba) * pct),
    )


def relative_luminance(r, g, b):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4

    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def contrast_ratio(ha, hb):
    r1, g1, b1 = hex_to_rgb(ha)
    r2, g2, b2 = hex_to_rgb(hb)
    l1 = relative_luminance(r1, g1, b1)
    l2 = relative_luminance(r2, g2, b2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def accessible_comment(bg, fg, comment_candidate):
    if contrast_ratio(comment_candidate, bg) >= 3.0:
        return comment_candidate
    for pct in (0.15, 0.25, 0.35, 0.5, 0.65, 0.8):
        candidate = blend(bg, fg, pct)
        if contrast_ratio(candidate, bg) >= 3.0:
            return candidate
    return blend(bg, fg, 0.65)


for name, c in palettes.items():
    bg = c["background"]
    fg = c["foreground"]

    comment_color = accessible_comment(bg, fg, c["color8"])

    def col(idx):
        return c[f"color{idx}"]

    blend_bg_fg_5pct = blend(bg, fg, 0.05)

    r, g, b = hex_to_rgb(bg)
    lum = relative_luminance(r, g, b)
    is_dark = lum < 0.5

    theme = {
        "name": f"Xscriptor {name}",
        "description": f"Xscriptor {name} theme for Replit",
        "dark": is_dark,
        "colors": {
            "background": bg,
            "foreground": fg,
            "primary": col(5),
            "secondary": col(6),
            "accent": col(4),
            "success": col(2),
            "warning": col(3),
            "error": col(1),
            "info": col(6),
            "muted": comment_color,
            "border": blend_bg_fg_5pct,
            "surface": col(0),
            "code": {
                "comment": comment_color,
                "string": col(2),
                "number": col(3),
                "keyword": col(5),
                "type": col(6),
                "function": col(4),
                "variable": fg,
                "constant": col(3),
                "operator": col(5),
                "preprocessor": col(9),
                "tag": col(1),
                "attribute": col(3),
            },
        },
    }

    filename = f"Xscriptor {name}.json"
    filepath = os.path.join(DIST_DIR, filename)
    with open(filepath, "w") as f:
        json.dump(theme, f, indent=2)
    print(f"  ✓ {filename}")
