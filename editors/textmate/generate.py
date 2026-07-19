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


SCOPE_MAP = [
    ("Comment", "comment", 8, "italic"),
    ("Comment Line", "comment.line", 8, None),
    ("Comment Block", "comment.block", 8, None),
    ("Keyword", "keyword", 5, None),
    ("Keyword Control", "keyword.control", 5, None),
    ("Keyword Operator", "keyword.operator", 5, None),
    ("Storage", "storage", 5, None),
    ("Storage Modifier", "storage.modifier", 5, None),
    ("Storage Type", "storage.type", 6, None),
    ("Constant", "constant", 3, None),
    ("Constant Numeric", "constant.numeric", 3, None),
    ("Constant Language", "constant.language", 3, None),
    ("Constant Escape", "constant.character.escape", 9, None),
    ("String", "string", 2, None),
    ("String Quoted", "string.quoted", 2, None),
    ("String Regexp", "string.regexp", 2, None),
    ("String Other Link", "string.other.link", 9, None),
    ("Function Name", "entity.name.function", 4, None),
    ("Function Call", "meta.function-call", 12, None),
    ("Support Function", "support.function", 12, None),
    ("Variable Function", "variable.function", 12, None),
    ("Type Name", "entity.name.type", 6, None),
    ("Class Name", "entity.name.class", 6, None),
    ("Support Type", "support.type", 6, None),
    ("Support Class", "support.class", 6, None),
    ("Tag Name", "entity.name.tag", 1, None),
    ("Attribute Name", "entity.other.attribute-name", 3, None),
    ("Language Variable", "variable.language", 1, None),
    ("Variable", "variable", 7, None),
    ("Variable Readwrite", "variable.other.readwrite", 7, None),
    ("Invalid", "invalid", 9, "bold"),
    ("Invalid Deprecated", "invalid.deprecated", 9, "bold"),
    ("Punctuation", "punctuation", 7, None),
    ("Punctuation Tag", "punctuation.definition.tag", 8, None),
    ("Heading", "markup.heading", 6, "bold"),
    ("List", "markup.list", 1, None),
    ("Bold", "markup.bold", 15, "bold"),
    ("Italic", "markup.italic", 7, "italic"),
    ("Link", "markup.underline.link", 6, "underline"),
    ("Inserted", "markup.inserted", 10, None),
    ("Deleted", "markup.deleted", 1, None),
    ("Changed", "markup.changed", 3, None),
    ("Support Constant", "support.constant", 3, None),
    ("CSS Property", "support.type.property-name", 4, None),
    ("CSS Property Value", "support.constant.property-value", 3, None),
    ("CSS Tag", "entity.name.tag.css", 1, None),
    ("CSS Class", "entity.other.attribute-name.class", 3, None),
    ("CSS Id", "entity.other.attribute-name.id", 4, None),
    ("Decorator", "entity.name.function.decorator", 14, None),
    ("Storage Type Function", "storage.type.function", 5, None),
    ("Quantifier", "keyword.other.quantifier", 5, None),
    ("Embedded", "meta.embedded", 5, None),
    ("String Key", "string.quoted.key", 1, None),
    ("String Unquoted Key", "string.unquoted.key", 1, None),
]


def escape_xml(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def generate_tmtheme(name, c):
    bg = c["background"]
    fg = c["foreground"]
    comment_color = accessible_comment(bg, fg, c["color8"])

    def col(idx):
        return c[f"color{idx}"]

    def resolve(idx):
        return comment_color if idx == 8 else col(idx)

    lines = []
    lines.append('<?xml version="1.0" encoding="UTF-8"?>')
    lines.append('<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">')
    lines.append('<plist version="1.0">')
    lines.append("<dict>")
    lines.append(f"    <key>name</key>")
    lines.append(f"    <string>Xscriptor {escape_xml(name)}</string>")
    lines.append(f"    <key>settings</key>")
    lines.append(f"    <array>")

    # Global settings
    lines.append(f"        <dict>")
    lines.append(f"            <key>settings</key>")
    lines.append(f"            <dict>")
    lines.append(f"                <key>background</key>")
    lines.append(f"                <string>{bg}</string>")
    lines.append(f"                <key>foreground</key>")
    lines.append(f"                <string>{fg}</string>")
    lines.append(f"                <key>caret</key>")
    lines.append(f"                <string>{col(5)}</string>")
    lines.append(f"                <key>selection</key>")
    lines.append(f"                <string>{rgba_str(fg, 0.15)}</string>")
    lines.append(f"                <key>lineHighlight</key>")
    lines.append(f"                <string>{blend(bg, fg, 0.05)}</string>")
    lines.append(f"                <key>invisibles</key>")
    lines.append(f"                <string>{comment_color}</string>")
    lines.append(f"            </dict>")
    lines.append(f"        </dict>")

    # Scope rules
    for label, scope, idx, font_style in SCOPE_MAP:
        lines.append(f"        <dict>")
        lines.append(f"            <key>name</key>")
        lines.append(f"            <string>{escape_xml(label)}</string>")
        lines.append(f"            <key>scope</key>")
        lines.append(f"            <string>{escape_xml(scope)}</string>")
        lines.append(f"            <key>settings</key>")
        lines.append(f"            <dict>")
        lines.append(f"                <key>foreground</key>")
        lines.append(f"                <string>{resolve(idx)}</string>")
        if font_style:
            lines.append(f"                <key>fontStyle</key>")
            lines.append(f"                <string>{font_style}</string>")
        lines.append(f"            </dict>")
        lines.append(f"        </dict>")

    lines.append(f"    </array>")
    lines.append(f"</dict>")
    lines.append(f"</plist>")
    return "\n".join(lines) + "\n"


for name in palettes:
    c = palettes[name]
    xml = generate_tmtheme(name, c)
    filename = f"{name}.tmTheme"
    filepath = os.path.join(DIST_DIR, filename)
    with open(filepath, "w") as f:
        f.write(xml)
    print(f"  ✓ {filename}")
