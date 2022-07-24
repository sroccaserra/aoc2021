256 Constant buffer-size
Create line-buffer buffer-size 2 + allot

: increment-2nd
    swap 1+ swap ;

: increment-3rd
    rot 1+ -rot ;

: halt
    .s bye ;

: parse-lines ( dst-addr -- nb-lines )
    0 swap ( nb-lines dst-addr )
    next-arg r/o open-file throw >r

    begin
        line-buffer buffer-size r@ read-line throw
    while ( dst-addr nb-read-chars )
        line-buffer swap s>number? 2drop ( dst-addr n )
        over !         \ store number
        cell+          \ increment destination address
        increment-2nd  \ increment line counter
    repeat 2drop

    r> close-file throw ;
