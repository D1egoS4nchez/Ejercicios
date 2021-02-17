syntax on


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

" Configuración de fondo y colortheme --------------------------------
set termguicolors
set background=dark


"Inicio de llamada de los Plugins

call plug#begin('~/.local/share/nvim/plugged')
          "Plugin para nerdtree y selección de archivos
Plug 'scrooloose/nerdtree'

          "Plugin para Airline, barrada de estado
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'  " Temas para airline

          "Plugin para el autocompletado
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
Plug 'Shougo/neco-syntax'  " Fuente general de auto completado
Plug 'deoplete-plugins/deoplete-jedi'
if has('nvim')
  Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
else
  Plug 'Shougo/deoplete.nvim'
  Plug 'roxma/nvim-yarp'
  Plug 'roxma/vim-hug-neovim-rpc'
endif

          "Navegar entre las sugerencias de deoplete usando Tab
Plug 'ervandew/supertab'

          "CSS
Plug 'hail2u/vim-css3-syntax', { 'for': 'css' }
          "HTML
Plug 'othree/html5.vim', { 'for': 'html' }

          "Incsearch
Plug 'haya14busa/incsearch.vim'


          "Comandos de git
Plug 'tpope/vim-fugitive'
          
        "Afterglow
Plug 'danilo-augusto/vim-afterglow'

        "IdentLine
Plug 'Yggdroot/indentLine'
        "snippets
Plug 'sirver/ultisnips'
Plug 'honza/vim-snippets'

"Se termina de llamar  a los plugins
call plug#end() "Configuración de Nerd Tree ----------------------------------------- 
let g:NERDTreeChDirMode = 2  " Cambia el directorio actual al nodo padre actual Abrir/cerrar NERDTree con F2
map <F2> :NERDTreeToggle<CR>
"--------------------------------------------------------------------
"
"Configuracion para barrakjkj de estado ----------------------------------
let g:airline#extensions#tabline#enabled = 1  " Mostrar buffers abiertos (como pestañas)
let g:airline#extensions#tabline#fnamemod = ':t'  " Mostrar sólo el nombre del archivo
" Cargar fuente Powerline y símbolos (ver nota) 
let g:airline_powerline_fonts = 1
let g:afterglow_blackout=1
let g:afterglow_italic_comments=1
let g:afterglow_use_italics=1
let g:afterglow_inherit_background=1
let g:airline_theme='afterglow'

set noshowmode  " No mostrar el modo actual (YA lo muestra la barra de estado)
"
"----------------------------------------------------------------------
"
"Autocompletado de lineas --------------------------------------------
"" Activar deoplete al iniciar Neovim
let g:deoplete#enable_at_startup = 1

" Cerrar automaticamente la ventana de vista previa (donde se muestra documentación, si existe)
augroup deopleteCompleteDoneAu
  autocmd!
  autocmd CompleteDone * silent! pclose!
augroup END

let g:python3_host_prog = '/bin/python3'
"---------------------------------------------------------------------
"
"Supertab -----------------------------------------------------------
"
" Invertir direccion de navegacion (de arriba a abajo)
let g:SuperTabDefaultCompletionType = '<c-n>'
"-------------------------------------------------------------------
"
"Incsearch ---------------------------------------------------------
"
" Maps requeridos
map /  <Plug>(incsearch-forward)
map ?  <Plug>(incsearch-backward)

" Quitar resaltado luego de buscar
let g:incsearch#auto_nohlsearch = 1
"------------------------------------------------------------------
"
colorscheme afterglow

"INdentLine------------------------------------------------------------------
"
"" No mostrar en ciertos tipos de buffers y archivos
let g:indentLine_fileTypeExclude = ['text', 'sh', 'help', 'terminal']
let g:indentLine_bufNameExclude = ['NERD_tree.*', 'term:.*']

" -----------------------------------------------------------------------
"
"  html5 Configuración ---------------------------------------------------
"
let g:html5_event_handler_attributes_complete = 1
let g:html5_rdfa_attributes_complete = 1
let g:html5_microdata_attributes_complete = 1
let html_no_rendering=1
let g:html5_aria_attributes_complete = 1
"set syntax=htmlos
"VimCSS3Syntax  --------------------------------------------------------------------
augroup VimCSS3Syntax
  autocmd!

  autocmd FileType css setlocal iskeyword+=-
augroup END

" ------------------------------------------------------------------------


" snippets, partes de codigo reutilizables ----------------------------------------

" Expandir snippet con Ctrl + j
let g:UltiSnipsExpandTrigger = '<c-j>'

" Ir a siguiente ubicacion con Ctrl + j
let g:UltiSnipsJumpForwardTrigger = '<c-j>'
" Ir a anterior ubicacion con Ctrl + k
let g:UltiSnipsJumpBackwardTrigger = '<c-k>'
