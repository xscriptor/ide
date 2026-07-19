import json
import os

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


TEMPLATE = """\
# Xscriptor {name} theme
set-option global face default {fg},{bg}
set-option global face PrimarySelection {bg},{color5}
set-option global face SecondarySelection {fg_at_15pct},{color0}
set-option global face LineNumbers {comment_color},{bg}
set-option global face LineNumberCursor {color5},{blend_bg_fg_5pct}
set-option global face StatusLine {fg},{color0}
set-option global face StatusLineMode {color5},{color0}
set-option global face BufferPadding {comment_color},{bg}
set-option global face Whitespace {comment_color},{bg}
set-option global face MenuForeground {fg},{color0}
set-option global face MenuBackground {bg},{color5}
set-option global face Prompt {color5},{bg}
set-option global face Information {color2},{bg}
set-option global face Error {color1},{bg}
set-option global face Window {color0},{bg}
set-option global face Cursor {color5},{bg}

# Syntax
set-option global face comment {comment_color},{bg}+i
set-option global face meta {comment_color},{bg}
set-option global face string {color2},{bg}
set-option global face number {color3},{bg}
set-option global face keyword {color5},{bg}
set-option global face attribute {color3},{bg}
set-option global face type {color6},{bg}
set-option global face builtin {color6},{bg}
set-option global face function {color4},{bg}
set-option global face variable {fg},{bg}
set-option global face module {color4},{bg}
set-option global face operator {color5},{bg}
set-option global face preproc {color9},{bg}
set-option global face constant {color3},{bg}
set-option global face tag {color1},{bg}

# Markup
set-option global face header {color6},{bg}+b
set-option global face list {color1},{bg}
set-option global face bold {fg},{bg}+b
set-option global face italic {fg},{bg}+i
set-option global face link {color6},{bg}+u
set-option global face raw {color2},{bg}
"""


for name, c in palettes.items():
    bg = c["background"]
    fg = c["foreground"]

    comment_color = accessible_comment(bg, fg, c["color8"])
    blend_bg_fg_5pct = blend(bg, fg, 0.05)

    def col(idx):
        return c[f"color{idx}"]

    content = TEMPLATE.format(
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
        color9=col(9),
        blend_bg_fg_5pct=blend_bg_fg_5pct,
        fg_at_15pct=rgba_str(fg, 0.15),
    )

    filename = f"{name}.kak"
    filepath = os.path.join(THEMES_DIR, filename)
    with open(filepath, "w") as f:
        f.write(content.lstrip())
    print(f"  \u2713 {filename}")

print("\nDone! Generated 12 Kakoune color themes.")
