0 Value file-id
256 Constant buffer-size
Create line-buffer buffer-size 2 + allot

: increment-2nd
    swap 1+ swap ;

: increment-3rd
    rot 1+ -rot ;

: .scr
    .s cr ;

: halt
    .s cr bye ;

: checkEmptyStack ( -- )
    assert( depth 0 = ) ;

: parse-number ( c-addr u -- n )
    s>number? drop d>s ;

: parse-lines { dst-addr parse-xt -- nb-lines }
    \ parse-xt ( c-addr u -- parsed-line )
    next-arg r/o open-file throw to file-id

    0 dst-addr
    begin
        line-buffer buffer-size file-id read-line throw
    while ( dst-addr nb-read-chars )
        line-buffer swap parse-xt execute ( dst-addr parsed-res-addr )
        over !   \ store parsed result address
        cell+    \ increment destination address
        increment-2nd  \ increment line counter
    repeat 2drop

    file-id close-file throw ;
