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

    comment_color = accessible_comment(bg, fg, c["color8"])

    def col(idx):
        return c[f"color{idx}"]

    # Determine appearance based on background luminance
    r, g, b = hex_to_rgb(bg)
    lum = relative_luminance(r, g, b)
    appearance = "dark" if lum < 0.5 else "light"

    foreground_at_15pct = rgba_str(fg, 0.15)
    blend_bg_fg_5pct = blend(bg, fg, 0.05)
    border_color = rgba_str(c["color8"], 1.0)

    theme = {
        "name": f"Xscriptor {name}",
        "appearance": appearance,
        "style": {
            "background": bg,
            "foreground": fg,
            "border": border_color,
            "scrollbar.thumb.border": border_color,
            "scrollbar.thumb.background": None,
            "scrollbar.track.background": None,
            "editor.background": bg,
            "editor.foreground": fg,
            "editor.cursor": col(5),
            "editor.accents.color": col(5),
            "editor.accents.selected_index_color": col(5),
            "editor.selection": foreground_at_15pct,
            "editor.active_line": blend_bg_fg_5pct,
            "editor.line_number": comment_color,
            "editor.active_line_number": col(5),
            "editor.gutter": bg,
            "editor.invisible_characters": comment_color,
            "editor.wrap_guides": comment_color,
            "editor.highlighted_line": blend_bg_fg_5pct,
            "editor.occurrence.border": col(5),
            "editor.occurrence.background": None,
            "editor.diagnostics.background": None,
            "editor.diagnostics.border": None,
            "editor.diagnostics.warning.background": None,
            "editor.diagnostics.warning.border": col(3),
            "editor.diagnostics.error.background": None,
            "editor.diagnostics.error.border": col(1),
            "editor.diagnostics.info.background": None,
            "editor.diagnostics.info.border": col(6),
            "editor.diagnostics.hint.background": None,
            "editor.diagnostics.hint.border": col(2),
            "editor.active_line.background": blend_bg_fg_5pct,
            "editor.document_highlight.read_background": None,
            "editor.document_highlight.write_background": None,
            "editor.range_highlight.background": None,
            "editor.range_highlight.border": None,
            "syntax": {
                "comment": comment_color,
                "comment.doc": comment_color,
                "constant": col(3),
                "constant.numeric": col(3),
                "constant.character.escape": col(1),
                "constant.builtin": col(3),
                "string": col(2),
                "string.regex": col(2),
                "string.special": col(1),
                "keyword": col(5),
                "keyword.control": col(5),
                "keyword.function": col(9),
                "keyword.return": col(5),
                "keyword.operator": col(5),
                "function": col(4),
                "function.call": col(4),
                "function.builtin": col(4),
                "function.macro": col(9),
                "function.special": col(4),
                "type": col(6),
                "type.builtin": col(6),
                "type.enum": col(6),
                "constructor": col(6),
                "variable": fg,
                "variable.builtin": col(1),
                "variable.parameter": col(4),
                "variable.member": fg,
                "variable.function": col(4),
                "operator": col(5),
                "punctuation": fg,
                "punctuation.delimiter": comment_color,
                "punctuation.bracket": fg,
                "markup.heading": col(6),
                "markup.list": col(1),
                "markup.bold": fg,
                "markup.italic": fg,
                "markup.link": col(6),
                "markup.quote": col(8),
                "markup.raw": col(2),
                "markup.highlight": col(3),
                "tag": col(1),
                "tag.attribute": col(3),
                "tag.delimiter": comment_color,
                "embedding": col(5),
                "emphasis.strong": {"font_weight": "bold", "color": fg},
                "emphasis.italic": {"font_style": "italic", "color": fg},
                "emphasis.underline": {"font_style": "underline", "color": col(6)},
            },
            "terminal": {
                "background": bg,
                "foreground": fg,
                "ansi": [
                    col(0), col(1), col(2), col(3),
                    col(4), col(5), col(6), col(7),
                    col(8), col(9), col(10), col(11),
                    col(12), col(13), col(14), col(15),
                ],
            },
        },
    }

    filename = f"Xscriptor {name}.json"
    filepath = os.path.join(DIST_DIR, filename)
    with open(filepath, "w") as f:
        json.dump(theme, f, indent=2)
    print(f"  ✓ {filename}")
