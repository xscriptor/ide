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


def rgba_str(h, a):
    r, g, b = hex_to_rgb(h)
    return f"rgba({r}, {g}, {b}, {a})"


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

    fg_at_15pct = rgba_str(fg, 0.15)
    blend_bg_fg_5pct = blend(bg, fg, 0.05)

    theme = {
        "name": f"Xscriptor {name}",
        "type": "theme",
        "colors": {
            "backgroundColor": bg,
            "foregroundColor": fg,
            "primaryColor": col(5),
            "secondaryColor": col(6),
            "accentColor": col(4),
            "errorColor": col(1),
            "warningColor": col(3),
            "successColor": col(2),
            "mutedColor": comment_color,
            "inputBackground": col(0),
            "inputForeground": fg,
            "sidebarBackground": blend_bg_fg_5pct,
            "sidebarForeground": fg,
            "tabActiveBackground": bg,
            "tabActiveForeground": fg,
            "tabInactiveBackground": blend_bg_fg_5pct,
            "tabInactiveForeground": comment_color,
            "paneBackground": bg,
            "paneBorder": blend_bg_fg_5pct,
            "selectionBackground": fg_at_15pct,
            "selectionForeground": fg,
            "buttonBackground": col(5),
            "buttonForeground": bg,
            "syntaxComment": comment_color,
            "syntaxString": col(2),
            "syntaxNumber": col(3),
            "syntaxKeyword": col(5),
            "syntaxType": col(6),
            "syntaxFunction": col(4),
            "syntaxVariable": fg,
            "syntaxConstant": col(3),
            "syntaxOperator": col(5),
            "syntaxPreprocessor": col(9),
            "syntaxTag": col(1),
            "syntaxAttribute": col(3),
        },
    }

    filename = f"Xscriptor {name}.json"
    filepath = os.path.join(DIST_DIR, filename)
    with open(filepath, "w") as f:
        json.dump(theme, f, indent=2)
    print(f"  ✓ {filename}")
