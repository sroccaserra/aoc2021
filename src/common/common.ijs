NB. The value `input` should be defined before calling this function. E.g. pass
NB. "input =: 'src/01.in'" to the program.

getinputlines_z_ =: monad define
readfile =. 1!:1
cutopen .toJ readfile < input
)
