" Vim color file
" Xscriptor Paris
" Maintainer: Xscriptor
" Generated from colors.json

set background=dark
highlight clear
if exists("syntax_on")
    syntax reset
endif
let g:colors_name="xscriptor_paris"

" UI
highlight Normal guifg=#f7f1ff guibg=#1a0a30 gui=NONE
highlight Cursor guifg=#1a0a30 guibg=#c4bdff gui=NONE
highlight LineNr guifg=#c4bdff guibg=#1a0a30 gui=NONE
highlight CursorLineNr guifg=#c4bdff guibg=#25163a gui=NONE
highlight CursorLine guibg=#25163a gui=NONE
highlight Visual guibg=#3b2d4f gui=NONE
highlight Search guifg=#1a0a30 guibg=#fce566 gui=NONE
highlight IncSearch guifg=#1a0a30 guibg=#a3f3ff gui=NONE
highlight StatusLine guifg=#f7f1ff guibg=#1a0a30 gui=NONE
highlight StatusLineNC guifg=#c4bdff guibg=#1a0a30 gui=NONE
highlight VertSplit guifg=#c4bdff guibg=#1a0a30 gui=NONE
highlight TabLine guifg=#c4bdff guibg=#1a0a30 gui=NONE
highlight TabLineFill guifg=#c4bdff guibg=#1a0a30 gui=NONE
highlight TabLineSel guifg=#f7f1ff guibg=#1a0a30 gui=NONE
highlight Pmenu guifg=#f7f1ff guibg=#1a0a30 gui=NONE
highlight PmenuSel guifg=#1a0a30 guibg=#c4bdff gui=NONE
highlight PmenuSbar guibg=#c4bdff gui=NONE
highlight PmenuThumb guibg=#c4bdff gui=NONE
highlight Directory guifg=#a3f3ff gui=NONE
highlight NonText guifg=#c4bdff gui=NONE
highlight SpecialKey guifg=#c4bdff gui=NONE
highlight Title guifg=#a3f3ff gui=BOLD
highlight Conceal guifg=#c4bdff guibg=#1a0a30 gui=NONE
highlight SpellBad guisp=#fc618d gui=undercurl
highlight SpellCap guisp=#fce566 gui=undercurl
highlight SpellRare guisp=#c4bdff gui=undercurl
highlight SpellLocal guisp=#a3f3ff gui=undercurl
highlight ColorColumn guibg=#25163a gui=NONE
highlight Folded guifg=#c4bdff guibg=#25163a gui=NONE
highlight FoldColumn guifg=#c4bdff guibg=#1a0a30 gui=NONE
highlight SignColumn guifg=#f7f1ff guibg=#1a0a30 gui=NONE
highlight Todo guifg=#fce566 guibg=#1a0a30 gui=BOLD,ITALIC
highlight Error guifg=#fc618d guibg=#1a0a30 gui=BOLD

" Syntax
highlight Comment guifg=#c4bdff gui=ITALIC
highlight Constant guifg=#fce566 gui=NONE
highlight String guifg=#7bd88f gui=NONE
highlight Character guifg=#fc618d gui=NONE
highlight Number guifg=#fce566 gui=NONE
highlight Boolean guifg=#fce566 gui=NONE
highlight Float guifg=#fce566 gui=NONE
highlight Identifier guifg=#f7f1ff gui=NONE
highlight Function guifg=#a3f3ff gui=NONE
highlight Statement guifg=#c4bdff gui=NONE
highlight Conditional guifg=#c4bdff gui=NONE
highlight Repeat guifg=#c4bdff gui=NONE
highlight Label guifg=#c4bdff gui=NONE
highlight Operator guifg=#c4bdff gui=NONE
highlight Keyword guifg=#c4bdff gui=NONE
highlight Exception guifg=#c4bdff gui=NONE
highlight PreProc guifg=#fc618d gui=NONE
highlight Include guifg=#fc618d gui=NONE
highlight Define guifg=#fc618d gui=NONE
highlight Macro guifg=#fc618d gui=NONE
highlight PreCondit guifg=#fc618d gui=NONE
highlight Type guifg=#a3f3ff gui=NONE
highlight StorageClass guifg=#c4bdff gui=NONE
highlight Structure guifg=#a3f3ff gui=NONE
highlight Typedef guifg=#a3f3ff gui=NONE
highlight Special guifg=#a3f3ff gui=NONE
highlight SpecialChar guifg=#fc618d gui=NONE
highlight Tag guifg=#fc618d gui=NONE
highlight Delimiter guifg=#c4bdff gui=NONE
highlight SpecialComment guifg=#c4bdff gui=NONE
highlight Debug guifg=#fc618d gui=NONE
highlight Underlined guifg=#a3f3ff gui=UNDERLINE
highlight Ignore guifg=#c4bdff gui=NONE
highlight ErrorMsg guifg=#fc618d guibg=#1a0a30 gui=BOLD
highlight WarningMsg guifg=#fce566 gui=NONE
highlight MoreMsg guifg=#7bd88f gui=NONE
highlight Question guifg=#7bd88f gui=NONE
highlight ModeMsg guifg=#f7f1ff gui=BOLD
highlight MatchParen guifg=#1a0a30 guibg=#c4bdff gui=NONE

" Diff
highlight DiffAdd guifg=#7bd88f guibg=#1a0a30 gui=NONE
highlight DiffChange guifg=#fce566 guibg=#1a0a30 gui=NONE
highlight DiffDelete guifg=#fc618d guibg=#1a0a30 gui=NONE
highlight DiffText guifg=#c4bdff guibg=#1a0a30 gui=NONE

" Terminal colors (for :terminal)
if has('terminal')
  let g:terminal_color_0 = '#1a0a30'
  let g:terminal_color_1 = '#fc618d'
  let g:terminal_color_2 = '#7bd88f'
  let g:terminal_color_3 = '#fce566'
  let g:terminal_color_4 = '#a3f3ff'
  let g:terminal_color_5 = '#c4bdff'
  let g:terminal_color_6 = '#a3f3ff'
  let g:terminal_color_7 = '#1a0a30'
  let g:terminal_color_8 = '#c4bdff'
  let g:terminal_color_9 = '#fc618d'
  let g:terminal_color_10 = '#7bd88f'
  let g:terminal_color_11 = '#fce566'
  let g:terminal_color_12 = '#a3f3ff'
  let g:terminal_color_13 = '#c4bdff'
  let g:terminal_color_14 = '#a3f3ff'
  let g:terminal_color_15 = '#f7f1ff'
endif
