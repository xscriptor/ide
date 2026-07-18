import json
import os
import plistlib
import math
from collections import OrderedDict

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.join(SCRIPT_DIR, "..", "..", "..")

with open(os.path.join(REPO_ROOT, "colors.json")) as f:
    THEMES = json.load(f)


def hex_to_rgba(h):
    h = h.lstrip("#")
    return [int(h[0:2], 16) / 255.0, int(h[2:4], 16) / 255.0, int(h[4:6], 16) / 255.0, 1.0]

def rgba_to_string(rgba):
    def fmt(v):
        return f"{v:.10f}".rstrip("0").rstrip(".")
    return f"{fmt(rgba[0])} {fmt(rgba[1])} {fmt(rgba[2])} {fmt(rgba[3])}"

def clamp(v):
    return max(0.0, min(1.0, v))

def is_light(bg):
    return 0.299 * bg[0] + 0.587 * bg[1] + 0.114 * bg[2] > 0.5

SYNTAX_MAP = [
    ("xcode.syntax.plain",                  "foreground"),
    ("xcode.syntax.comment",                 2),
    ("xcode.syntax.comment.doc",             10),
    ("xcode.syntax.comment.keyword",         2),
    ("xcode.syntax.comment.doc.keyword",     10),
    ("xcode.syntax.string",                  9),
    ("xcode.syntax.character",               1),
    ("xcode.syntax.number",                  3),
    ("xcode.syntax.keyword",                 5),
    ("xcode.syntax.preprocessor",            13),
    ("xcode.syntax.identifier.class",        6),
    ("xcode.syntax.identifier.class.system",  14),
    ("xcode.syntax.identifier.constant",     11),
    ("xcode.syntax.identifier.constant.system", 3),
    ("xcode.syntax.identifier.function",     4),
    ("xcode.syntax.identifier.function.system", 14),
    ("xcode.syntax.identifier.macro",        13),
    ("xcode.syntax.identifier.macro.system",  13),
    ("xcode.syntax.identifier.type",         6),
    ("xcode.syntax.identifier.type.system",   14),
    ("xcode.syntax.identifier.variable",     7),
    ("xcode.syntax.identifier.variable.system", "foreground"),
    ("xcode.syntax.attribute",               4),
    ("xcode.syntax.url",                     12),
    ("xcode.syntax.mark",                    2),
    ("xcode.syntax.markup.code",             10),
    ("xcode.syntax.markup.aside.kind",       12),
    ("xcode.syntax.project",                 13),
    ("xcode.syntax.declaration.other",       6),
    ("xcode.syntax.declaration.type",        4),
]

def make_theme(name, colors):
    bg = hex_to_rgba(colors["background"])
    fg = hex_to_rgba(colors["foreground"])
    ansi = {i: hex_to_rgba(colors[f"color{i}"]) for i in range(16)}

    light = is_light(bg)
    amt = -0.035 if light else 0.06
    highlight = [clamp(c + amt) for c in bg[:3]] + [1.0]

    sel = ansi[4]
    sel_alpha = 0.2 if light else 0.3
    selection = [sel[0], sel[1], sel[2], sel_alpha]

    insertion = fg[:]
    block_dim = bg[:]
    invisibles = [clamp(fg[0] * 0.6), clamp(fg[1] * 0.6), clamp(fg[2] * 0.6), 0.6]

    root = OrderedDict()

    # Console
    root["DVTConsoleDebuggerInputTextColor"] = rgba_to_string(fg)
    root["DVTConsoleDebuggerInputTextFont"] = "SFMono-Regular - 12.0"
    root["DVTConsoleDebuggerOutputTextColor"] = rgba_to_string(fg)
    root["DVTConsoleDebuggerOutputTextFont"] = "SFMono-Regular - 12.0"
    root["DVTConsoleDebuggerPromptTextColor"] = rgba_to_string(ansi[2])
    root["DVTConsoleDebuggerPromptTextFont"] = "SFMono-Regular - 12.0"
    root["DVTConsoleExectuableInputTextColor"] = rgba_to_string(fg)
    root["DVTConsoleExectuableInputTextFont"] = "SFMono-Regular - 12.0"
    root["DVTConsoleExectuableOutputTextColor"] = rgba_to_string(fg)
    root["DVTConsoleExectuableOutputTextFont"] = "SFMono-Regular - 12.0"
    root["DVTConsoleTextBackgroundColor"] = rgba_to_string(bg)
    root["DVTConsoleTextInsertionPointColor"] = rgba_to_string(fg)
    root["DVTConsoleTextSelectionColor"] = rgba_to_string(selection)

    root["DVTFontAndColorVersion"] = 1
    root["DVTLineSpacing"] = 1.1

    # Markup
    markup_bg = [clamp(c + (0.1 if light else 0.05)) for c in bg[:3]] + [1.0]
    markup_border = [clamp(c + (0.05 if light else 0.08)) for c in bg[:3]] + [1.0]
    root["DVTMarkupTextBackgroundColor"] = rgba_to_string(markup_bg)
    root["DVTMarkupTextBorderColor"] = rgba_to_string(markup_border)
    root["DVTMarkupTextCodeFont"] = "SFMono-Regular - 10.0"
    root["DVTMarkupTextEmphasisColor"] = rgba_to_string(fg)
    root["DVTMarkupTextEmphasisFont"] = ".AppleSystemUIFontItalic - 10.0"
    root["DVTMarkupTextInlineCodeColor"] = rgba_to_string([fg[0], fg[1], fg[2], 0.7])
    root["DVTMarkupTextLinkColor"] = rgba_to_string(ansi[4])
    root["DVTMarkupTextLinkFont"] = ".AppleSystemUIFont - 10.0"
    root["DVTMarkupTextNormalColor"] = rgba_to_string(fg)
    root["DVTMarkupTextNormalFont"] = ".AppleSystemUIFont - 10.0"
    root["DVTMarkupTextOtherHeadingColor"] = rgba_to_string([fg[0], fg[1], fg[2], 0.5])
    root["DVTMarkupTextOtherHeadingFont"] = ".AppleSystemUIFont - 14.0"
    root["DVTMarkupTextPrimaryHeadingColor"] = rgba_to_string(fg)
    root["DVTMarkupTextPrimaryHeadingFont"] = ".AppleSystemUIFont - 24.0"
    root["DVTMarkupTextSecondaryHeadingColor"] = rgba_to_string(fg)
    root["DVTMarkupTextSecondaryHeadingFont"] = ".AppleSystemUIFont - 18.0"
    root["DVTMarkupTextStrongColor"] = rgba_to_string(fg)
    root["DVTMarkupTextStrongFont"] = ".AppleSystemUIFontBold - 10.0"

    # Scrollbar markers
    root["DVTScrollbarMarkerAnalyzerColor"] = rgba_to_string(ansi[5])
    root["DVTScrollbarMarkerBreakpointColor"] = rgba_to_string(ansi[5])
    root["DVTScrollbarMarkerDiffColor"] = rgba_to_string([0.5, 0.5, 0.5, 1.0])
    root["DVTScrollbarMarkerDiffConflictColor"] = rgba_to_string(ansi[1])
    root["DVTScrollbarMarkerErrorColor"] = rgba_to_string(ansi[1])
    root["DVTScrollbarMarkerRuntimeIssueColor"] = rgba_to_string(ansi[5])
    root["DVTScrollbarMarkerWarningColor"] = rgba_to_string(ansi[3])

    # Source text colors (string format for modern Xcode)
    root["DVTSourceTextBackground"] = rgba_to_string(bg)
    root["DVTSourceTextBlockDimBackgroundColor"] = rgba_to_string(block_dim)
    root["DVTSourceTextCurrentLineHighlightColor"] = rgba_to_string(highlight)
    root["DVTSourceTextInsertionPointColor"] = rgba_to_string(insertion)
    root["DVTSourceTextInvisiblesColor"] = rgba_to_string(invisibles)
    root["DVTSourceTextSelectionColor"] = rgba_to_string(selection)

    syntax_colors = OrderedDict()
    syntax_fonts = OrderedDict()
    for key, src in SYNTAX_MAP:
        if src == "foreground":
            syntax_colors[key] = rgba_to_string(fg)
        else:
            syntax_colors[key] = rgba_to_string(ansi[src])
        syntax_fonts[key] = "SFMono-Regular - 12.0"

    root["DVTSourceTextSyntaxColors"] = syntax_colors
    root["DVTSourceTextSyntaxFonts"] = syntax_fonts
    return root


outdir = os.path.join(SCRIPT_DIR, "dist")
os.makedirs(outdir, exist_ok=True)

for name, colors in THEMES.items():
    data = make_theme(name, colors)
    plist = plistlib.dumps(data, fmt=plistlib.FMT_XML)
    filename = f"{name}.xccolortheme"
    filepath = os.path.join(outdir, filename)
    with open(filepath, "wb") as f:
        f.write(plist)
    print(f"Created {filepath}")
