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
    comment = accessible_comment(bg, fg, c["color8"])

    def col(idx):
        return c[f"color{idx}"]

    cur_line = blend(bg, fg, 0.05)
    sel_rgba = rgba_str(fg, 0.15)

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE theme SYSTEM "gedit-color-scheme.dtd">
<theme>
  <name>Xscriptor {name}</name>
  <author>Xscriptor</author>
  <description>Xscriptor {name} theme for Gedit</description>
  <color name="background" value="{bg}"/>
  <color name="foreground" value="{fg}"/>
  <color name="cursor" value="{col(5)}"/>
  <color name="selection" value="{sel_rgba}"/>
  <color name="current_line" value="{cur_line}"/>
  <color name="line_numbers" value="{comment}"/>
  <color name="bracket_match" value="{col(5)}"/>
  <color name="search_match" value="{col(3)}"/>
  <!-- Styles -->
  <style name="text" foreground="{fg}" background="{bg}"/>
  <style name="cursor" foreground="{col(5)}"/>
  <style name="current-line" background="{cur_line}"/>
  <style name="line-numbers" foreground="{comment}"/>
  <style name="selection" background="{sel_rgba}"/>
  <style name="search-match" foreground="{bg}" background="{col(3)}"/>
  <!-- Syntax -->
  <style name="comment" foreground="{comment}" italic="true"/>
  <style name="string" foreground="{col(2)}"/>
  <style name="constant" foreground="{col(3)}"/>
  <style name="constant.numeric" foreground="{col(3)}"/>
  <style name="variable" foreground="{fg}"/>
  <style name="keyword" foreground="{col(5)}"/>
  <style name="type" foreground="{col(6)}"/>
  <style name="function" foreground="{col(4)}"/>
  <style name="preprocessor" foreground="{col(9)}"/>
  <style name="specials" foreground="{col(1)}"/>
  <style name="def:linenumber" foreground="{comment}"/>
</theme>"""

    filepath = os.path.join(DIST_DIR, f"{name}.xml")
    with open(filepath, "w") as f:
        f.write(xml)
    print(f"  \u2713 {name}.xml")
