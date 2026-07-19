" Vim color file
" Xscriptor Oslo
" Maintainer: Xscriptor
" Generated from colors.json

set background=dark
highlight clear
if exists("syntax_on")
    syntax reset
endif
let g:colors_name="xscriptor_oslo"

" UI
highlight Normal guifg=#abb2bf guibg=#3f4451 gui=NONE
highlight Cursor guifg=#3f4451 guibg=#c162de gui=NONE
highlight LineNr guifg=#959ca9 guibg=#3f4451 gui=NONE
highlight CursorLineNr guifg=#c162de guibg=#444a56 gui=NONE
highlight CursorLine guibg=#444a56 gui=NONE
highlight Visual guibg=#4f5462 gui=NONE
highlight Search guifg=#3f4451 guibg=#d18f52 gui=NONE
highlight IncSearch guifg=#3f4451 guibg=#4aa5f0 gui=NONE
highlight StatusLine guifg=#abb2bf guibg=#3f4451 gui=NONE
highlight StatusLineNC guifg=#959ca9 guibg=#3f4451 gui=NONE
highlight VertSplit guifg=#959ca9 guibg=#3f4451 gui=NONE
highlight TabLine guifg=#959ca9 guibg=#3f4451 gui=NONE
highlight TabLineFill guifg=#959ca9 guibg=#3f4451 gui=NONE
highlight TabLineSel guifg=#abb2bf guibg=#3f4451 gui=NONE
highlight Pmenu guifg=#abb2bf guibg=#3f4451 gui=NONE
highlight PmenuSel guifg=#3f4451 guibg=#c162de gui=NONE
highlight PmenuSbar guibg=#4f5666 gui=NONE
highlight PmenuThumb guibg=#c162de gui=NONE
highlight Directory guifg=#42b3c2 gui=NONE
highlight NonText guifg=#959ca9 gui=NONE
highlight SpecialKey guifg=#959ca9 gui=NONE
highlight Title guifg=#4aa5f0 gui=BOLD
highlight Conceal guifg=#c162de guibg=#3f4451 gui=NONE
highlight SpellBad guisp=#e05561 gui=undercurl
highlight SpellCap guisp=#d18f52 gui=undercurl
highlight SpellRare guisp=#c162de gui=undercurl
highlight SpellLocal guisp=#42b3c2 gui=undercurl
highlight ColorColumn guibg=#444a56 gui=NONE
highlight Folded guifg=#959ca9 guibg=#444a56 gui=NONE
highlight FoldColumn guifg=#959ca9 guibg=#3f4451 gui=NONE
highlight SignColumn guifg=#abb2bf guibg=#3f4451 gui=NONE
highlight Todo guifg=#d18f52 guibg=#3f4451 gui=BOLD,ITALIC
highlight Error guifg=#e05561 guibg=#3f4451 gui=BOLD

" Syntax
highlight Comment guifg=#959ca9 gui=ITALIC
highlight Constant guifg=#d18f52 gui=NONE
highlight String guifg=#8cc265 gui=NONE
highlight Character guifg=#e05561 gui=NONE
highlight Number guifg=#d18f52 gui=NONE
highlight Boolean guifg=#d18f52 gui=NONE
highlight Float guifg=#d18f52 gui=NONE
highlight Identifier guifg=#abb2bf gui=NONE
highlight Function guifg=#4aa5f0 gui=NONE
highlight Statement guifg=#c162de gui=NONE
highlight Conditional guifg=#c162de gui=NONE
highlight Repeat guifg=#c162de gui=NONE
highlight Label guifg=#c162de gui=NONE
highlight Operator guifg=#c162de gui=NONE
highlight Keyword guifg=#c162de gui=NONE
highlight Exception guifg=#c162de gui=NONE
highlight PreProc guifg=#ff616e gui=NONE
highlight Include guifg=#ff616e gui=NONE
highlight Define guifg=#ff616e gui=NONE
highlight Macro guifg=#ff616e gui=NONE
highlight PreCondit guifg=#ff616e gui=NONE
highlight Type guifg=#42b3c2 gui=NONE
highlight StorageClass guifg=#c162de gui=NONE
highlight Structure guifg=#42b3c2 gui=NONE
highlight Typedef guifg=#42b3c2 gui=NONE
highlight Special guifg=#4aa5f0 gui=NONE
highlight SpecialChar guifg=#e05561 gui=NONE
highlight Tag guifg=#e05561 gui=NONE
highlight Delimiter guifg=#959ca9 gui=NONE
highlight SpecialComment guifg=#959ca9 gui=NONE
highlight Debug guifg=#e05561 gui=NONE
highlight Underlined guifg=#42b3c2 gui=UNDERLINE
highlight Ignore guifg=#959ca9 gui=NONE
highlight ErrorMsg guifg=#e05561 guibg=#3f4451 gui=BOLD
highlight WarningMsg guifg=#d18f52 gui=NONE
highlight MoreMsg guifg=#8cc265 gui=NONE
highlight Question guifg=#8cc265 gui=NONE
highlight ModeMsg guifg=#abb2bf gui=BOLD
highlight MatchParen guifg=#3f4451 guibg=#c162de gui=NONE

" Diff
highlight DiffAdd guifg=#8cc265 guibg=#3f4451 gui=NONE
highlight DiffChange guifg=#d18f52 guibg=#3f4451 gui=NONE
highlight DiffDelete guifg=#e05561 guibg=#3f4451 gui=NONE
highlight DiffText guifg=#c162de guibg=#3f4451 gui=NONE

" Terminal colors (for :terminal)
if has('terminal')
  let g:terminal_color_0 = '#3f4451'
  let g:terminal_color_1 = '#e05561'
  let g:terminal_color_2 = '#8cc265'
  let g:terminal_color_3 = '#d18f52'
  let g:terminal_color_4 = '#4aa5f0'
  let g:terminal_color_5 = '#c162de'
  let g:terminal_color_6 = '#42b3c2'
  let g:terminal_color_7 = '#e6e6e6'
  let g:terminal_color_8 = '#4f5666'
  let g:terminal_color_9 = '#ff616e'
  let g:terminal_color_10 = '#a5e075'
  let g:terminal_color_11 = '#f0a45d'
  let g:terminal_color_12 = '#4dc4ff'
  let g:terminal_color_13 = '#de73ff'
  let g:terminal_color_14 = '#4cd1e0'
  let g:terminal_color_15 = '#ffffff'
endif
