set nocompatible

syntax on
set t_Co=256
hi Normal guibg=NONE ctermbg=NONE

set hidden
"set wildmenu
set showcmd
set clipboard=unnamedplus    " use the clipboards of vim and win

filetype plugin indent on
"set backspace=indent,eol,start
"set autoindent
set cindent
set tabstop=2
set shiftwidth=2
set softtabstop=2
set expandtab

set scrolloff=20

set laststatus=2
set confirm

set number
" set foldcolumn=1

set wrap linebreak nolist

" enable man pages
"runtime ftplugin/man.vim
"nnoremap K :Man <cword> <Cr>

" mouse support
"set mouse=a

" spellcheck
set spelllang=de

" yank to end of line
map Y y$

" better leader
map <space> <leader>

" always move up/down to the next visual line
map j gj
map k gk

" change behavior of move to beginning of line
noremap 0 ^
noremap ^ 0

" easier commands
noremap ; :
noremap <M-;> ;

" toggle buffers
nnoremap <C-d> <C-^>
inoremap <C-d> <esc><C-^>

" search settings
set hlsearch
set ignorecase
set smartcase
"map ?  <Plug>(incsearch-backward)
"map g/ <Plug>(incsearch-stay)

" backup files"
set nobackup

" open vimrc
nmap <leader>v :tabedit $MYVIMRC<CR>

" disabling autocomment"
autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o

" copy & paste using VISUAL selection
" only available after installing gVim
set guioptions+=a

" --------------------- vim-plug --------------------- "
" visit github page of vimplug for more information "

" Specify a directory for plugins
call plug#begin('~/.vim/plugged')

" syntastic
" syntax checking hack for vim
"Plug 'scrooloose/syntastic'

" vim-sensible
Plug 'tpope/vim-sensible'

" command-t
"Plug 'wincent/command-t', {
"    \   'do': 'cd ruby/command-t/ext/command-t && ruby extconf.rb && make'
"\ }

call plug#end()
" --------------------- vim-plug --------------------- "

