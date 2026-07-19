" Vim color file
" Xscriptor Berlin
" Maintainer: Xscriptor
" Generated from colors.json

set background=dark
highlight clear
if exists("syntax_on")
    syntax reset
endif
let g:colors_name="xscriptor_berlin"

" UI
highlight Normal guifg=#cccccc guibg=#000000 gui=NONE
highlight Cursor guifg=#000000 guibg=#aaaaaa gui=NONE
highlight LineNr guifg=#666666 guibg=#000000 gui=NONE
highlight CursorLineNr guifg=#aaaaaa guibg=#0a0a0a gui=NONE
highlight CursorLine guibg=#0a0a0a gui=NONE
highlight Visual guibg=#1f1f1f gui=NONE
highlight Search guifg=#000000 guibg=#dddddd gui=NONE
highlight IncSearch guifg=#000000 guibg=#888888 gui=NONE
highlight StatusLine guifg=#cccccc guibg=#000000 gui=NONE
highlight StatusLineNC guifg=#666666 guibg=#000000 gui=NONE
highlight VertSplit guifg=#666666 guibg=#000000 gui=NONE
highlight TabLine guifg=#666666 guibg=#000000 gui=NONE
highlight TabLineFill guifg=#666666 guibg=#000000 gui=NONE
highlight TabLineSel guifg=#cccccc guibg=#000000 gui=NONE
highlight Pmenu guifg=#cccccc guibg=#000000 gui=NONE
highlight PmenuSel guifg=#000000 guibg=#aaaaaa gui=NONE
highlight PmenuSbar guibg=#333333 gui=NONE
highlight PmenuThumb guibg=#aaaaaa gui=NONE
highlight Directory guifg=#cccccc gui=NONE
highlight NonText guifg=#666666 gui=NONE
highlight SpecialKey guifg=#666666 gui=NONE
highlight Title guifg=#888888 gui=BOLD
highlight Conceal guifg=#aaaaaa guibg=#000000 gui=NONE
highlight SpellBad guisp=#999999 gui=undercurl
highlight SpellCap guisp=#dddddd gui=undercurl
highlight SpellRare guisp=#aaaaaa gui=undercurl
highlight SpellLocal guisp=#cccccc gui=undercurl
highlight ColorColumn guibg=#0a0a0a gui=NONE
highlight Folded guifg=#666666 guibg=#0a0a0a gui=NONE
highlight FoldColumn guifg=#666666 guibg=#000000 gui=NONE
highlight SignColumn guifg=#cccccc guibg=#000000 gui=NONE
highlight Todo guifg=#dddddd guibg=#000000 gui=BOLD,ITALIC
highlight Error guifg=#999999 guibg=#000000 gui=BOLD

" Syntax
highlight Comment guifg=#666666 gui=ITALIC
highlight Constant guifg=#dddddd gui=NONE
highlight String guifg=#bbbbbb gui=NONE
highlight Character guifg=#999999 gui=NONE
highlight Number guifg=#dddddd gui=NONE
highlight Boolean guifg=#dddddd gui=NONE
highlight Float guifg=#dddddd gui=NONE
highlight Identifier guifg=#cccccc gui=NONE
highlight Function guifg=#888888 gui=NONE
highlight Statement guifg=#aaaaaa gui=NONE
highlight Conditional guifg=#aaaaaa gui=NONE
highlight Repeat guifg=#aaaaaa gui=NONE
highlight Label guifg=#aaaaaa gui=NONE
highlight Operator guifg=#aaaaaa gui=NONE
highlight Keyword guifg=#aaaaaa gui=NONE
highlight Exception guifg=#aaaaaa gui=NONE
highlight PreProc guifg=#bbbbbb gui=NONE
highlight Include guifg=#bbbbbb gui=NONE
highlight Define guifg=#bbbbbb gui=NONE
highlight Macro guifg=#bbbbbb gui=NONE
highlight PreCondit guifg=#bbbbbb gui=NONE
highlight Type guifg=#cccccc gui=NONE
highlight StorageClass guifg=#aaaaaa gui=NONE
highlight Structure guifg=#cccccc gui=NONE
highlight Typedef guifg=#cccccc gui=NONE
highlight Special guifg=#888888 gui=NONE
highlight SpecialChar guifg=#999999 gui=NONE
highlight Tag guifg=#999999 gui=NONE
highlight Delimiter guifg=#666666 gui=NONE
highlight SpecialComment guifg=#666666 gui=NONE
highlight Debug guifg=#999999 gui=NONE
highlight Underlined guifg=#cccccc gui=UNDERLINE
highlight Ignore guifg=#666666 gui=NONE
highlight ErrorMsg guifg=#999999 guibg=#000000 gui=BOLD
highlight WarningMsg guifg=#dddddd gui=NONE
highlight MoreMsg guifg=#bbbbbb gui=NONE
highlight Question guifg=#bbbbbb gui=NONE
highlight ModeMsg guifg=#cccccc gui=BOLD
highlight MatchParen guifg=#000000 guibg=#aaaaaa gui=NONE

" Diff
highlight DiffAdd guifg=#bbbbbb guibg=#000000 gui=NONE
highlight DiffChange guifg=#dddddd guibg=#000000 gui=NONE
highlight DiffDelete guifg=#999999 guibg=#000000 gui=NONE
highlight DiffText guifg=#aaaaaa guibg=#000000 gui=NONE

" Terminal colors (for :terminal)
if has('terminal')
  let g:terminal_color_0 = '#000000'
  let g:terminal_color_1 = '#999999'
  let g:terminal_color_2 = '#bbbbbb'
  let g:terminal_color_3 = '#dddddd'
  let g:terminal_color_4 = '#888888'
  let g:terminal_color_5 = '#aaaaaa'
  let g:terminal_color_6 = '#cccccc'
  let g:terminal_color_7 = '#ffffff'
  let g:terminal_color_8 = '#333333'
  let g:terminal_color_9 = '#bbbbbb'
  let g:terminal_color_10 = '#dddddd'
  let g:terminal_color_11 = '#ffffff'
  let g:terminal_color_12 = '#aaaaaa'
  let g:terminal_color_13 = '#cccccc'
  let g:terminal_color_14 = '#eeeeee'
  let g:terminal_color_15 = '#ffffff'
endif
