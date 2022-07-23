256 Constant buffer-size
Create line-buffer buffer-size 2 + allot
2000 Constant max-lines
Create numbers max-lines cells allot

0 Value nb-lines
99999999999 Constant huge

: solve-01-1 ( -- result )
    0 huge ( result prev )
    numbers nb-lines cells bounds do
        i @ ( result prev n )
        2dup <
        if
            rot 1+ -rot \ increment result
        then
        swap drop ( result n )
    cell +loop drop ( result ) ;

: sum-first-n ( addr n -- sum )
    0 -rot ( result addr n )
    cells bounds do ( result )
        i @ +
    cell +loop ;

: has-bigger-sum ( addr-prevs n -- flag )
    swap dup 3 sum-first-n ( n addr-prevs prevs-sum )
    swap 2 sum-first-n rot +  ( prevs-sum new-sum )
    < ;

: shift-previous ( addr-prevs n -- addr-prevs )
    swap dup cell+ @ over 2 cells + !
    dup @ over cell+ !
    dup -rot ! ;

: solve-01-2 ( -- result )
    0 here huge , huge , huge , ( count addr-prevs )
    nb-lines 0 do
        numbers i cells + @ ( count addr-prevs n )
        2dup has-bigger-sum
        if
            rot 1+ -rot ( count+1 addr-prevs n )
        then
        shift-previous ( count addr-prevs )
    loop drop ( count ) ;

: parse-lines ( dst-addr -- )
    next-arg r/o open-file throw >r

    begin
        line-buffer buffer-size r@ read-line throw
    while ( dst-addr nb-read-chars )
        line-buffer swap s>number? 2drop ( dst-addr n )
        over nb-lines cells + !
        nb-lines 1+ to nb-lines
    repeat drop

    r> close-file throw ;

numbers parse-lines
solve-01-1 . cr
solve-01-2 . cr
bye
