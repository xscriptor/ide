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


CONF_TEMPLATE = """// Xscriptor {name}
colour_set_1 = {bg_hex_no_hash}
colour_set_2 = {fg_hex_no_hash}
colour_set_3 = {color5_hex_no_hash}
colour_set_4 = {comment_color_hex_no_hash}
colour_set_5 = {blend_bg_fg_5pct_hex_no_hash}
colour_set_6 = {fg_at_15pct_hex_no_hash}
colour_set_7 = {color1_hex_no_hash}
colour_set_8 = {color2_hex_no_hash}
colour_set_9 = {color3_hex_no_hash}
colour_set_10 = {color4_hex_no_hash}
colour_set_11 = {color6_hex_no_hash}
colour_set_12 = {color9_hex_no_hash}
colour_set_13 = {color5_hex_no_hash}
colour_set_14 = {color8_hex_no_hash}
"""


for name, c in palettes.items():
    bg = c["background"]
    fg = c["foreground"]
    comment_color = accessible_comment(bg, fg, c["color8"])

    def col(idx):
        return c[f"color{idx}"]

    content = CONF_TEMPLATE.format(
        name=name,
        bg_hex_no_hash=bg.lstrip("#"),
        fg_hex_no_hash=fg.lstrip("#"),
        comment_color_hex_no_hash=comment_color.lstrip("#"),
        color5_hex_no_hash=col(5).lstrip("#"),
        color1_hex_no_hash=col(1).lstrip("#"),
        color2_hex_no_hash=col(2).lstrip("#"),
        color3_hex_no_hash=col(3).lstrip("#"),
        color4_hex_no_hash=col(4).lstrip("#"),
        color6_hex_no_hash=col(6).lstrip("#"),
        color9_hex_no_hash=col(9).lstrip("#"),
        color8_hex_no_hash=col(8).lstrip("#"),
        blend_bg_fg_5pct_hex_no_hash=blend(bg, fg, 0.05).lstrip("#"),
        fg_at_15pct_hex_no_hash=blend(bg, fg, 0.15).lstrip("#"),
    )

    filepath = os.path.join(DIST_DIR, f"{name}.conf")
    with open(filepath, "w") as f:
        f.write(content)
    print(f"  \u2713 {name}.conf")
