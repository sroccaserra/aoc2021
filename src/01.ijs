load 'src/common/common.ijs'

parse_subfn =: ".
numbers =. getParsedLines ''

solve1 =: +/&(}:<}.)

solve2 =: monad define
+/ 2 </\ 3 +/\ y
)

echo solve1 numbers
echo solve2 numbers
