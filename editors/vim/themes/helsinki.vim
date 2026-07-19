" Vim color file
" Xscriptor Helsinki
" Maintainer: Xscriptor
" Generated from colors.json

set background=light
highlight clear
if exists("syntax_on")
    syntax reset
endif
let g:colors_name="xscriptor_helsinki"

" UI
highlight Normal guifg=#544d40 guibg=#f8fafe gui=NONE
highlight Cursor guifg=#f8fafe guibg=#3e9d21 gui=NONE
highlight LineNr guifg=#8d8a82 guibg=#f8fafe gui=NONE
highlight CursorLineNr guifg=#3e9d21 guibg=#f0f1f4 gui=NONE
highlight CursorLine guibg=#f0f1f4 gui=NONE
highlight Visual guibg=#dfe0e2 gui=NONE
highlight Search guifg=#f8fafe guibg=#2e70ad gui=NONE
highlight IncSearch guifg=#f8fafe guibg=#b55a0f gui=NONE
highlight StatusLine guifg=#544d40 guibg=#f8fafe gui=NONE
highlight StatusLineNC guifg=#8d8a82 guibg=#f8fafe gui=NONE
highlight VertSplit guifg=#8d8a82 guibg=#f8fafe gui=NONE
highlight TabLine guifg=#8d8a82 guibg=#f8fafe gui=NONE
highlight TabLineFill guifg=#8d8a82 guibg=#f8fafe gui=NONE
highlight TabLineSel guifg=#544d40 guibg=#f8fafe gui=NONE
highlight Pmenu guifg=#544d40 guibg=#f8fafe gui=NONE
highlight PmenuSel guifg=#f8fafe guibg=#3e9d21 gui=NONE
highlight PmenuSbar guibg=#b0a999 gui=NONE
highlight PmenuThumb guibg=#3e9d21 gui=NONE
highlight Directory guifg=#bd4c3d gui=NONE
highlight NonText guifg=#8d8a82 gui=NONE
highlight SpecialKey guifg=#8d8a82 gui=NONE
highlight Title guifg=#b55a0f gui=BOLD
highlight Conceal guifg=#3e9d21 guibg=#f8fafe gui=NONE
highlight SpellBad guisp=#1faa9e gui=undercurl
highlight SpellCap guisp=#2e70ad gui=undercurl
highlight SpellRare guisp=#3e9d21 gui=undercurl
highlight SpellLocal guisp=#bd4c3d gui=undercurl
highlight ColorColumn guibg=#f0f1f4 gui=NONE
highlight Folded guifg=#8d8a82 guibg=#f0f1f4 gui=NONE
highlight FoldColumn guifg=#8d8a82 guibg=#f8fafe gui=NONE
highlight SignColumn guifg=#544d40 guibg=#f8fafe gui=NONE
highlight Todo guifg=#2e70ad guibg=#f8fafe gui=BOLD,ITALIC
highlight Error guifg=#1faa9e guibg=#f8fafe gui=BOLD

" Syntax
highlight Comment guifg=#8d8a82 gui=ITALIC
highlight Constant guifg=#2e70ad gui=NONE
highlight String guifg=#733d9a gui=NONE
highlight Character guifg=#1faa9e gui=NONE
highlight Number guifg=#2e70ad gui=NONE
highlight Boolean guifg=#2e70ad gui=NONE
highlight Float guifg=#2e70ad gui=NONE
highlight Identifier guifg=#544d40 gui=NONE
highlight Function guifg=#b55a0f gui=NONE
highlight Statement guifg=#3e9d21 gui=NONE
highlight Conditional guifg=#3e9d21 gui=NONE
highlight Repeat guifg=#3e9d21 gui=NONE
highlight Label guifg=#3e9d21 gui=NONE
highlight Operator guifg=#3e9d21 gui=NONE
highlight Keyword guifg=#3e9d21 gui=NONE
highlight Exception guifg=#3e9d21 gui=NONE
highlight PreProc guifg=#009e91 gui=NONE
highlight Include guifg=#009e91 gui=NONE
highlight Define guifg=#009e91 gui=NONE
highlight Macro guifg=#009e91 gui=NONE
highlight PreCondit guifg=#009e91 gui=NONE
highlight Type guifg=#bd4c3d gui=NONE
highlight StorageClass guifg=#3e9d21 gui=NONE
highlight Structure guifg=#bd4c3d gui=NONE
highlight Typedef guifg=#bd4c3d gui=NONE
highlight Special guifg=#b55a0f gui=NONE
highlight SpecialChar guifg=#1faa9e gui=NONE
highlight Tag guifg=#1faa9e gui=NONE
highlight Delimiter guifg=#8d8a82 gui=NONE
highlight SpecialComment guifg=#8d8a82 gui=NONE
highlight Debug guifg=#1faa9e gui=NONE
highlight Underlined guifg=#bd4c3d gui=UNDERLINE
highlight Ignore guifg=#8d8a82 gui=NONE
highlight ErrorMsg guifg=#1faa9e guibg=#f8fafe gui=BOLD
highlight WarningMsg guifg=#2e70ad gui=NONE
highlight MoreMsg guifg=#733d9a gui=NONE
highlight Question guifg=#733d9a gui=NONE
highlight ModeMsg guifg=#544d40 gui=BOLD
highlight MatchParen guifg=#f8fafe guibg=#3e9d21 gui=NONE

" Diff
highlight DiffAdd guifg=#733d9a guibg=#f8fafe gui=NONE
highlight DiffChange guifg=#2e70ad guibg=#f8fafe gui=NONE
highlight DiffDelete guifg=#1faa9e guibg=#f8fafe gui=NONE
highlight DiffText guifg=#3e9d21 guibg=#f8fafe gui=NONE

" Terminal colors (for :terminal)
if has('terminal')
  let g:terminal_color_0 = '#f8fafe'
  let g:terminal_color_1 = '#1faa9e'
  let g:terminal_color_2 = '#733d9a'
  let g:terminal_color_3 = '#2e70ad'
  let g:terminal_color_4 = '#b55a0f'
  let g:terminal_color_5 = '#3e9d21'
  let g:terminal_color_6 = '#bd4c3d'
  let g:terminal_color_7 = '#544d40'
  let g:terminal_color_8 = '#b0a999'
  let g:terminal_color_9 = '#009e91'
  let g:terminal_color_10 = '#5a1f8a'
  let g:terminal_color_11 = '#0f5ba2'
  let g:terminal_color_12 = '#b23b00'
  let g:terminal_color_13 = '#218c00'
  let g:terminal_color_14 = '#b32e1f'
  let g:terminal_color_15 = '#000000'
endif
