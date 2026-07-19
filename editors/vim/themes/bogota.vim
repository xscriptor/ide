" Vim color file
" Xscriptor Bogota
" Maintainer: Xscriptor
" Generated from colors.json

set background=dark
highlight clear
if exists("syntax_on")
    syntax reset
endif
let g:colors_name="xscriptor_bogota"

" UI
highlight Normal guifg=#f7f1ff guibg=#200b0a gui=NONE
highlight Cursor guifg=#200b0a guibg=#ff9999 gui=NONE
highlight LineNr guifg=#8c7e84 guibg=#200b0a gui=NONE
highlight CursorLineNr guifg=#ff9999 guibg=#2b1616 gui=NONE
highlight CursorLine guibg=#2b1616 gui=NONE
highlight Visual guibg=#402e2f gui=NONE
highlight Search guifg=#200b0a guibg=#ffed89 gui=NONE
highlight IncSearch guifg=#200b0a guibg=#47e6ff gui=NONE
highlight StatusLine guifg=#f7f1ff guibg=#200b0a gui=NONE
highlight StatusLineNC guifg=#8c7e84 guibg=#200b0a gui=NONE
highlight VertSplit guifg=#8c7e84 guibg=#200b0a gui=NONE
highlight TabLine guifg=#8c7e84 guibg=#200b0a gui=NONE
highlight TabLineFill guifg=#8c7e84 guibg=#200b0a gui=NONE
highlight TabLineSel guifg=#f7f1ff guibg=#200b0a gui=NONE
highlight Pmenu guifg=#f7f1ff guibg=#200b0a gui=NONE
highlight PmenuSel guifg=#200b0a guibg=#ff9999 gui=NONE
highlight PmenuSbar guibg=#525053 gui=NONE
highlight PmenuThumb guibg=#ff9999 gui=NONE
highlight Directory guifg=#47e6ff gui=NONE
highlight NonText guifg=#8c7e84 gui=NONE
highlight SpecialKey guifg=#8c7e84 gui=NONE
highlight Title guifg=#47e6ff gui=BOLD
highlight Conceal guifg=#ff9999 guibg=#200b0a gui=NONE
highlight SpellBad guisp=#fc618d gui=undercurl
highlight SpellCap guisp=#ffed89 gui=undercurl
highlight SpellRare guisp=#ff9999 gui=undercurl
highlight SpellLocal guisp=#47e6ff gui=undercurl
highlight ColorColumn guibg=#2b1616 gui=NONE
highlight Folded guifg=#8c7e84 guibg=#2b1616 gui=NONE
highlight FoldColumn guifg=#8c7e84 guibg=#200b0a gui=NONE
highlight SignColumn guifg=#f7f1ff guibg=#200b0a gui=NONE
highlight Todo guifg=#ffed89 guibg=#200b0a gui=BOLD,ITALIC
highlight Error guifg=#fc618d guibg=#200b0a gui=BOLD

" Syntax
highlight Comment guifg=#8c7e84 gui=ITALIC
highlight Constant guifg=#ffed89 gui=NONE
highlight String guifg=#7bd88f gui=NONE
highlight Character guifg=#fc618d gui=NONE
highlight Number guifg=#ffed89 gui=NONE
highlight Boolean guifg=#ffed89 gui=NONE
highlight Float guifg=#ffed89 gui=NONE
highlight Identifier guifg=#f7f1ff gui=NONE
highlight Function guifg=#47e6ff gui=NONE
highlight Statement guifg=#ff9999 gui=NONE
highlight Conditional guifg=#ff9999 gui=NONE
highlight Repeat guifg=#ff9999 gui=NONE
highlight Label guifg=#ff9999 gui=NONE
highlight Operator guifg=#ff9999 gui=NONE
highlight Keyword guifg=#ff9999 gui=NONE
highlight Exception guifg=#ff9999 gui=NONE
highlight PreProc guifg=#fc618d gui=NONE
highlight Include guifg=#fc618d gui=NONE
highlight Define guifg=#fc618d gui=NONE
highlight Macro guifg=#fc618d gui=NONE
highlight PreCondit guifg=#fc618d gui=NONE
highlight Type guifg=#47e6ff gui=NONE
highlight StorageClass guifg=#ff9999 gui=NONE
highlight Structure guifg=#47e6ff gui=NONE
highlight Typedef guifg=#47e6ff gui=NONE
highlight Special guifg=#47e6ff gui=NONE
highlight SpecialChar guifg=#fc618d gui=NONE
highlight Tag guifg=#fc618d gui=NONE
highlight Delimiter guifg=#8c7e84 gui=NONE
highlight SpecialComment guifg=#8c7e84 gui=NONE
highlight Debug guifg=#fc618d gui=NONE
highlight Underlined guifg=#47e6ff gui=UNDERLINE
highlight Ignore guifg=#8c7e84 gui=NONE
highlight ErrorMsg guifg=#fc618d guibg=#200b0a gui=BOLD
highlight WarningMsg guifg=#ffed89 gui=NONE
highlight MoreMsg guifg=#7bd88f gui=NONE
highlight Question guifg=#7bd88f gui=NONE
highlight ModeMsg guifg=#f7f1ff gui=BOLD
highlight MatchParen guifg=#200b0a guibg=#ff9999 gui=NONE

" Diff
highlight DiffAdd guifg=#7bd88f guibg=#200b0a gui=NONE
highlight DiffChange guifg=#ffed89 guibg=#200b0a gui=NONE
highlight DiffDelete guifg=#fc618d guibg=#200b0a gui=NONE
highlight DiffText guifg=#ff9999 guibg=#200b0a gui=NONE

" Terminal colors (for :terminal)
if has('terminal')
  let g:terminal_color_0 = '#200b0a'
  let g:terminal_color_1 = '#fc618d'
  let g:terminal_color_2 = '#7bd88f'
  let g:terminal_color_3 = '#ffed89'
  let g:terminal_color_4 = '#47e6ff'
  let g:terminal_color_5 = '#ff9999'
  let g:terminal_color_6 = '#47e6ff'
  let g:terminal_color_7 = '#f7f1ff'
  let g:terminal_color_8 = '#525053'
  let g:terminal_color_9 = '#fc618d'
  let g:terminal_color_10 = '#7bd88f'
  let g:terminal_color_11 = '#ffed89'
  let g:terminal_color_12 = '#47e6ff'
  let g:terminal_color_13 = '#ff9999'
  let g:terminal_color_14 = '#47e6ff'
  let g:terminal_color_15 = '#f7f1ff'
endif
