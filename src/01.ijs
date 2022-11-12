NB. The value `input` should be defined before calling this function. E.g. pass
NB. "input =: 'src/01.in'" to the program.

NB. The value `parse_subfn` should be defined before calling this function.

getParsedLines =: monad define
readfile =. 1!:1
> parse_subfn each cutopen .toJ readfile < input
)

parse_subfn =: ".
numbers =. getParsedLines ''

solve1 =: +/&(}:<}.)

echo solve1 numbers
