256 Constant buffer-size
Create line-buffer buffer-size 2 + allot

: parse-lines ( dst-addr -- nb-lines )
    0 swap ( nb-lines dst-addr )
    next-arg r/o open-file throw >r

    begin
        line-buffer buffer-size r@ read-line throw
    while ( dst-addr nb-read-chars )
        line-buffer swap s>number? 2drop ( dst-addr n )
        swap cell+ swap
        over !
        swap 1+ swap
    repeat 2drop

    r> close-file throw ;
