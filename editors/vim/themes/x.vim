" Vim color file
" Xscriptor X
" Maintainer: Xscriptor
" Generated from colors.json

set background=dark
highlight clear
if exists("syntax_on")
    syntax reset
endif
let g:colors_name="xscriptor_x"

" UI
highlight Normal guifg=#f7f1ff guibg=#050505 gui=NONE
highlight Cursor guifg=#050505 guibg=#948ae3 gui=NONE
highlight LineNr guifg=#7e7b82 guibg=#050505 gui=NONE
highlight CursorLineNr guifg=#948ae3 guibg=#111112 gui=NONE
highlight CursorLine guibg=#111112 gui=NONE
highlight Visual guibg=#29282a gui=NONE
highlight Search guifg=#050505 guibg=#fce566 gui=NONE
highlight IncSearch guifg=#050505 guibg=#fd9353 gui=NONE
highlight StatusLine guifg=#f7f1ff guibg=#0a0a0a gui=NONE
highlight StatusLineNC guifg=#7e7b82 guibg=#0a0a0a gui=NONE
highlight VertSplit guifg=#7e7b82 guibg=#0a0a0a gui=NONE
highlight TabLine guifg=#7e7b82 guibg=#0a0a0a gui=NONE
highlight TabLineFill guifg=#7e7b82 guibg=#0a0a0a gui=NONE
highlight TabLineSel guifg=#f7f1ff guibg=#050505 gui=NONE
highlight Pmenu guifg=#f7f1ff guibg=#0a0a0a gui=NONE
highlight PmenuSel guifg=#050505 guibg=#948ae3 gui=NONE
highlight PmenuSbar guibg=#0f0f0f gui=NONE
highlight PmenuThumb guibg=#948ae3 gui=NONE
highlight Directory guifg=#5ad4e6 gui=NONE
highlight NonText guifg=#7e7b82 gui=NONE
highlight SpecialKey guifg=#7e7b82 gui=NONE
highlight Title guifg=#fd9353 gui=BOLD
highlight Conceal guifg=#948ae3 guibg=#050505 gui=NONE
highlight SpellBad guisp=#fc618d gui=undercurl
highlight SpellCap guisp=#fce566 gui=undercurl
highlight SpellRare guisp=#948ae3 gui=undercurl
highlight SpellLocal guisp=#5ad4e6 gui=undercurl
highlight ColorColumn guibg=#111112 gui=NONE
highlight Folded guifg=#7e7b82 guibg=#111112 gui=NONE
highlight FoldColumn guifg=#7e7b82 guibg=#050505 gui=NONE
highlight SignColumn guifg=#f7f1ff guibg=#050505 gui=NONE
highlight Todo guifg=#fce566 guibg=#050505 gui=BOLD,ITALIC
highlight Error guifg=#fc618d guibg=#050505 gui=BOLD

" Syntax
highlight Comment guifg=#7e7b82 gui=ITALIC
highlight Constant guifg=#fce566 gui=NONE
highlight String guifg=#7bd88f gui=NONE
highlight Character guifg=#fc618d gui=NONE
highlight Number guifg=#fce566 gui=NONE
highlight Boolean guifg=#fce566 gui=NONE
highlight Float guifg=#fce566 gui=NONE
highlight Identifier guifg=#f7f1ff gui=NONE
highlight Function guifg=#fd9353 gui=NONE
highlight Statement guifg=#948ae3 gui=NONE
highlight Conditional guifg=#948ae3 gui=NONE
highlight Repeat guifg=#948ae3 gui=NONE
highlight Label guifg=#948ae3 gui=NONE
highlight Operator guifg=#948ae3 gui=NONE
highlight Keyword guifg=#948ae3 gui=NONE
highlight Exception guifg=#948ae3 gui=NONE
highlight PreProc guifg=#fc618d gui=NONE
highlight Include guifg=#fc618d gui=NONE
highlight Define guifg=#fc618d gui=NONE
highlight Macro guifg=#fc618d gui=NONE
highlight PreCondit guifg=#fc618d gui=NONE
highlight Type guifg=#5ad4e6 gui=NONE
highlight StorageClass guifg=#948ae3 gui=NONE
highlight Structure guifg=#5ad4e6 gui=NONE
highlight Typedef guifg=#5ad4e6 gui=NONE
highlight Special guifg=#fd9353 gui=NONE
highlight SpecialChar guifg=#fc618d gui=NONE
highlight Tag guifg=#fc618d gui=NONE
highlight Delimiter guifg=#7e7b82 gui=NONE
highlight SpecialComment guifg=#7e7b82 gui=NONE
highlight Debug guifg=#fc618d gui=NONE
highlight Underlined guifg=#5ad4e6 gui=UNDERLINE
highlight Ignore guifg=#7e7b82 gui=NONE
highlight ErrorMsg guifg=#fc618d guibg=#050505 gui=BOLD
highlight WarningMsg guifg=#fce566 gui=NONE
highlight MoreMsg guifg=#7bd88f gui=NONE
highlight Question guifg=#7bd88f gui=NONE
highlight ModeMsg guifg=#f7f1ff gui=BOLD
highlight MatchParen guifg=#050505 guibg=#948ae3 gui=NONE

" Diff
highlight DiffAdd guifg=#7bd88f guibg=#050505 gui=NONE
highlight DiffChange guifg=#fce566 guibg=#050505 gui=NONE
highlight DiffDelete guifg=#fc618d guibg=#050505 gui=NONE
highlight DiffText guifg=#948ae3 guibg=#050505 gui=NONE

" Terminal colors (for :terminal)
if has('terminal')
  let g:terminal_color_0 = '#0a0a0a'
  let g:terminal_color_1 = '#fc618d'
  let g:terminal_color_2 = '#7bd88f'
  let g:terminal_color_3 = '#fce566'
  let g:terminal_color_4 = '#fd9353'
  let g:terminal_color_5 = '#948ae3'
  let g:terminal_color_6 = '#5ad4e6'
  let g:terminal_color_7 = '#f7f1ff'
  let g:terminal_color_8 = '#0f0f0f'
  let g:terminal_color_9 = '#fc618d'
  let g:terminal_color_10 = '#7bd88f'
  let g:terminal_color_11 = '#fce566'
  let g:terminal_color_12 = '#fd9353'
  let g:terminal_color_13 = '#948ae3'
  let g:terminal_color_14 = '#5ad4e6'
  let g:terminal_color_15 = '#f7f1ff'
endif
