" Title:        Navigator
" Description:  Find functions in buffer(s)
" Last Change:  Fri 15 Sep 2023 09:08:45 CEST
" Maintainer:   Yannick Reiss <yannick.reiss@protonmail.ch>

" Prevent multiple load of the plugin
if exists("g:loaded_navigator")
    finish
endif

let g:loaded_navigator  =   1

command!    -nargs=0 Navigator call navigator#Navigator()
