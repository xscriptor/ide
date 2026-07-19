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


def rgb_str(h):
    r, g, b = hex_to_rgb(h)
    return f"{r},{g},{b}"


for name, c in palettes.items():
    bg = c["background"]
    fg = c["foreground"]

    comment_color = accessible_comment(bg, fg, c["color8"])

    def col(idx):
        return c[f"color{idx}"]

    bg_rgb = rgb_str(bg)
    fg_rgb = rgb_str(fg)
    fg_15pct_rgb = rgb_str(blend(bg, fg, 0.15))
    blend_bg_fg_rgb = rgb_str(blend(bg, fg, 0.05))
    comment_rgb = rgb_str(comment_color)
    color2_rgb = rgb_str(col(2))
    color3_rgb = rgb_str(col(3))
    color4_rgb = rgb_str(col(4))
    color5_rgb = rgb_str(col(5))
    color6_rgb = rgb_str(col(6))
    color9_rgb = rgb_str(col(9))

    epf = f"""file_export_version=3.0
// Xscriptor {name}
instance/org.eclipse.ui.editors/backgroundColor={bg_rgb}
instance/org.eclipse.ui.editors/foregroundColor={fg_rgb}
instance/org.eclipse.ui.editors/selectionBackgroundColor={fg_15pct_rgb}
instance/org.eclipse.ui.editors/selectionForegroundColor={fg_rgb}
instance/org.eclipse.ui.editors/currentLineColor={blend_bg_fg_rgb}
instance/org.eclipse.ui.editors/lineNumberColor={comment_rgb}
instance/org.eclipse.ui.editors/printMarginColor={comment_rgb}
instance/org.eclipse.ui.editors/AbstractTextEditor.Color.Foreground={fg_rgb}
instance/org.eclipse.ui.editors/AbstractTextEditor.Color.Background={bg_rgb}
instance/org.eclipse.ui.editors/AbstractTextEditor.Color.SelectionBackgroundColor={fg_15pct_rgb}
instance/org.eclipse.ui.editors/AsynchronousColorSlave/selectionBackgroundColor.slave={fg_15pct_rgb}
instance/org.eclipse.jdt.ui/JavaEditor/TokenConstantColor={color3_rgb}
instance/org.eclipse.jdt.ui/JavaEditor/TokenKeywordColor={color5_rgb}
instance/org.eclipse.jdt.ui/JavaEditor/TokenStringColor={color2_rgb}
instance/org.eclipse.jdt.ui/JavaEditor/TokenCommentColor={comment_rgb}
instance/org.eclipse.jdt.ui/JavaEditor/TokenTypeColor={color6_rgb}
instance/org.eclipse.jdt.ui/JavaEditor/TokenMethodColor={color4_rgb}
instance/org.eclipse.jdt.ui/JavaEditor/TokenParameterColor={color4_rgb}
instance/org.eclipse.jdt.ui/JavaEditor/TokenAnnotationColor={color9_rgb}
instance/org.eclipse.jdt.ui/JavaEditor/TokenNumberColor={color3_rgb}
instance/org.eclipse.jdt.ui/JavaEditor/TokenOperatorColor={color5_rgb}
instance/org.eclipse.jdt.ui/JavaEditor/TokenReturnKeywordColor={color5_rgb}
instance/org.eclipse.jdt.ui/JavaEditor/TokenStaticMethodColor={color4_rgb}
instance/org.eclipse.jdt.ui/JavaEditor/TokenStaticFieldColor={color3_rgb}
"""

    filepath = os.path.join(DIST_DIR, f"{name}.epf")
    with open(filepath, "w") as f:
        f.write(epf)
    print(f"  {name}.epf")

print("\nDone! Generated 12 Eclipse .epf files.")
