" Vim color file
" Xscriptor Madrid
" Maintainer: Xscriptor
" Generated from colors.json

set background=light
highlight clear
if exists("syntax_on")
    syntax reset
endif
let g:colors_name="xscriptor_madrid"

" UI
highlight Normal guifg=#1a1a1a guibg=#fafafa gui=NONE
highlight Cursor guifg=#fafafa guibg=#4d2699 gui=NONE
highlight LineNr guifg=#4d4d4d guibg=#fafafa gui=NONE
highlight CursorLineNr guifg=#4d2699 guibg=#efefef gui=NONE
highlight CursorLine guibg=#efefef gui=NONE
highlight Visual guibg=#d8d8d8 gui=NONE
highlight Search guifg=#fafafa guibg=#8a6408 gui=NONE
highlight IncSearch guifg=#fafafa guibg=#007a9e gui=NONE
highlight StatusLine guifg=#1a1a1a guibg=#fafafa gui=NONE
highlight StatusLineNC guifg=#4d4d4d guibg=#fafafa gui=NONE
highlight VertSplit guifg=#4d4d4d guibg=#fafafa gui=NONE
highlight TabLine guifg=#4d4d4d guibg=#fafafa gui=NONE
highlight TabLineFill guifg=#4d4d4d guibg=#fafafa gui=NONE
highlight TabLineSel guifg=#1a1a1a guibg=#fafafa gui=NONE
highlight Pmenu guifg=#1a1a1a guibg=#fafafa gui=NONE
highlight PmenuSel guifg=#fafafa guibg=#4d2699 gui=NONE
highlight PmenuSbar guibg=#4d4d4d gui=NONE
highlight PmenuThumb guibg=#4d2699 gui=NONE
highlight Directory guifg=#007a9e gui=NONE
highlight NonText guifg=#4d4d4d gui=NONE
highlight SpecialKey guifg=#4d4d4d gui=NONE
highlight Title guifg=#007a9e gui=BOLD
highlight Conceal guifg=#4d2699 guibg=#fafafa gui=NONE
highlight SpellBad guisp=#990026 gui=undercurl
highlight SpellCap guisp=#8a6408 gui=undercurl
highlight SpellRare guisp=#4d2699 gui=undercurl
highlight SpellLocal guisp=#007a9e gui=undercurl
highlight ColorColumn guibg=#efefef gui=NONE
highlight Folded guifg=#4d4d4d guibg=#efefef gui=NONE
highlight FoldColumn guifg=#4d4d4d guibg=#fafafa gui=NONE
highlight SignColumn guifg=#1a1a1a guibg=#fafafa gui=NONE
highlight Todo guifg=#8a6408 guibg=#fafafa gui=BOLD,ITALIC
highlight Error guifg=#990026 guibg=#fafafa gui=BOLD

" Syntax
highlight Comment guifg=#4d4d4d gui=ITALIC
highlight Constant guifg=#8a6408 gui=NONE
highlight String guifg=#007a28 gui=NONE
highlight Character guifg=#990026 gui=NONE
highlight Number guifg=#8a6408 gui=NONE
highlight Boolean guifg=#8a6408 gui=NONE
highlight Float guifg=#8a6408 gui=NONE
highlight Identifier guifg=#1a1a1a gui=NONE
highlight Function guifg=#007a9e gui=NONE
highlight Statement guifg=#4d2699 gui=NONE
highlight Conditional guifg=#4d2699 gui=NONE
highlight Repeat guifg=#4d2699 gui=NONE
highlight Label guifg=#4d2699 gui=NONE
highlight Operator guifg=#4d2699 gui=NONE
highlight Keyword guifg=#4d2699 gui=NONE
highlight Exception guifg=#4d2699 gui=NONE
highlight PreProc guifg=#990026 gui=NONE
highlight Include guifg=#990026 gui=NONE
highlight Define guifg=#990026 gui=NONE
highlight Macro guifg=#990026 gui=NONE
highlight PreCondit guifg=#990026 gui=NONE
highlight Type guifg=#007a9e gui=NONE
highlight StorageClass guifg=#4d2699 gui=NONE
highlight Structure guifg=#007a9e gui=NONE
highlight Typedef guifg=#007a9e gui=NONE
highlight Special guifg=#007a9e gui=NONE
highlight SpecialChar guifg=#990026 gui=NONE
highlight Tag guifg=#990026 gui=NONE
highlight Delimiter guifg=#4d4d4d gui=NONE
highlight SpecialComment guifg=#4d4d4d gui=NONE
highlight Debug guifg=#990026 gui=NONE
highlight Underlined guifg=#007a9e gui=UNDERLINE
highlight Ignore guifg=#4d4d4d gui=NONE
highlight ErrorMsg guifg=#990026 guibg=#fafafa gui=BOLD
highlight WarningMsg guifg=#8a6408 gui=NONE
highlight MoreMsg guifg=#007a28 gui=NONE
highlight Question guifg=#007a28 gui=NONE
highlight ModeMsg guifg=#1a1a1a gui=BOLD
highlight MatchParen guifg=#fafafa guibg=#4d2699 gui=NONE

" Diff
highlight DiffAdd guifg=#007a28 guibg=#fafafa gui=NONE
highlight DiffChange guifg=#8a6408 guibg=#fafafa gui=NONE
highlight DiffDelete guifg=#990026 guibg=#fafafa gui=NONE
highlight DiffText guifg=#4d2699 guibg=#fafafa gui=NONE

" Terminal colors (for :terminal)
if has('terminal')
  let g:terminal_color_0 = '#fafafa'
  let g:terminal_color_1 = '#990026'
  let g:terminal_color_2 = '#007a28'
  let g:terminal_color_3 = '#8a6408'
  let g:terminal_color_4 = '#007a9e'
  let g:terminal_color_5 = '#4d2699'
  let g:terminal_color_6 = '#007a9e'
  let g:terminal_color_7 = '#1a1a1a'
  let g:terminal_color_8 = '#4d4d4d'
  let g:terminal_color_9 = '#990026'
  let g:terminal_color_10 = '#007a28'
  let g:terminal_color_11 = '#8a6408'
  let g:terminal_color_12 = '#007a9e'
  let g:terminal_color_13 = '#4d2699'
  let g:terminal_color_14 = '#007a9e'
  let g:terminal_color_15 = '#1a1a1a'
endif
