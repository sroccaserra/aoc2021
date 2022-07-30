require common/common.fs

0 Value nb-lines
1000 Constant max-lines
Create numbers max-lines cells allot

: create-submarine ( -- sub-addr ) here 0 , 0 , 0 , 0 , ;
: sub.hpos ( sub-addr -- addr ) ;
: sub.depth-1 ( sub-addr -- addr ) cell+ ;
: sub.depth-2 ( sub-addr -- addr ) 2 cells + ;
: sub.aim ( sub-addr -- addr ) 3 cells + ;

: inc-sub-hpos ( sub-addr n -- )
    over sub.hpos @ + swap sub.hpos ! ;
: inc-sub-depth-1 ( sub-addr n -- )
    over sub.depth-1 @ + swap sub.depth-1 ! ;
: dec-sub-depth-1 ( sub-addr n  -- )
    negate inc-sub-depth-1 ;
: inc-sub-depth-2 ( sub-addr n -- )
    over sub.depth-2 @ + swap sub.depth-2 ! ;
: dec-sub-depth-2 ( sub-addr n  -- )
    negate inc-sub-depth-2 ;
: inc-sub-aim ( sub-addr n -- )
    over sub.aim @ + swap sub.aim ! ;
: dec-sub-aim ( sub-addr n  -- )
    negate inc-sub-aim ;

: command.direction@ ( command-addr -- c ) c@ ;
: command.value@ ( command-addr -- n ) char+ @ ;

: eval-command ( sub-addr command-addr -- )
    dup command.value@ swap command.direction@
    case ( addr n )
        'f' of 2dup inc-sub-hpos over sub.aim @ * inc-sub-depth-2 endof
        'u' of 2dup dec-sub-depth-1 dec-sub-aim endof
        'd' of 2dup inc-sub-depth-1 inc-sub-aim endof
    endcase ;

: solve-02 ( -- result-2 result-1 )
    assert( nb-lines max-lines <= )
    create-submarine { submarine }
    numbers nb-lines cells bounds do
        submarine i @ eval-command
    cell +loop
    submarine dup sub.hpos @ swap sub.depth-2 @ *
    submarine dup sub.hpos @ swap sub.depth-1 @ * ;

: parse-02 ( c-addr u -- command-addr )
    here >r
    over c@ c,
    1- chars + 1 parse-number ,
    r> ;

numbers ' parse-02 parse-lines to nb-lines
solve-02 . cr . cr

checkEmptyStack bye
