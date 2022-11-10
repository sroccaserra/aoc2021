getParsedLines =: 3 : 0
    readfile =. 1!:1
    > parse_subfn each cutopen .toJ readfile < y
)

parse_subfn =: ".
numbers =. getParsedLines input

load 'plot'
plot numbers
