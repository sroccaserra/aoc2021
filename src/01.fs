require common/common.fs

0 Value nb-lines
2000 Constant max-lines
Create numbers max-lines cells allot

99999999999 Constant huge

: solve-01-1 ( -- result )
    assert( nb-lines max-lines <= )
    0 huge ( result prev )
    numbers nb-lines cells bounds do
        i @ ( result prev n )
        2dup < if
            inc-3rd \ result++
        then
        nip ( result n )
    cell +loop drop ( result ) ;

: sum-first-n ( addr n -- sum )
    0 -rot ( result addr n )
    cells bounds do ( result )
        i @ +
    cell +loop ;

: has-bigger-sum { addr-prevs n -- flag }
    addr-prevs 3 sum-first-n
    addr-prevs 2 sum-first-n n +
    < ;

: .1st ;
: .2nd cell+ ;
: .3rd [ 2 cells ] literal + ;
: shift-previous ( n addr-prevs -- )
    dup .2nd @ over .3rd !
    dup .1st @ over .2nd !
    ( n addr-prevs ) .1st ! ;

: solve-01-2 ( -- result )
    0 >r here huge , huge , huge , ( addr-prevs )
    numbers nb-lines cells bounds begin
        rot  ( end-addr addr addr-prevs )
        over @  ( ... addr-prevs n )
        2dup has-bigger-sum if
            inc-r
        then
        over shift-previous  ( ... addr-prevs )
        -rot cell+ 2dup <=
    until 2drop drop
    r> ;

numbers ' parse-number parse-lines to nb-lines
solve-01-1 . cr
solve-01-2 . cr
checkEmptyStack bye
