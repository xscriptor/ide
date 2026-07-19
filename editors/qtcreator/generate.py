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


XML_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<style-scheme version="1.0" name="Xscriptor {name}">
  <style name="Text" foreground="{fg}" background="{bg}"/>
  <style name="LineNumber" foreground="{comment_color}" background="{bg}"/>
  <style name="CurrentLineNumber" foreground="{color5}" background="{blend_bg_fg_5pct}"/>
  <style name="Selection" background="{fg_at_15pct}"/>
  <style name="CurrentLine" background="{blend_bg_fg_5pct}"/>
  <style name="SearchResult" foreground="{bg}" background="{color3}"/>
  <style name="SearchScope" background="{color3_30pct}"/>
  <style name="Parentheses" foreground="{color5}" background="{blend_bg_fg_5pct}"/>
  <style name="VisualWhitespace" foreground="{comment_color}"/>
  <style name="MismatchingParentheses" foreground="{color1}"/>
  <style name="Comment" foreground="{comment_color}" italic="true"/>
  <style name="Keyword" foreground="{color5}"/>
  <style name="Type" foreground="{color6}"/>
  <style name="Function" foreground="{color4}"/>
  <style name="String" foreground="{color2}"/>
  <style name="Number" foreground="{color3}"/>
  <style name="Preprocessor" foreground="{color9}"/>
  <style name="Operator" foreground="{color5}"/>
  <style name="Constant" foreground="{color3}"/>
  <style name="Variable" foreground="{fg}"/>
</style-scheme>
"""


for name, c in palettes.items():
    bg = c["background"]
    fg = c["foreground"]
    comment_color = accessible_comment(bg, fg, c["color8"])

    def col(idx):
        return c[f"color{idx}"]

    content = XML_TEMPLATE.format(
        name=name,
        fg=fg,
        bg=bg,
        comment_color=comment_color,
        color5=col(5),
        color1=col(1),
        color2=col(2),
        color3=col(3),
        color4=col(4),
        color6=col(6),
        color9=col(9),
        blend_bg_fg_5pct=blend(bg, fg, 0.05),
        fg_at_15pct=blend(bg, fg, 0.15),
        color3_30pct=f"rgba({hex_to_rgb(col(3))[0]}, {hex_to_rgb(col(3))[1]}, {hex_to_rgb(col(3))[2]}, 0.3)",
    )

    filepath = os.path.join(DIST_DIR, f"{name}.creatortheme")
    with open(filepath, "w") as f:
        f.write(content)
    print(f"  \u2713 {name}.creatortheme")
