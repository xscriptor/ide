" Vim color file
" Xscriptor Lahabana
" Maintainer: Xscriptor
" Generated from colors.json

set background=dark
highlight clear
if exists("syntax_on")
    syntax reset
endif
let g:colors_name="xscriptor_lahabana"

" UI
highlight Normal guifg=#f7f1ff guibg=#19191a gui=NONE
highlight Cursor guifg=#19191a guibg=#948ae3 gui=NONE
highlight LineNr guifg=#67656a guibg=#19191a gui=NONE
highlight CursorLineNr guifg=#948ae3 guibg=#242425 gui=NONE
highlight CursorLine guibg=#242425 gui=NONE
highlight Visual guibg=#3a393c gui=NONE
highlight Search guifg=#19191a guibg=#e5ff9d gui=NONE
highlight IncSearch guifg=#19191a guibg=#fd9353 gui=NONE
highlight StatusLine guifg=#f7f1ff guibg=#19191a gui=NONE
highlight StatusLineNC guifg=#67656a guibg=#19191a gui=NONE
highlight VertSplit guifg=#67656a guibg=#19191a gui=NONE
highlight TabLine guifg=#67656a guibg=#19191a gui=NONE
highlight TabLineFill guifg=#67656a guibg=#19191a gui=NONE
highlight TabLineSel guifg=#f7f1ff guibg=#19191a gui=NONE
highlight Pmenu guifg=#f7f1ff guibg=#19191a gui=NONE
highlight PmenuSel guifg=#19191a guibg=#948ae3 gui=NONE
highlight PmenuSbar guibg=#19191a gui=NONE
highlight PmenuThumb guibg=#948ae3 gui=NONE
highlight Directory guifg=#5ad4e6 gui=NONE
highlight NonText guifg=#67656a gui=NONE
highlight SpecialKey guifg=#67656a gui=NONE
highlight Title guifg=#fd9353 gui=BOLD
highlight Conceal guifg=#948ae3 guibg=#19191a gui=NONE
highlight SpellBad guisp=#fc618d gui=undercurl
highlight SpellCap guisp=#e5ff9d gui=undercurl
highlight SpellRare guisp=#948ae3 gui=undercurl
highlight SpellLocal guisp=#5ad4e6 gui=undercurl
highlight ColorColumn guibg=#242425 gui=NONE
highlight Folded guifg=#67656a guibg=#242425 gui=NONE
highlight FoldColumn guifg=#67656a guibg=#19191a gui=NONE
highlight SignColumn guifg=#f7f1ff guibg=#19191a gui=NONE
highlight Todo guifg=#e5ff9d guibg=#19191a gui=BOLD,ITALIC
highlight Error guifg=#fc618d guibg=#19191a gui=BOLD

" Syntax
highlight Comment guifg=#67656a gui=ITALIC
highlight Constant guifg=#e5ff9d gui=NONE
highlight String guifg=#7bd88f gui=NONE
highlight Character guifg=#fc618d gui=NONE
highlight Number guifg=#e5ff9d gui=NONE
highlight Boolean guifg=#e5ff9d gui=NONE
highlight Float guifg=#e5ff9d gui=NONE
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
highlight Delimiter guifg=#67656a gui=NONE
highlight SpecialComment guifg=#67656a gui=NONE
highlight Debug guifg=#fc618d gui=NONE
highlight Underlined guifg=#5ad4e6 gui=UNDERLINE
highlight Ignore guifg=#67656a gui=NONE
highlight ErrorMsg guifg=#fc618d guibg=#19191a gui=BOLD
highlight WarningMsg guifg=#e5ff9d gui=NONE
highlight MoreMsg guifg=#7bd88f gui=NONE
highlight Question guifg=#7bd88f gui=NONE
highlight ModeMsg guifg=#f7f1ff gui=BOLD
highlight MatchParen guifg=#19191a guibg=#948ae3 gui=NONE

" Diff
highlight DiffAdd guifg=#7bd88f guibg=#19191a gui=NONE
highlight DiffChange guifg=#e5ff9d guibg=#19191a gui=NONE
highlight DiffDelete guifg=#fc618d guibg=#19191a gui=NONE
highlight DiffText guifg=#948ae3 guibg=#19191a gui=NONE

" Terminal colors (for :terminal)
if has('terminal')
  let g:terminal_color_0 = '#19191a'
  let g:terminal_color_1 = '#fc618d'
  let g:terminal_color_2 = '#7bd88f'
  let g:terminal_color_3 = '#e5ff9d'
  let g:terminal_color_4 = '#fd9353'
  let g:terminal_color_5 = '#948ae3'
  let g:terminal_color_6 = '#5ad4e6'
  let g:terminal_color_7 = '#f7f1ff'
  let g:terminal_color_8 = '#19191a'
  let g:terminal_color_9 = '#fc618d'
  let g:terminal_color_10 = '#7bd88f'
  let g:terminal_color_11 = '#e5ff9d'
  let g:terminal_color_12 = '#fd9353'
  let g:terminal_color_13 = '#948ae3'
  let g:terminal_color_14 = '#5ad4e6'
  let g:terminal_color_15 = '#f7f1ff'
endif
