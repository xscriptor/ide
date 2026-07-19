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


THEME_ENTRIES = [
    ("ui.background",               "bg"),
    ("ui.foreground",               "fg"),
    ("ui.cursor",                   "c5"),
    ("ui.cursor.insert",            "c5"),
    ("ui.cursor.select",            "c5"),
    ("ui.cursor.normal",            "c5"),
    ("ui.selection",                "sel"),
    ("ui.linenr",                   "cmt"),
    ("ui.linenr.selected",          "fg"),
    ("ui.statusline",               "bg"),
    ("ui.statusline.inactive",      "c0"),
    ("ui.popup",                    "bg"),
    ("ui.window",                   "c0"),
    ("ui.help",                     "bg"),
    ("ui.text",                     "fg"),
    ("ui.text.focus",               "fg"),
    ("ui.menu",                     "bg"),
    ("ui.menu.selected",            "c5"),
    ("ui.virtual.ruler",            "cmt"),
    ("ui.virtual.whitespace",       "cmt"),
    ("keyword",                     "c5"),
    ("keyword.directive",           "c5"),
    ("keyword.control",             "c5"),
    ("operator",                    "c5"),
    ("punctuation",                 "fg"),
    ("punctuation.delimiter",       "cmt"),
    ("constant",                    "c3"),
    ("constant.numeric",            "c3"),
    ("constant.character.escape",   "c1"),
    ("string",                      "c2"),
    ("string.regexp",               "c2"),
    ("function",                    "c4"),
    ("function.call",               "c4"),
    ("function.macro",              "c9"),
    ("function.builtin",            "c4"),
    ("type",                        "c6"),
    ("type.builtin",                "c6"),
    ("type.enum",                   "c6"),
    ("constructor",                 "c6"),
    ("variable",                    "fg"),
    ("variable.builtin",            "c1"),
    ("variable.parameter",          "c4"),
    ("comment",                     "cmt"),
    ("comment.line",                "cmt"),
    ("comment.block",               "cmt"),
    ("markup.heading",              "c6"),
    ("markup.list",                 "c1"),
    ("markup.bold",                 "fg"),
    ("markup.italic",               "fg"),
    ("markup.link",                 "c6"),
    ("markup.link.text",            "c2"),
    ("markup.quote",                "cmt"),
    ("markup.raw",                  "c2"),
    ("diff.plus",                   "c2"),
    ("diff.minus",                  "c1"),
    ("diff.delta",                  "c3"),
    ("ui.highlight",                "c3"),
    ("ui.highlight.fuzzy",          "c4"),
    ("warning",                     "c3"),
    ("error",                       "c1"),
    ("info",                        "c6"),
    ("hint",                        "c2"),
]

for name, c in palettes.items():
    bg = c["background"]
    fg = c["foreground"]
    comment_color = accessible_comment(bg, fg, c["color8"])

    def col(idx):
        return c[f"color{idx}"]

    def resolve(key):
        return {
            "bg": bg,
            "fg": fg,
            "c0": col(0),
            "c1": col(1),
            "c2": col(2),
            "c3": col(3),
            "c4": col(4),
            "c5": col(5),
            "c6": col(6),
            "c7": col(7),
            "c8": col(8),
            "c9": col(9),
            "c10": col(10),
            "c11": col(11),
            "c12": col(12),
            "c13": col(13),
            "c14": col(14),
            "c15": col(15),
            "cmt": comment_color,
            "sel": rgba_str(fg, 0.15),
        }[key]

    filepath = os.path.join(DIST_DIR, f"{name}.toml")
    with open(filepath, "w") as f:
        for entry_key, val_key in THEME_ENTRIES:
            f.write(f'"{entry_key}" = "{resolve(val_key)}"\n')
    print(f"  ✓ {name}.toml")
