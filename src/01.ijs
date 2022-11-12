load 'src/common/common.ijs'

parse_subfn =: ".
numbers =. getParsedLines ''

solve1 =: +/&(}: < }.)
solve2 =: [: +/ 2 </\ 3 +/\ ]

echo solve1 numbers
echo solve2 numbers
