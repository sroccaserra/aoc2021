load 'src/common/common.ijs'

solve1 =. [: +/2</\ ]
solve2 =. [: solve1 3+/\ ]

numbers =. > ". each getinputlines ''
echo solve1 numbers
echo solve2 numbers
