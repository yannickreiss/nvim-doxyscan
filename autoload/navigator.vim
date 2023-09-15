function! navigator#Navigator()
    call OpenFloatingWindow("echo 'Hello'")
endfunction

function! OpenFloatingWindow(command)
    " Create a new scratch buffer for the floating window
    let buffer = nvim_create_buf(v:false, v:true)

    let window_width = float2nr( winwidth(0) * 0.8 )
    let window_height = float2nr( winheight(0) * 0.8 )

    let window_x = ( winwidth(0) - window_width ) / 2
    let window_y = ( winheight(0) - window_height ) / 2
    " Create a floating window for the buffer
    let options = {
        \ 'relative': 'editor',
        \ 'row': float2nr(window_y),
        \ 'col': float2nr(window_x),
        \ 'width': window_width,
        \ 'height': window_height,
        \ 'anchor': 'NW',
        \ 'style': 'minimal',
        \ 'border': 'single'
        \ }
    let window = nvim_open_win(buffer, v:true, options)

    " Run the specified command in the buffer
    call nvim_buf_set_lines(buffer, 0, -1, v:true, split(execute(a:command), "\n"))
    nnoremap <buffer> q :call CloseFloatingWindow()<CR>

    " Set the buffer to be unmodifiable
    call nvim_buf_set_option(buffer, 'modifiable', v:false)
endfunction

function CloseFloatingWindow()
    call nvim_win_close(0, v:true)
endfunction
