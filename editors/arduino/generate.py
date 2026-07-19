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


def rgba_str(h, a):
    r, g, b = hex_to_rgb(h)
    return f"rgba({r}, {g}, {b}, {a})"


THEME_TEMPLATE = """{{
  "name": "Xscriptor {name}",
  "type": "theme",
  "colors": {{
    "editor.background": "{bg}",
    "editor.foreground": "{fg}",
    "editorCursor.foreground": "{color5}",
    "editor.selectionBackground": "{fg_at_15pct}",
    "editor.lineHighlightBackground": "{blend_bg_fg_5pct}",
    "editorLineNumber.foreground": "{comment_color}",
    "editorLineNumber.activeForeground": "{color5}",
    "editorGutter.background": "{bg}",
    "editorBracketMatch.background": "{blend_bg_fg_5pct}",
    "editorBracketMatch.border": "{color5}",
    "editor.findMatchHighlightBackground": "{color3_30pct}",
    "editor.findMatchBackground": "{color3}",
    "editorWidget.background": "{color0}",
    "editorWidget.foreground": "{fg}",
    "inputValidation.infoBackground": "{color6_30pct}",
    "inputValidation.warningBackground": "{color3_30pct}",
    "inputValidation.errorBackground": "{color1_30pct}"
  }},
  "tokenColors": [
    {{"scope": "comment", "settings": {{"foreground": "{comment_color}", "fontStyle": "italic"}}}},
    {{"scope": "string", "settings": {{"foreground": "{color2}"}}}},
    {{"scope": "constant.numeric", "settings": {{"foreground": "{color3}"}}}},
    {{"scope": "keyword", "settings": {{"foreground": "{color5}"}}}},
    {{"scope": "storage.type", "settings": {{"foreground": "{color6}"}}}},
    {{"scope": "entity.name.function", "settings": {{"foreground": "{color4}"}}}},
    {{"scope": "entity.name.type", "settings": {{"foreground": "{color6}"}}}},
    {{"scope": "variable", "settings": {{"foreground": "{fg}"}}}},
    {{"scope": "variable.language", "settings": {{"foreground": "{color1}"}}}},
    {{"scope": "constant", "settings": {{"foreground": "{color3}"}}}},
    {{"scope": "support.function", "settings": {{"foreground": "{color4}"}}}},
    {{"scope": "support.type", "settings": {{"foreground": "{color6}"}}}},
    {{"scope": "entity.other.attribute-name", "settings": {{"foreground": "{color3}"}}}},
    {{"scope": "entity.name.tag", "settings": {{"foreground": "{color1}"}}}},
    {{"scope": "markup.heading", "settings": {{"foreground": "{color6}", "fontStyle": "bold"}}}},
    {{"scope": "markup.list", "settings": {{"foreground": "{color1}"}}}}
  ]
}}
"""


for name, c in palettes.items():
    bg = c["background"]
    fg = c["foreground"]
    comment_color = accessible_comment(bg, fg, c["color8"])

    def col(idx):
        return c[f"color{idx}"]

    content = THEME_TEMPLATE.format(
        name=name,
        bg=bg,
        fg=fg,
        comment_color=comment_color,
        color0=col(0),
        color1=col(1),
        color2=col(2),
        color3=col(3),
        color4=col(4),
        color5=col(5),
        color6=col(6),
        fg_at_15pct=blend(bg, fg, 0.15),
        blend_bg_fg_5pct=blend(bg, fg, 0.05),
        color3_30pct=rgba_str(col(3), 0.3),
        color1_30pct=rgba_str(col(1), 0.3),
        color6_30pct=rgba_str(col(6), 0.3),
    )

    filepath = os.path.join(DIST_DIR, f"{name}.json")
    with open(filepath, "w") as f:
        f.write(content)
    print(f"  \u2713 {name}.json")
