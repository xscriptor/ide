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


VIM_TEMPLATE = '''\
" Vim color file
" Xscriptor {name}
" Maintainer: Xscriptor
" Generated from colors.json

set background={bg_mode}
highlight clear
if exists("syntax_on")
    syntax reset
endif
let g:colors_name="xscriptor_{name_lower}"

" UI
highlight Normal guifg={fg} guibg={bg} gui=NONE
highlight Cursor guifg={bg} guibg={c5} gui=NONE
highlight LineNr guifg={comment} guibg={bg} gui=NONE
highlight CursorLineNr guifg={c5} guibg={blend05} gui=NONE
highlight CursorLine guibg={blend05} gui=NONE
highlight Visual guibg={blend15} gui=NONE
highlight Search guifg={bg} guibg={c3} gui=NONE
highlight IncSearch guifg={bg} guibg={c4} gui=NONE
highlight StatusLine guifg={fg} guibg={c0} gui=NONE
highlight StatusLineNC guifg={comment} guibg={c0} gui=NONE
highlight VertSplit guifg={comment} guibg={c0} gui=NONE
highlight TabLine guifg={comment} guibg={c0} gui=NONE
highlight TabLineFill guifg={comment} guibg={c0} gui=NONE
highlight TabLineSel guifg={fg} guibg={bg} gui=NONE
highlight Pmenu guifg={fg} guibg={c0} gui=NONE
highlight PmenuSel guifg={bg} guibg={c5} gui=NONE
highlight PmenuSbar guibg={c8} gui=NONE
highlight PmenuThumb guibg={c5} gui=NONE
highlight Directory guifg={c6} gui=NONE
highlight NonText guifg={comment} gui=NONE
highlight SpecialKey guifg={comment} gui=NONE
highlight Title guifg={c4} gui=BOLD
highlight Conceal guifg={c5} guibg={bg} gui=NONE
highlight SpellBad guisp={c1} gui=undercurl
highlight SpellCap guisp={c3} gui=undercurl
highlight SpellRare guisp={c5} gui=undercurl
highlight SpellLocal guisp={c6} gui=undercurl
highlight ColorColumn guibg={blend05} gui=NONE
highlight Folded guifg={comment} guibg={blend05} gui=NONE
highlight FoldColumn guifg={comment} guibg={bg} gui=NONE
highlight SignColumn guifg={fg} guibg={bg} gui=NONE
highlight Todo guifg={c3} guibg={bg} gui=BOLD,ITALIC
highlight Error guifg={c1} guibg={bg} gui=BOLD

" Syntax
highlight Comment guifg={comment} gui=ITALIC
highlight Constant guifg={c3} gui=NONE
highlight String guifg={c2} gui=NONE
highlight Character guifg={c1} gui=NONE
highlight Number guifg={c3} gui=NONE
highlight Boolean guifg={c3} gui=NONE
highlight Float guifg={c3} gui=NONE
highlight Identifier guifg={fg} gui=NONE
highlight Function guifg={c4} gui=NONE
highlight Statement guifg={c5} gui=NONE
highlight Conditional guifg={c5} gui=NONE
highlight Repeat guifg={c5} gui=NONE
highlight Label guifg={c5} gui=NONE
highlight Operator guifg={c5} gui=NONE
highlight Keyword guifg={c5} gui=NONE
highlight Exception guifg={c5} gui=NONE
highlight PreProc guifg={c9} gui=NONE
highlight Include guifg={c9} gui=NONE
highlight Define guifg={c9} gui=NONE
highlight Macro guifg={c9} gui=NONE
highlight PreCondit guifg={c9} gui=NONE
highlight Type guifg={c6} gui=NONE
highlight StorageClass guifg={c5} gui=NONE
highlight Structure guifg={c6} gui=NONE
highlight Typedef guifg={c6} gui=NONE
highlight Special guifg={c4} gui=NONE
highlight SpecialChar guifg={c1} gui=NONE
highlight Tag guifg={c1} gui=NONE
highlight Delimiter guifg={comment} gui=NONE
highlight SpecialComment guifg={comment} gui=NONE
highlight Debug guifg={c1} gui=NONE
highlight Underlined guifg={c6} gui=UNDERLINE
highlight Ignore guifg={comment} gui=NONE
highlight ErrorMsg guifg={c1} guibg={bg} gui=BOLD
highlight WarningMsg guifg={c3} gui=NONE
highlight MoreMsg guifg={c2} gui=NONE
highlight Question guifg={c2} gui=NONE
highlight ModeMsg guifg={fg} gui=BOLD
highlight MatchParen guifg={bg} guibg={c5} gui=NONE

" Diff
highlight DiffAdd guifg={c2} guibg={bg} gui=NONE
highlight DiffChange guifg={c3} guibg={bg} gui=NONE
highlight DiffDelete guifg={c1} guibg={bg} gui=NONE
highlight DiffText guifg={c5} guibg={bg} gui=NONE

" Terminal colors (for :terminal)
if has('terminal')
  let g:terminal_color_0 = '{c0}'
  let g:terminal_color_1 = '{c1}'
  let g:terminal_color_2 = '{c2}'
  let g:terminal_color_3 = '{c3}'
  let g:terminal_color_4 = '{c4}'
  let g:terminal_color_5 = '{c5}'
  let g:terminal_color_6 = '{c6}'
  let g:terminal_color_7 = '{c7}'
  let g:terminal_color_8 = '{c8}'
  let g:terminal_color_9 = '{c9}'
  let g:terminal_color_10 = '{c10}'
  let g:terminal_color_11 = '{c11}'
  let g:terminal_color_12 = '{c12}'
  let g:terminal_color_13 = '{c13}'
  let g:terminal_color_14 = '{c14}'
  let g:terminal_color_15 = '{c15}'
endif
'''

LIGHT_NAMES = {"Madrid", "Helsinki", "London"}

for name, c in palettes.items():
    bg = c["background"]
    fg = c["foreground"]
    name_lower = name.lower()

    bg_mode = "light" if name in LIGHT_NAMES else "dark"

    comment = accessible_comment(bg, fg, c["color8"])
    blend05 = blend(bg, fg, 0.05)
    blend15 = blend(bg, fg, 0.15)

    vals = {"name": name, "name_lower": name_lower, "bg_mode": bg_mode,
            "bg": bg, "fg": fg, "comment": comment,
            "blend05": blend05, "blend15": blend15}
    for i in range(16):
        vals[f"c{i}"] = c[f"color{i}"]

    vim_content = VIM_TEMPLATE.format(**vals)

    filepath = os.path.join(DIST_DIR, f"{name_lower}.vim")
    with open(filepath, "w") as f:
        f.write(vim_content)
    print(f"  ✓ {name_lower}.vim")

print("\nDone! Generated 12 Vim color schemes.")
