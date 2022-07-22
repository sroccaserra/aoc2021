# aoc2021

## Learnings

See also:

- <https://github.com/sroccaserra/aoc2015#learnings>
- <https://github.com/sroccaserra/aoc2018#learnings>
- <https://github.com/sroccaserra/aoc2019#learnings>
- <https://github.com/sroccaserra/aoc2020#learnings>

### Algorithms

- General problem solving: How to Solve It (book) ~ <https://en.wikipedia.org/wiki/How_to_Solve_It>

- Heaps & Priority Queues
    - Introduction to Algorithms, Third Edition, 6.1, p. 151
    - Algorithm Design, 2.5, p. 57
    - Algorithms, 4.5, p. 125-126
    - The Algorithm Design Manual, 4.3.1, p. 109
    - https://stanford-cs221.github.io/autumn2019/live/search1/
    - https://www.youtube.com/watch?v=aIsgJJYrlXk

- Dynamic programming: to solve a DP problem with two players, we can swap
  arguments in the recursive call, see day 21 part two (Lua).

#### Search

- Breadth-First Search
    - Introduction to Algorithms, Third Edition, 22.2, p. 594
    - Algorithm Design, 3.3, p. 90
    - Algorithms, 4.2, p. 116
    - Artificial Intelligence: a Modern Approach, Third Edition 3.4.1, p. 81
    - The Algorithm Design Manual, 5.6, p. 162
    - <https://en.wikipedia.org/wiki/Breadth-first_search>

- Depth-First Search
    - Introduction to Algorithms, Third Edition, 22.3, p. 603
    - Algorithm Design, 3.3, p. 92
    - Algorithms, 3.2, p. 93
    - Artificial Intelligence: a Modern Approach, Third Edition 3.4.3, p. 85
    - The Algorithm Design Manual, 5.8, p. 169
    - <https://en.wikipedia.org/wiki/Depth-first_search>

- Topological Sort
    - Introduction to Algorithms, Third Edition, 22.4, p. 612
        - Of a DAG, using DFS
    - Algorithm Design, 3.6, p. 99
    - <https://en.wikipedia.org/wiki/Topological_sorting>

- Uniform Cost Search
    - Artificial Intelligence: a Modern Approach, Third Edition 3.4.2, p. 83
    - <https://ojs.aaai.org/index.php/SOCS/article/view/18191>
    - <https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Practical_optimizations_and_infinite_graphs>

- Dijkstra's Algorithm
    - Introduction to Algorithms, Third Edition, 24.3, p. 658
    - Algorithm Design, 4.4, p. 137
    - Algorithms, 4.4, p. 119
    - The Algorithm Design Manual, 6.3.1, p. 206
    - <https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm>

- Greedy Best-First Search
    - Artificial Intelligence: a Modern Approach, Third Edition 3.5.1, p. 92
    - <https://en.wikipedia.org/wiki/Best-first_search>

- A-star Search
    - Artificial Intelligence: a Modern Approach, Third Edition 3.5.2, p. 93
    - <https://en.wikipedia.org/wiki/A*_search_algorithm>

- Summary
    - Artificial Intelligence: a Modern Approach, Third Edition 3.7, p. 108

- Backtracking
    - Algorithm Design Manual, 7.1, p. 231.
    - Example of usage in Python: <https://leetcode.com/problems/reconstruct-itinerary/discuss/491164/python-backtracking-following-skienas-template>
    - <https://en.wikipedia.org/wiki/Backtracking>

### Linux

- On Linux, `/usr/bin/time -v ...` gives the memory usage (see `Maximum
  resident set size`).

### Scheme

- Scheme is even smaller that Lua it seems, there is no regex utilities in the
  standard library for instance.
- Named `let` is useful for looping:
    - <http://www.r6rs.org/final/html/r6rs/r6rs-Z-H-14.html#node_sec_11.16>
- The `do` special form looks powerful:
    - <http://www.r6rs.org/final/html/r6rs-lib/r6rs-lib-Z-H-6.html>

References:

- <http://www.r6rs.org/>
- <http://www.r6rs.org/final/html/r6rs/r6rs-Z-H-2.html>
- <http://www.r6rs.org/final/html/r6rs-lib/r6rs-lib-Z-H-1.html>
- <https://cisco.github.io/ChezScheme>
- <https://www.scheme.com/tspl4/>
- <https://cisco.github.io/ChezScheme/csug9.5/csug.html>
- <https://schemers.org/Documents/>
- <https://srfi.schemers.org/?statuses=final>
- <https://akkuscm.org/packages/chez-srfi/>
- <https://wiki.c2.com/?SchemeUnit>

### Lua

Lua is a simple and very small language, which is a nice feature because it is
one of the rare languages where you can read the entire doc in a reasonable
time.

The downside is that the standard library is limited, there is no tuples, no
sets, no class. We have to use what is provided in a creative way to emulate
those.

So in a way, it can be fun to try and be creative to "use what we have" and "do
what we can".

What we have is a very versatile "table" data structure, that can either be
used as a 1-based array or as a hash table, and functions. And while Lua also
provides "metatables", that can be used to emulate prototype-based inheritance,
I found it not really useful for Advent of Code puzzles, maybe I didn't look
hard enough.

Another problem is that not unlike JavaScript, Lua does not check function
arity, nil value bugs can sneak in very easily deep into a program. So we have
to be extra careful.

- Lua has no set of tuples and no set, but it can be faked with tables, for
  exemple:

```lua
t = {}
function add(t,x,y) if not t[y] then t[y] = {} end t[y][x] = true end
function has(t,x,y) if not t[y] then t[y] = {} end return t[y][x] end
```

- Lua cannot use tables or tuples as keys, but you can usually easily generate
  a key with `string.format()`, for example:

```lua
local key = string.format("%d %d %d %d", p1_pos, p1_score, p2_pos, p2_score)
```

- Use `t[y][x] = {}` to store data based on coordinates, like adjacency lists.

- Use `table.insert(t, x)` and `table.remove(t)` to implement an array-based
  stack with tables.

- Use `table.insert(t, 1, x)` and `table.remove(t, 1)` for small queues (up to
  some hundred elements).

### Python

- Python can now pattern match:
    - Structural Pattern Matching: Tutorial ~ <https://www.python.org/dev/peps/pep-0636/>
- Counters can be useful:
    - Counter objects ~ <https://docs.python.org/3/library/collections.html#counter-objects>
- If I mute a matrix m (list of lists) copied with `m.copy()`, there is a good chance that I mute the original matrix also. `[r.copy() for r in m]` should work better. See also `copy.deepcopy()`.

### Haskell

- `Data.Set` can be used as a priority queue (`insert` and `deleteFindMin` are
  O(log n)) (see day 15).
- `flip (,) <$> [y-1..y+1] <*> [x-1..x+1]` generates `[(x-1, y-1), (x, y-1), (x+1, y-1) ...]`.
- We can pattern guard on monads with the `<-` operator : `validate xs (y:ys) | Just x <- lookup y brackets = validate (x:xs) ys`.
- Beware, if you want to update a count with -n `Map.insertWith (-)` will
  probably reverse the arguments. Use `flip (-)` or `(+) k (-n)`.

### Uxn

- Take great care with relative addresses. `#00 ,&a STR` works but `,&a #00 SWP STR` doesn't, because in the second case the relative address is measured from the wrong point.
- Use `STH` and `STHr` to move values to and from the return stack
- Use `LITr` to push values like `#00` to the return stack

References:

- <https://100r.co/site/uxn.html>
- <https://wiki.xxiivv.com/site/uxntal.html>
- <https://wiki.xxiivv.com/site/varvara.html>
- <https://wiki.xxiivv.com/site/uxntal_reference.html>
- <https://wiki.xxiivv.com/site/chr_format.html>

Resources:

- <https://compudanzas.net/uxn_tutorial.html>
- <https://learnxinyminutes.com/docs/uxntal/>
- <https://metasyn.github.io/learn-uxn/>
- <https://github.com/hundredrabbits/awesome-uxn>
- <https://mobile.twitter.com/hundredrabbits/status/1466454006906032131>
- <https://llllllll.co/t/uxn-virtual-computer/46103>
- Mini-gmp port for uxn virtual computer ~ <https://code.mathr.co.uk/ugmp>

Solutions:

- <https://github.com/jonathanperret/aoc2021>
- <https://git.sr.ht/~alderwick/>

8 bit references:

- <http://6502.org/source/integers/hex2dec.htm>
- <https://codebase64.org/doku.php?id=base:another_hexadecimal_to_decimal_conversion>
- <http://6502.org/source/integers/32muldiv.htm?utm_source=pocket_mylist>
- <https://codebase64.org/doku.php?id=base:6502_6510_maths>
- <https://devblogs.microsoft.com/oldnewthing/20141208-00/?p=43453>

### Go

References:

- Documentation ~ <https://go.dev/doc/>
- A Tour of Go ~ <https://go.dev/tour/list>
- Using Go Modules ~ <https://go.dev/blog/using-go-modules>
- How to Write Go Code ~ <https://go.dev/doc/code>
- The Go Programming Language Specification ~ <https://go.dev/ref/spec>
- Go Modules Reference ~ <https://go.dev/ref/mod>
- Standard Library ~ <https://pkg.go.dev/std>
- Frequently Asked Questions (FAQ) ~ <https://go.dev/doc/faq>
- Error Handling and Go ~ <https://go.dev/blog/error-handling-and-go>

Solutions:

- <https://github.com/alexchao26/advent-of-code-go>
- <https://github.com/paulden/aoc-2021>

Tools:

- gopls ~ <https://pkg.go.dev/golang.org/x/tools/gopls>

### Forth

Example of defining an unnamed word and executing it:

```forth
:noname
  3 ;

.s
<1> 140266528584968  ok
execute
ok
.s
<1> 3  ok

```

References:

- Gforth Manual ~ <https://gforth.org/manual/index.html>
- Create ~ <https://gforth.org/manual/CREATE.html>
- Execution Tokens ~ <https://gforth.org/manual/Execution-Tokens-Tutorial.html>
- Quotations ~ <https://gforth.org/manual/Quotations.html>
- General Files ~ <https://gforth.org/manual/General-files.html>
- Line Input and Converstion ~ <https://gforth.org/manual/Line-input-and-conversion.html>


## How to run

To run Python solutions:

```
$ python3 src/01.{py,in}
```

To run Haskell solutions (two ways):

```
$ stack runhaskell src/01.hs
$ stack runhaskell src/01.{hs,in}
```

To run Lua solutions:

```
$ lua src/01.{lua,in}
```

To run Lua tests (requires busted, `luarocks install --local busted`):
```
$ busted -o TAP src
```

To run Scheme solutions:

```
$ scheme --libdirs src --script src/01.{ss,in}
```

To run uxn solutions:

```
$ make 01
```

To run Elixir solutions:

```
$ elixir src/01.exs <src/01.in
```

To run Go solutions:

```
$ go run src/01.{go,in}
```

To run Forth solutions:

```
$ gforth src/01.{fs,in}
```

## How it started

```shell
$ stack new aoc2021
$ cd aoc2021
$ rm -r app
$ rm -r test
$ rm -r Changelog.md
```

In package.yaml:
- Remove "executables" section
- Remove "tests" section
- add hspec dependency (LTS) and -W ghc-option in "library" section

```shell
$ stack setup
$ stack build
```

Then write a Spec.hs file in src, and try to run it with:
```shell
$ stack runhaskell -- src/Spec.hs
```

Note: for this simple project, I want all the code in the src directory.
