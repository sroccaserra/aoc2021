require common/common.fs

0 Value nb-commands
1000 Constant max-commands
Create commands max-commands cells allot

: create-submarine ( -- sub-addr )
    here 0 , 0 , 0 , 0 , ;
: sub.hpos ( sub-addr -- addr ) ;
: sub.depth-1 ( sub-addr -- addr ) cell+ ;
: sub.depth-2 ( sub-addr -- addr ) [ 2 cells ] literal + ;
: sub.aim ( sub-addr -- addr ) [ 3 cells ] literal + ;

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

: create-command ( c-direction n-value -- command-addr )
    here -rot swap c, , ;
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
    assert( nb-commands max-commands <= )
    create-submarine { submarine }
    commands nb-commands cells bounds do
        submarine i @ eval-command
    cell +loop
    submarine dup sub.hpos @ swap sub.depth-2 @ *
    submarine dup sub.hpos @ swap sub.depth-1 @ * ;

: parse-02 ( c-addr u -- command-addr )
    over c@ -rot ( c-direction c-addr u )
    1- chars + 1 parse-number ( c-direction n-value )
    create-command ;

commands ' parse-02 parse-lines to nb-commands
solve-02 . cr . cr
checkEmptyStack bye
