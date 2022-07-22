256 Constant buffer-size
Create line-buffer buffer-size 2 + allot
2000 Constant max-lines
Create numbers max-lines cells allot

0 Value nb-lines
99999999999 Constant huge

: solve-01-1 ( -- result )
    0 huge ( count prev )
    nb-lines 0 do
        numbers i cells + @ ( count prev n )
        2dup <
        if
            rot 1+ -rot ( count+1 prev n )
        then
        swap drop ( count n )
    loop drop ( count ) ;

: parse-lines
    next-arg r/o open-file throw >r

    begin
        line-buffer buffer-size r@ read-line throw
    while ( nb-read-chars )
        line-buffer swap s>number? 2drop ( n )
        numbers nb-lines cells + !
        nb-lines 1+ to nb-lines
    repeat drop

    r> close-file throw ;

parse-lines
solve-01-1 . cr
bye
