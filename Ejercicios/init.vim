syntax on

" Directorio de plugins
call plug#begin('~/.local/share/nvim/plugged')

Plug 'tpope/vim-surround'  " Es buena idea agregar una descripción del plugin
Plug 'joshdick/onedark.vim' " Tema one dark
Plug 'scrooloose/nerdtree' "Exploracion de archivos
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'  " Temas para airline
Plug 'Yggdroot/indentLine' "Lineas de identacion
Plug 'iCyMind/NeoSolarized'
Plug 'deoplete-plugins/deoplete-jedi'
Plug 'sirver/ultisnips'
Plug 'honza/vim-snippets'
Plug 'haya14busa/incsearch.vim'
Plug 'danilo-augusto/vim-afterglow'


call plug#end()



set mouse=a
set noerrorbells
set sw=2
set expandtab
set smartindent 
set numberwidth=1
set number
set rnu
set nowrap
set noswapfile
set clipboard=unnamedplus
set ignorecase


set colorcolumn=120
highlight ColoColumn ctermbg=0 guibg=lightgrey

" Aqui se van a llamar las configuraciones de los plugin
"
set termguicolors  " Activa true colors en la terminal
set background=dark  " Fondo del tema: dark/light
colorscheme afterglow  " Activa tema NeoSolarized

let g:NERDTreeChDirMode = 2  " Cambia el directorio actual al nodo padre actual

" Abrir/cerrar NERDTree con F2
map <F2> :NERDTreeToggle<CR>
" No mostrar en ciertos tipos de buffers y archivos
let g:indentLine_fileTypeExclude = ['text', 'sh', 'help', 'terminal']
let g:indentLine_bufNameExclude = ['NERD_tree.*', 'term:.*']


let g:airline#extensions#tabline#enabled = 1  " Mostrar buffers abiertos (como pestañas)
let g:airline#extensions#tabline#fnamemod = ':t'  " Mostrar sólo el nombre del archivo

" Cargar fuente Powerline y símbolos (ver nota)
let g:airline_powerline_fonts = 1
let g:airline_theme='afterglow'
set noshowmode  " No mostrar el modo actual (ya lo muestra la barra de estado)

let g:UltiSnipsExpandTrigger = '<c-j>'

" Ir a siguiente ubicacion con Ctrl + j
let g:UltiSnipsJumpForwardTrigger = '<c-j>'
" Ir a anterior ubicacion con Ctrl + k
let g:UltiSnipsJumpBackwardTrigger = '<c-k>'

" Maps requeridos
map /  <Plug>(incsearch-forward)
map ?  <Plug>(incsearch-backward)

" Quitar resaltado luego de buscar
let g:incsearch#auto_nohlsearch = 1

let g:afterglow_blackout=1
let g:afterglow_italic_comments=1
let g:afterglow_use_italics=1
let g:afterglow_inherit_background=1
let g:airline_theme='afterglow'
