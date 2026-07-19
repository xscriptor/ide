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


def rgb_int_str(h):
    r, g, b = hex_to_rgb(h)
    return f"{r};{g};{b}"


for name, c in palettes.items():
    bg = c["background"]
    fg = c["foreground"]
    comment = accessible_comment(bg, fg, c["color8"])

    def col(idx):
        return c[f"color{idx}"]

    sel = blend(bg, fg, 0.15)
    cur_line = blend(bg, fg, 0.05)

    fg_int = rgb_int_str(fg)
    comment_int = rgb_int_str(comment)

    ini = f"""[Scheme]
Name=Xscriptor {name}
Description=Xscriptor {name} theme for Geany
Author=Xscriptor
Version=1.0

[Colors]
background={bg}
caret=0;0;0;
caret0={rgb_int_str(col(5))}
current_line={cur_line}
line_numbers={comment}
selection={sel}

[NamedStyles]
comment={comment_int},false,true,false,false
commentline={comment_int},false,true,false,false
commentdoc={comment_int},false,true,false,false
commentdockeyword={comment_int},false,true,false,false
string={rgb_int_str(col(2))},false,false,false,false
number={rgb_int_str(col(3))},false,false,false,false
keyword={rgb_int_str(col(5))},false,false,false,false
type={rgb_int_str(col(6))},false,false,false,false
function={rgb_int_str(col(4))},false,false,false,false
preprocessor={rgb_int_str(col(9))},false,false,false,false
constant={rgb_int_str(col(3))},false,false,false,false
variable={fg_int},false,false,false,false
operator={rgb_int_str(col(5))},false,false,false,false
"""

    filepath = os.path.join(DIST_DIR, f"{name}.scheme")
    with open(filepath, "w") as f:
        f.write(ini)
    print(f"  \u2713 {name}.scheme")
