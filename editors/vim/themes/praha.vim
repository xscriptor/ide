" Vim color file
" Xscriptor Praha
" Maintainer: Xscriptor
" Generated from colors.json

set background=dark
highlight clear
if exists("syntax_on")
    syntax reset
endif
let g:colors_name="xscriptor_praha"

" UI
highlight Normal guifg=#ffffff guibg=#1a1a1a gui=NONE
highlight Cursor guifg=#1a1a1a guibg=#FF9AA2 gui=NONE
highlight LineNr guifg=#6272A4 guibg=#1a1a1a gui=NONE
highlight CursorLineNr guifg=#FF9AA2 guibg=#252525 gui=NONE
highlight CursorLine guibg=#252525 gui=NONE
highlight Visual guibg=#3c3c3c gui=NONE
highlight Search guifg=#1a1a1a guibg=#FFE4A3 gui=NONE
highlight IncSearch guifg=#1a1a1a guibg=#BD93F9 gui=NONE
highlight StatusLine guifg=#ffffff guibg=#1A1A1A gui=NONE
highlight StatusLineNC guifg=#6272A4 guibg=#1A1A1A gui=NONE
highlight VertSplit guifg=#6272A4 guibg=#1A1A1A gui=NONE
highlight TabLine guifg=#6272A4 guibg=#1A1A1A gui=NONE
highlight TabLineFill guifg=#6272A4 guibg=#1A1A1A gui=NONE
highlight TabLineSel guifg=#ffffff guibg=#1a1a1a gui=NONE
highlight Pmenu guifg=#ffffff guibg=#1A1A1A gui=NONE
highlight PmenuSel guifg=#1a1a1a guibg=#FF9AA2 gui=NONE
highlight PmenuSbar guibg=#6272A4 gui=NONE
highlight PmenuThumb guibg=#FF9AA2 gui=NONE
highlight Directory guifg=#8BE9FD gui=NONE
highlight NonText guifg=#6272A4 gui=NONE
highlight SpecialKey guifg=#6272A4 gui=NONE
highlight Title guifg=#BD93F9 gui=BOLD
highlight Conceal guifg=#FF9AA2 guibg=#1a1a1a gui=NONE
highlight SpellBad guisp=#FF5555 gui=undercurl
highlight SpellCap guisp=#FFE4A3 gui=undercurl
highlight SpellRare guisp=#FF9AA2 gui=undercurl
highlight SpellLocal guisp=#8BE9FD gui=undercurl
highlight ColorColumn guibg=#252525 gui=NONE
highlight Folded guifg=#6272A4 guibg=#252525 gui=NONE
highlight FoldColumn guifg=#6272A4 guibg=#1a1a1a gui=NONE
highlight SignColumn guifg=#ffffff guibg=#1a1a1a gui=NONE
highlight Todo guifg=#FFE4A3 guibg=#1a1a1a gui=BOLD,ITALIC
highlight Error guifg=#FF5555 guibg=#1a1a1a gui=BOLD

" Syntax
highlight Comment guifg=#6272A4 gui=ITALIC
highlight Constant guifg=#FFE4A3 gui=NONE
highlight String guifg=#B8E6A0 gui=NONE
highlight Character guifg=#FF5555 gui=NONE
highlight Number guifg=#FFE4A3 gui=NONE
highlight Boolean guifg=#FFE4A3 gui=NONE
highlight Float guifg=#FFE4A3 gui=NONE
highlight Identifier guifg=#ffffff gui=NONE
highlight Function guifg=#BD93F9 gui=NONE
highlight Statement guifg=#FF9AA2 gui=NONE
highlight Conditional guifg=#FF9AA2 gui=NONE
highlight Repeat guifg=#FF9AA2 gui=NONE
highlight Label guifg=#FF9AA2 gui=NONE
highlight Operator guifg=#FF9AA2 gui=NONE
highlight Keyword guifg=#FF9AA2 gui=NONE
highlight Exception guifg=#FF9AA2 gui=NONE
highlight PreProc guifg=#FF6E6E gui=NONE
highlight Include guifg=#FF6E6E gui=NONE
highlight Define guifg=#FF6E6E gui=NONE
highlight Macro guifg=#FF6E6E gui=NONE
highlight PreCondit guifg=#FF6E6E gui=NONE
highlight Type guifg=#8BE9FD gui=NONE
highlight StorageClass guifg=#FF9AA2 gui=NONE
highlight Structure guifg=#8BE9FD gui=NONE
highlight Typedef guifg=#8BE9FD gui=NONE
highlight Special guifg=#BD93F9 gui=NONE
highlight SpecialChar guifg=#FF5555 gui=NONE
highlight Tag guifg=#FF5555 gui=NONE
highlight Delimiter guifg=#6272A4 gui=NONE
highlight SpecialComment guifg=#6272A4 gui=NONE
highlight Debug guifg=#FF5555 gui=NONE
highlight Underlined guifg=#8BE9FD gui=UNDERLINE
highlight Ignore guifg=#6272A4 gui=NONE
highlight ErrorMsg guifg=#FF5555 guibg=#1a1a1a gui=BOLD
highlight WarningMsg guifg=#FFE4A3 gui=NONE
highlight MoreMsg guifg=#B8E6A0 gui=NONE
highlight Question guifg=#B8E6A0 gui=NONE
highlight ModeMsg guifg=#ffffff gui=BOLD
highlight MatchParen guifg=#1a1a1a guibg=#FF9AA2 gui=NONE

" Diff
highlight DiffAdd guifg=#B8E6A0 guibg=#1a1a1a gui=NONE
highlight DiffChange guifg=#FFE4A3 guibg=#1a1a1a gui=NONE
highlight DiffDelete guifg=#FF5555 guibg=#1a1a1a gui=NONE
highlight DiffText guifg=#FF9AA2 guibg=#1a1a1a gui=NONE

" Terminal colors (for :terminal)
if has('terminal')
  let g:terminal_color_0 = '#1A1A1A'
  let g:terminal_color_1 = '#FF5555'
  let g:terminal_color_2 = '#B8E6A0'
  let g:terminal_color_3 = '#FFE4A3'
  let g:terminal_color_4 = '#BD93F9'
  let g:terminal_color_5 = '#FF9AA2'
  let g:terminal_color_6 = '#8BE9FD'
  let g:terminal_color_7 = '#FFFFFF'
  let g:terminal_color_8 = '#6272A4'
  let g:terminal_color_9 = '#FF6E6E'
  let g:terminal_color_10 = '#B8E6A0'
  let g:terminal_color_11 = '#FFE4A3'
  let g:terminal_color_12 = '#D6ACFF'
  let g:terminal_color_13 = '#FF9AA2'
  let g:terminal_color_14 = '#A4FFFF'
  let g:terminal_color_15 = '#FFFFFF'
endif
