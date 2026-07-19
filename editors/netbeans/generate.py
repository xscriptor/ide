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
    return (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)


def accessible_comment(bg, fg, comment_candidate):
    if contrast_ratio(comment_candidate, bg) >= 3.0:
        return comment_candidate
    for pct in (0.15, 0.25, 0.35, 0.5, 0.65, 0.8):
        candidate = blend(bg, fg, pct)
        if contrast_ratio(candidate, bg) >= 3.0:
            return candidate
    return blend(bg, fg, 0.65)


XML_HEADER = '<?xml version="1.0" encoding="UTF-8"?>\n'
DOCTYPE = '<!DOCTYPE fontscolors PUBLIC "-//NetBeans//DTD Editor Fonts and Colors 1.1//EN" "http://www.netbeans.org/dtds/EditorFontsColors-1_1.dtd">\n'

XML_TEMPLATE = """\
<fontscolors>
  <fontcolor name="default" foreColor="{fg}" backColor="{bg}"/>
  <fontcolor name="caret" foreColor="{c5}"/>
  <fontcolor name="selection" foreColor="{fg}" backColor="{fg_at_15pct}"/>
  <fontcolor name="selectionForeground" foreColor="{bg}"/>
  <fontcolor name="line-numbers" foreColor="{comment_color}"/>
  <fontcolor name="current-line" backColor="{blend_bg_fg_5pct}"/>
  <fontcolor name="code-folding" foreColor="{comment_color}"/>
  <fontcolor name="brace-matching" foreColor="{c5}"/>
  <fontcolor name="comment" foreColor="{comment_color}" italic="true"/>
  <fontcolor name="string" foreColor="{c2}"/>
  <fontcolor name="number" foreColor="{c3}"/>
  <fontcolor name="keyword" foreColor="{c5}"/>
  <fontcolor name="type" foreColor="{c6}"/>
  <fontcolor name="method" foreColor="{c4}"/>
  <fontcolor name="operator" foreColor="{c5}"/>
  <fontcolor name="constant" foreColor="{c3}"/>
  <fontcolor name="field" foreColor="{fg}"/>
  <fontcolor name="local-variable" foreColor="{fg}"/>
  <fontcolor name="parameter" foreColor="{c4}"/>
  <fontcolor name="annotation" foreColor="{c9}"/>
  <fontcolor name="class" foreColor="{c6}"/>
  <fontcolor name="interface" foreColor="{c6}"/>
  <fontcolor name="separator" foreColor="{comment_color}"/>
  <fontcolor name="whitespace" foreColor="{comment_color}"/>
</fontscolors>"""


for name, c in palettes.items():
    bg = c["background"]
    fg = c["foreground"]

    comment_color = accessible_comment(bg, fg, c["color8"])

    def col(idx):
        return c[f"color{idx}"]

    vals = {
        "name": name,
        "bg": bg,
        "fg": fg,
        "comment_color": comment_color,
        "fg_at_15pct": blend(bg, fg, 0.15),
        "blend_bg_fg_5pct": blend(bg, fg, 0.05),
    }
    for i in range(16):
        vals[f"c{i}"] = c[f"color{i}"]

    xml_content = XML_HEADER + DOCTYPE + XML_TEMPLATE.format(**vals)

    filepath = os.path.join(DIST_DIR, f"{name}.xml")
    with open(filepath, "w") as f:
        f.write(xml_content)
    print(f"  {name}.xml")

print("\nDone! Generated 12 NetBeans XML theme files.")
