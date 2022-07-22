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

: sum-two ( addr -- sum )
    dup @ swap cell+ @ + ;

: sum-three ( addr -- sum )
    dup sum-two swap 2 cells + @ + ;

: has-bigger-sum ( addr-prevs n -- flag )
    swap dup sum-three ( n addr-prevs prevs-sum )
    swap sum-two rot +  ( prevs-sum new-sum )
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
solve-01-2 . cr
bye
