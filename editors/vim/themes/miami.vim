" Vim color file
" Xscriptor Miami
" Maintainer: Xscriptor
" Generated from colors.json

set background=dark
highlight clear
if exists("syntax_on")
    syntax reset
endif
let g:colors_name="xscriptor_miami"

" UI
highlight Normal guifg=#f7f1ff guibg=#000000 gui=NONE
highlight Cursor guifg=#000000 guibg=#D36CFF gui=NONE
highlight LineNr guifg=#69676c guibg=#000000 gui=NONE
highlight CursorLineNr guifg=#D36CFF guibg=#0c0c0d gui=NONE
highlight CursorLine guibg=#0c0c0d gui=NONE
highlight Visual guibg=#252426 gui=NONE
highlight Search guifg=#000000 guibg=#FFD84C gui=NONE
highlight IncSearch guifg=#000000 guibg=#00FFA8 gui=NONE
highlight StatusLine guifg=#f7f1ff guibg=#000000 gui=NONE
highlight StatusLineNC guifg=#69676c guibg=#000000 gui=NONE
highlight VertSplit guifg=#69676c guibg=#000000 gui=NONE
highlight TabLine guifg=#69676c guibg=#000000 gui=NONE
highlight TabLineFill guifg=#69676c guibg=#000000 gui=NONE
highlight TabLineSel guifg=#f7f1ff guibg=#000000 gui=NONE
highlight Pmenu guifg=#f7f1ff guibg=#000000 gui=NONE
highlight PmenuSel guifg=#000000 guibg=#D36CFF gui=NONE
highlight PmenuSbar guibg=#69676c gui=NONE
highlight PmenuThumb guibg=#D36CFF gui=NONE
highlight Directory guifg=#47CFFF gui=NONE
highlight NonText guifg=#69676c gui=NONE
highlight SpecialKey guifg=#69676c gui=NONE
highlight Title guifg=#00FFA8 gui=BOLD
highlight Conceal guifg=#D36CFF guibg=#000000 gui=NONE
highlight SpellBad guisp=#FF4C8B gui=undercurl
highlight SpellCap guisp=#FFD84C gui=undercurl
highlight SpellRare guisp=#D36CFF gui=undercurl
highlight SpellLocal guisp=#47CFFF gui=undercurl
highlight ColorColumn guibg=#0c0c0d gui=NONE
highlight Folded guifg=#69676c guibg=#0c0c0d gui=NONE
highlight FoldColumn guifg=#69676c guibg=#000000 gui=NONE
highlight SignColumn guifg=#f7f1ff guibg=#000000 gui=NONE
highlight Todo guifg=#FFD84C guibg=#000000 gui=BOLD,ITALIC
highlight Error guifg=#FF4C8B guibg=#000000 gui=BOLD

" Syntax
highlight Comment guifg=#69676c gui=ITALIC
highlight Constant guifg=#FFD84C gui=NONE
highlight String guifg=#7FFFD4 gui=NONE
highlight Character guifg=#FF4C8B gui=NONE
highlight Number guifg=#FFD84C gui=NONE
highlight Boolean guifg=#FFD84C gui=NONE
highlight Float guifg=#FFD84C gui=NONE
highlight Identifier guifg=#f7f1ff gui=NONE
highlight Function guifg=#00FFA8 gui=NONE
highlight Statement guifg=#D36CFF gui=NONE
highlight Conditional guifg=#D36CFF gui=NONE
highlight Repeat guifg=#D36CFF gui=NONE
highlight Label guifg=#D36CFF gui=NONE
highlight Operator guifg=#D36CFF gui=NONE
highlight Keyword guifg=#D36CFF gui=NONE
highlight Exception guifg=#D36CFF gui=NONE
highlight PreProc guifg=#FF4C8B gui=NONE
highlight Include guifg=#FF4C8B gui=NONE
highlight Define guifg=#FF4C8B gui=NONE
highlight Macro guifg=#FF4C8B gui=NONE
highlight PreCondit guifg=#FF4C8B gui=NONE
highlight Type guifg=#47CFFF gui=NONE
highlight StorageClass guifg=#D36CFF gui=NONE
highlight Structure guifg=#47CFFF gui=NONE
highlight Typedef guifg=#47CFFF gui=NONE
highlight Special guifg=#00FFA8 gui=NONE
highlight SpecialChar guifg=#FF4C8B gui=NONE
highlight Tag guifg=#FF4C8B gui=NONE
highlight Delimiter guifg=#69676c gui=NONE
highlight SpecialComment guifg=#69676c gui=NONE
highlight Debug guifg=#FF4C8B gui=NONE
highlight Underlined guifg=#47CFFF gui=UNDERLINE
highlight Ignore guifg=#69676c gui=NONE
highlight ErrorMsg guifg=#FF4C8B guibg=#000000 gui=BOLD
highlight WarningMsg guifg=#FFD84C gui=NONE
highlight MoreMsg guifg=#7FFFD4 gui=NONE
highlight Question guifg=#7FFFD4 gui=NONE
highlight ModeMsg guifg=#f7f1ff gui=BOLD
highlight MatchParen guifg=#000000 guibg=#D36CFF gui=NONE

" Diff
highlight DiffAdd guifg=#7FFFD4 guibg=#000000 gui=NONE
highlight DiffChange guifg=#FFD84C guibg=#000000 gui=NONE
highlight DiffDelete guifg=#FF4C8B guibg=#000000 gui=NONE
highlight DiffText guifg=#D36CFF guibg=#000000 gui=NONE

" Terminal colors (for :terminal)
if has('terminal')
  let g:terminal_color_0 = '#000000'
  let g:terminal_color_1 = '#FF4C8B'
  let g:terminal_color_2 = '#7FFFD4'
  let g:terminal_color_3 = '#FFD84C'
  let g:terminal_color_4 = '#00FFA8'
  let g:terminal_color_5 = '#D36CFF'
  let g:terminal_color_6 = '#47CFFF'
  let g:terminal_color_7 = '#f7f1ff'
  let g:terminal_color_8 = '#69676c'
  let g:terminal_color_9 = '#FF4C8B'
  let g:terminal_color_10 = '#7FFFD4'
  let g:terminal_color_11 = '#FFD84C'
  let g:terminal_color_12 = '#00FFA8'
  let g:terminal_color_13 = '#D36CFF'
  let g:terminal_color_14 = '#47CFFF'
  let g:terminal_color_15 = '#f7f1ff'
endif
