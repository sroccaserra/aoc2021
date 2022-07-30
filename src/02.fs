require common/common.fs

0 Value nb-lines
1000 Constant max-lines
Create numbers max-lines cells allot

: command-direction ( command-addr -- c )
    c@ ;

: command-value ( command-addr -- n )
    char+ @ ;

: state-hpos ( state-addr -- n )
    @ ;

: inc-state-hpos ( n state-addr -- )
    tuck state-hpos + swap ! ;

: state-depth ( state-addr -- n )
    cell+ @ ;

: inc-state-depth ( n state-addr -- )
    tuck state-depth + swap cell+ ! ;

: dec-state-depth ( n state-addr -- )
    swap negate swap inc-state-depth ;

: eval-command ( command-addr state-addr -- )
    swap dup command-value swap command-direction
    case
        'f' of over inc-state-hpos endof
        'u' of over dec-state-depth endof
        'd' of over inc-state-depth endof
    endcase
    drop ;

: eval-result ( state-addr -- n )
    dup state-hpos swap state-depth * ;

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
