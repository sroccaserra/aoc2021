require common/common.fs

\ "sub" is for submarine.

0 Value nb-lines
1000 Constant max-lines
Create numbers max-lines cells allot

: command-direction ( command-addr -- c )
    c@ ;

: command-value ( command-addr -- n )
    char+ @ ;

: sub-hpos ( sub-addr -- n )
    @ ;

: inc-sub-hpos ( n sub-addr -- )
    tuck sub-hpos + swap ! ;

: sub-depth ( sub-addr -- n )
    cell+ @ ;

: inc-sub-depth ( n sub-addr -- )
    tuck sub-depth + swap cell+ ! ;

: dec-sub-depth ( n sub-addr -- )
    swap negate swap inc-sub-depth ;

: eval-command ( command-addr sub-addr -- )
    swap dup command-value swap command-direction
    case
        'f' of over inc-sub-hpos endof
        'u' of over dec-sub-depth endof
        'd' of over inc-sub-depth endof
    endcase
    drop ;

: eval-result ( sub-addr -- n )
    dup sub-hpos swap sub-depth * ;

: solve-02-1 ( -- result )
    assert( nb-lines max-lines <= )
    here >r 0 , 0 ,
    numbers nb-lines cells bounds begin
        dup @ r@ eval-command
        cell+ 2dup <=
    until 2drop
    r> eval-result ;

: parse-02 ( c-addr u -- command-addr )
    here >r
    over c@ c,
    1- chars + 1 parse-number ,
    r> ;

numbers ' parse-02 parse-lines to nb-lines
solve-02-1 . cr

checkEmptyStack bye
