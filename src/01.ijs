load 'src/common/common.ijs'

solve1 =. +/&(}: < }.)
solve2 =. [: +/ 2 </\ 3 +/\ ]

numbers =. > ". each getinputlines ''
echo solve1 numbers
echo solve2 numbers
