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


def np_color(h):
    return h.lstrip("#").upper()


for name, c in palettes.items():
    bg = c["background"]
    fg = c["foreground"]
    comment = accessible_comment(bg, fg, c["color8"])

    def col(idx):
        return c[f"color{idx}"]

    sel_bg = blend(bg, fg, 0.15)
    cur_line = blend(bg, fg, 0.05)

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<NotepadPlus>
  <Theme name="Xscriptor {name}">
    <GlobalStyle bgColor="{np_color(bg)}" fgColor="{np_color(fg)}" bold="no" italic="no"/>
    <WidgetStyle name="Global override" bgColor="{np_color(bg)}" fgColor="{np_color(fg)}"/>
    <WidgetStyle name="Selected text colour" bgColor="{np_color(sel_bg)}" fgColor="{np_color(fg)}"/>
    <WidgetStyle name="Caret colour" fgColor="{np_color(col(5))}"/>
    <WidgetStyle name="Line number margin" bgColor="{np_color(bg)}" fgColor="{np_color(comment)}"/>
    <WidgetStyle name="Fold" bgColor="{np_color(bg)}" fgColor="{np_color(col(5))}"/>
    <WidgetStyle name="Current line" bgColor="{np_color(cur_line)}"/>
    <!-- Syntax -->
    <LexerType name="comment" fgColor="{np_color(comment)}" italic="yes"/>
    <LexerType name="commentline" fgColor="{np_color(comment)}" italic="yes"/>
    <LexerType name="string" fgColor="{np_color(col(2))}"/>
    <LexerType name="number" fgColor="{np_color(col(3))}"/>
    <LexerType name="keyword" fgColor="{np_color(col(5))}"/>
    <LexerType name="type" fgColor="{np_color(col(6))}"/>
    <LexerType name="function" fgColor="{np_color(col(4))}"/>
    <LexerType name="preprocessor" fgColor="{np_color(col(9))}"/>
    <LexerType name="operator" fgColor="{np_color(col(5))}"/>
    <LexerType name="variable" fgColor="{np_color(fg)}"/>
    <LexerType name="constant" fgColor="{np_color(col(3))}"/>
  </Theme>
</NotepadPlus>"""

    filepath = os.path.join(DIST_DIR, f"{name}.xml")
    with open(filepath, "w") as f:
        f.write(xml)
    print(f"  \u2713 {name}.xml")
