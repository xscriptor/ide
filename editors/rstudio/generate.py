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


PLIST_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>name</key>
  <string>Xscriptor {name}</string>
  <key>settings</key>
  <array>
    <dict>
      <key>settings</key>
      <dict>
        <key>background</key>
        <string>{bg}</string>
        <key>foreground</key>
        <string>{fg}</string>
        <key>caret</key>
        <string>{color5}</string>
        <key>selection</key>
        <string>{fg_at_15pct}</string>
        <key>lineHighlight</key>
        <string>{blend_bg_fg_5pct}</string>
      </dict>
    </dict>
    <dict>
      <key>name</key>
      <string>Comment</string>
      <key>scope</key>
      <string>comment</string>
      <key>settings</key>
      <dict>
        <key>foreground</key>
        <string>{comment_color}</string>
        <key>fontStyle</key>
        <string>italic</string>
      </dict>
    </dict>
    <dict>
      <key>name</key>
      <string>String</string>
      <key>scope</key>
      <string>string</string>
      <key>settings</key>
      <dict>
        <key>foreground</key>
        <string>{color2}</string>
      </dict>
    </dict>
    <dict>
      <key>name</key>
      <string>Number</string>
      <key>scope</key>
      <string>constant.numeric</string>
      <key>settings</key>
      <dict>
        <key>foreground</key>
        <string>{color3}</string>
      </dict>
    </dict>
    <dict>
      <key>name</key>
      <string>Keyword</string>
      <key>scope</key>
      <string>keyword</string>
      <key>settings</key>
      <dict>
        <key>foreground</key>
        <string>{color5}</string>
      </dict>
    </dict>
    <dict>
      <key>name</key>
      <string>Type</string>
      <key>scope</key>
      <string>type</string>
      <key>settings</key>
      <dict>
        <key>foreground</key>
        <string>{color6}</string>
      </dict>
    </dict>
    <dict>
      <key>name</key>
      <string>Function</string>
      <key>scope</key>
      <string>entity.name.function</string>
      <key>settings</key>
      <dict>
        <key>foreground</key>
        <string>{color4}</string>
      </dict>
    </dict>
    <dict>
      <key>name</key>
      <string>Variable</string>
      <key>scope</key>
      <string>variable</string>
      <key>settings</key>
      <dict>
        <key>foreground</key>
        <string>{fg}</string>
      </dict>
    </dict>
    <dict>
      <key>name</key>
      <string>Constant</string>
      <key>scope</key>
      <string>constant</string>
      <key>settings</key>
      <dict>
        <key>foreground</key>
        <string>{color3}</string>
      </dict>
    </dict>
  </array>
</dict>
</plist>
"""


for name, c in palettes.items():
    bg = c["background"]
    fg = c["foreground"]
    comment_color = accessible_comment(bg, fg, c["color8"])

    def col(idx):
        return c[f"color{idx}"]

    content = PLIST_TEMPLATE.format(
        name=name,
        bg=bg,
        fg=fg,
        comment_color=comment_color,
        color2=col(2),
        color3=col(3),
        color4=col(4),
        color5=col(5),
        color6=col(6),
        fg_at_15pct=blend(bg, fg, 0.15),
        blend_bg_fg_5pct=blend(bg, fg, 0.05),
    )

    filepath = os.path.join(DIST_DIR, f"{name}.tmTheme")
    with open(filepath, "w") as f:
        f.write(content)
    print(f"  \u2713 {name}.tmTheme")
