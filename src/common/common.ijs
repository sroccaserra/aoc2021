NB. The value `input` should be defined before calling this function. E.g. pass
NB. "input =: 'src/01.in'" to the program.

getParsedLines_z_ =. adverb define
readfile =. 1!:1
> u each cutopen .toJ readfile < input
)
