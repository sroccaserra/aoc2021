require common/common.fs

0 Value nb-lines
1000 Constant max-lines
Create numbers max-lines cells allot

: command-direction ( command-addr -- c )
    c@ ;

: command-value ( command-addr -- n )
    char+ @ ;

: create-submarine ( -- sub-addr )
    here 0 , 0 , 0 , 0 , ;

: sub-hpos ( sub-addr -- n )
    @ ;

: inc-sub-hpos ( sub-addr n -- )
    over sub-hpos + swap ! ;

: sub-depth-1 ( sub-addr -- n )
    cell+ @ ;

: inc-sub-depth-1 ( sub-addr n -- )
    over sub-depth-1 + swap cell+ ! ;

: dec-sub-depth-1 ( sub-addr n  -- )
    negate inc-sub-depth-1 ;

: sub-depth-2 ( sub-addr -- n )
    2 cells + @ ;

: inc-sub-depth-2 ( sub-addr n -- )
    over sub-depth-2 + swap 2 cells + ! ;

: dec-sub-depth-2 ( sub-addr n  -- )
    negate inc-sub-depth-2 ;

: sub-aim ( sub-addr -- n )
    3 cells + @ ;

: inc-sub-aim ( sub-addr n -- )
    over sub-aim + swap 3 cells + ! ;

: dec-sub-aim ( sub-addr n  -- )
    negate inc-sub-aim ;

: eval-command ( command-addr sub-addr -- )
    swap dup command-value swap command-direction
    case ( addr n )
        'f' of 2dup inc-sub-hpos over sub-aim * inc-sub-depth-2 endof
        'u' of 2dup dec-sub-depth-1 dec-sub-aim endof
        'd' of 2dup inc-sub-depth-1 inc-sub-aim endof
    endcase ;

: eval-result-1 ( sub-addr -- n )
    dup sub-hpos swap sub-depth-1 * ;

: eval-result-2 ( sub-addr -- n )
    dup sub-hpos swap sub-depth-2 * ;

: solve-02 ( -- result-2 result-1 )
    assert( nb-lines max-lines <= )
    create-submarine >r
    numbers nb-lines cells bounds begin
        dup @ r@ eval-command
        cell+ 2dup <=
    until 2drop
    r> dup eval-result-2 swap eval-result-1 ;

: parse-02 ( c-addr u -- command-addr )
    here >r
    over c@ c,
    1- chars + 1 parse-number ,
    r> ;

numbers ' parse-02 parse-lines to nb-lines
solve-02 . cr . cr

checkEmptyStack bye