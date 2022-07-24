0 Value file-id
256 Constant buffer-size
Create line-buffer buffer-size 2 + allot

: increment-2nd
    swap 1+ swap ;

: increment-3rd
    rot 1+ -rot ;

: halt
    .s bye ;

: parse-lines { dst-addr -- nb-lines }
    next-arg r/o open-file throw to file-id

    0 dst-addr
    begin
        line-buffer buffer-size file-id read-line throw
    while ( dst-addr nb-read-chars )
        line-buffer swap s>number? 2drop ( dst-addr n )
        over !         \ store number
        cell+          \ increment destination address
        increment-2nd  \ increment line counter
    repeat 2drop

    file-id close-file throw ;