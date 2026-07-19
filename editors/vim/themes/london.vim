" Vim color file
" Xscriptor London
" Maintainer: Xscriptor
" Generated from colors.json

set background=light
highlight clear
if exists("syntax_on")
    syntax reset
endif
let g:colors_name="xscriptor_london"

" UI
highlight Normal guifg=#333333 guibg=#ffffff gui=NONE
highlight Cursor guifg=#ffffff guibg=#777777 gui=NONE
highlight LineNr guifg=#333333 guibg=#ffffff gui=NONE
highlight CursorLineNr guifg=#777777 guibg=#f5f5f5 gui=NONE
highlight CursorLine guibg=#f5f5f5 gui=NONE
highlight Visual guibg=#e0e0e0 gui=NONE
highlight Search guifg=#ffffff guibg=#555555 gui=NONE
highlight IncSearch guifg=#ffffff guibg=#666666 gui=NONE
highlight StatusLine guifg=#333333 guibg=#ffffff gui=NONE
highlight StatusLineNC guifg=#333333 guibg=#ffffff gui=NONE
highlight VertSplit guifg=#333333 guibg=#ffffff gui=NONE
highlight TabLine guifg=#333333 guibg=#ffffff gui=NONE
highlight TabLineFill guifg=#333333 guibg=#ffffff gui=NONE
highlight TabLineSel guifg=#333333 guibg=#ffffff gui=NONE
highlight Pmenu guifg=#333333 guibg=#ffffff gui=NONE
highlight PmenuSel guifg=#ffffff guibg=#777777 gui=NONE
highlight PmenuSbar guibg=#333333 gui=NONE
highlight PmenuThumb guibg=#777777 gui=NONE
highlight Directory guifg=#888888 gui=NONE
highlight NonText guifg=#333333 gui=NONE
highlight SpecialKey guifg=#333333 gui=NONE
highlight Title guifg=#666666 gui=BOLD
highlight Conceal guifg=#777777 guibg=#ffffff gui=NONE
highlight SpellBad guisp=#333333 gui=undercurl
highlight SpellCap guisp=#555555 gui=undercurl
highlight SpellRare guisp=#777777 gui=undercurl
highlight SpellLocal guisp=#888888 gui=undercurl
highlight ColorColumn guibg=#f5f5f5 gui=NONE
highlight Folded guifg=#333333 guibg=#f5f5f5 gui=NONE
highlight FoldColumn guifg=#333333 guibg=#ffffff gui=NONE
highlight SignColumn guifg=#333333 guibg=#ffffff gui=NONE
highlight Todo guifg=#555555 guibg=#ffffff gui=BOLD,ITALIC
highlight Error guifg=#333333 guibg=#ffffff gui=BOLD

" Syntax
highlight Comment guifg=#333333 gui=ITALIC
highlight Constant guifg=#555555 gui=NONE
highlight String guifg=#444444 gui=NONE
highlight Character guifg=#333333 gui=NONE
highlight Number guifg=#555555 gui=NONE
highlight Boolean guifg=#555555 gui=NONE
highlight Float guifg=#555555 gui=NONE
highlight Identifier guifg=#333333 gui=NONE
highlight Function guifg=#666666 gui=NONE
highlight Statement guifg=#777777 gui=NONE
highlight Conditional guifg=#777777 gui=NONE
highlight Repeat guifg=#777777 gui=NONE
highlight Label guifg=#777777 gui=NONE
highlight Operator guifg=#777777 gui=NONE
highlight Keyword guifg=#777777 gui=NONE
highlight Exception guifg=#777777 gui=NONE
highlight PreProc guifg=#444444 gui=NONE
highlight Include guifg=#444444 gui=NONE
highlight Define guifg=#444444 gui=NONE
highlight Macro guifg=#444444 gui=NONE
highlight PreCondit guifg=#444444 gui=NONE
highlight Type guifg=#888888 gui=NONE
highlight StorageClass guifg=#777777 gui=NONE
highlight Structure guifg=#888888 gui=NONE
highlight Typedef guifg=#888888 gui=NONE
highlight Special guifg=#666666 gui=NONE
highlight SpecialChar guifg=#333333 gui=NONE
highlight Tag guifg=#333333 gui=NONE
highlight Delimiter guifg=#333333 gui=NONE
highlight SpecialComment guifg=#333333 gui=NONE
highlight Debug guifg=#333333 gui=NONE
highlight Underlined guifg=#888888 gui=UNDERLINE
highlight Ignore guifg=#333333 gui=NONE
highlight ErrorMsg guifg=#333333 guibg=#ffffff gui=BOLD
highlight WarningMsg guifg=#555555 gui=NONE
highlight MoreMsg guifg=#444444 gui=NONE
highlight Question guifg=#444444 gui=NONE
highlight ModeMsg guifg=#333333 gui=BOLD
highlight MatchParen guifg=#ffffff guibg=#777777 gui=NONE

" Diff
highlight DiffAdd guifg=#444444 guibg=#ffffff gui=NONE
highlight DiffChange guifg=#555555 guibg=#ffffff gui=NONE
highlight DiffDelete guifg=#333333 guibg=#ffffff gui=NONE
highlight DiffText guifg=#777777 guibg=#ffffff gui=NONE

" Terminal colors (for :terminal)
if has('terminal')
  let g:terminal_color_0 = '#ffffff'
  let g:terminal_color_1 = '#333333'
  let g:terminal_color_2 = '#444444'
  let g:terminal_color_3 = '#555555'
  let g:terminal_color_4 = '#666666'
  let g:terminal_color_5 = '#777777'
  let g:terminal_color_6 = '#888888'
  let g:terminal_color_7 = '#333333'
  let g:terminal_color_8 = '#333333'
  let g:terminal_color_9 = '#444444'
  let g:terminal_color_10 = '#555555'
  let g:terminal_color_11 = '#666666'
  let g:terminal_color_12 = '#777777'
  let g:terminal_color_13 = '#888888'
  let g:terminal_color_14 = '#999999'
  let g:terminal_color_15 = '#aaaaaa'
endif
