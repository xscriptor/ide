import json
import os
from xml.sax.saxutils import escape

PARENT = os.path.dirname(__file__)
THEMES_DIR = os.path.join(PARENT, "themes")
os.makedirs(THEMES_DIR, exist_ok=True)

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
    return (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)


def accessible_comment(bg, fg, comment_candidate):
    if contrast_ratio(comment_candidate, bg) >= 3.0:
        return comment_candidate
    for pct in (0.15, 0.25, 0.35, 0.5, 0.65, 0.8):
        candidate = blend(bg, fg, pct)
        if contrast_ratio(candidate, bg) >= 3.0:
            return candidate
    return blend(bg, fg, 0.65)


def rgb_floats(h):
    r, g, b = hex_to_rgb(h)
    return f"{r/255:.10f} {g/255:.10f} {b/255:.10f}"


def rgba_floats(h, a):
    r, g, b = hex_to_rgb(h)
    return f"{r/255:.10f} {g/255:.10f} {b/255:.10f} {a}"


TEMPLATE = """\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>name</key>
  <string>Xscriptor {name}</string>
  <key>author</key>
  <string>Xscriptor</string>
  <key>background</key>
  <string>{bg_rgb_floats}</string>
  <key>foreground</key>
  <string>{fg_rgb_floats}</string>
  <key>selection</key>
  <string>{fg_rgba_floats}</string>
  <key>currentLine</key>
  <string>{blend_bg_fg_rgba_floats}</string>
  <key>cursor</key>
  <string>{color5_rgb_floats}</string>
  <key>lineNumbers</key>
  <string>{comment_color_rgb_floats}</string>
  <key>comment</key>
  <string>{comment_color_rgb_floats}</string>
  <key>string</key>
  <string>{color2_rgb_floats}</string>
  <key>number</key>
  <string>{color3_rgb_floats}</string>
  <key>keyword</key>
  <string>{color5_rgb_floats}</string>
  <key>type</key>
  <string>{color6_rgb_floats}</string>
  <key>function</key>
  <string>{color4_rgb_floats}</string>
  <key>preprocessor</key>
  <string>{color9_rgb_floats}</string>
  <key>variable</key>
  <string>{fg_rgb_floats}</string>
  <key>constant</key>
  <string>{color3_rgb_floats}</string>
  <key>tag</key>
  <string>{color1_rgb_floats}</string>
  <key>attribute</key>
  <string>{color3_rgb_floats}</string>
</dict>
</plist>
"""


for name, c in palettes.items():
    bg = c["background"]
    fg = c["foreground"]

    comment_color = accessible_comment(bg, fg, c["color8"])
    blend_bg_fg_5pct = blend(bg, fg, 0.05)

    def col(idx):
        return c[f"color{idx}"]

    content = TEMPLATE.format(
        name=escape(name),
        bg_rgb_floats=rgb_floats(bg),
        fg_rgb_floats=rgb_floats(fg),
        fg_rgba_floats=rgba_floats(fg, 0.15),
        blend_bg_fg_rgba_floats=rgba_floats(blend_bg_fg_5pct, 1.0),
        comment_color_rgb_floats=rgb_floats(comment_color),
        color1_rgb_floats=rgb_floats(col(1)),
        color2_rgb_floats=rgb_floats(col(2)),
        color3_rgb_floats=rgb_floats(col(3)),
        color4_rgb_floats=rgb_floats(col(4)),
        color5_rgb_floats=rgb_floats(col(5)),
        color6_rgb_floats=rgb_floats(col(6)),
        color9_rgb_floats=rgb_floats(col(9)),
    )

    filename = f"{name}.bbcolorproject"
    filepath = os.path.join(THEMES_DIR, filename)
    with open(filepath, "w") as f:
        f.write(content.lstrip())
    print(f"  \u2713 {filename}")

print("\nDone! Generated 12 BBEdit color themes.")
