load 'src/common/common.ijs'

solve1 =: {{ +/ 2</\ y }}
solve2 =: {{ solve1 3+/\ y }}

numbers =. > ". each getinputlines ''
echo solve1 numbers
echo solve2 numbers

NB. Tests
{{
  ns =. 199 200 208 210 200 207 240 269 260 263
  assert. 7 5 -: (solve1,solve2) ns
}}''
