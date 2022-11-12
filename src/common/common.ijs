NB. The value `input` should be defined before calling this function. E.g. pass
NB. "input =: 'src/01.in'" to the program.

getParsedLines_z_ =. monad define
readfile =. 1!:1
> y `:6 each cutopen .toJ readfile < input
)
