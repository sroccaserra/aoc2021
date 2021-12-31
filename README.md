# aoc2021

## Learnings

See also:

- <https://github.com/sroccaserra/aoc2015#learnings>
- <https://github.com/sroccaserra/aoc2018#learnings>
- <https://github.com/sroccaserra/aoc2019#learnings>
- <https://github.com/sroccaserra/aoc2020#learnings>

### Algorithms

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

- `flip (,) <$> [y-1..y+1] <*> [x-1..x+1]` generates `[(x-1, y-1), (x, y-1), (x+1, y-1) ...]`
- We can pattern guard on monads with the `<-` operator : `validate xs (y:ys) | Just x <- lookup y brackets = validate (x:xs) ys`
- Beware, if you want to update a count with -n `Map.insertWith (-)` will probably reverse the arguments. Use `flip (-)` or `(+) k (-n)`.


## How to run

To run Python solutions:

```
$ python3 src/01.{py,txt}
```

To run Haskell solutions (two ways):

```
$ stack runhaskell src/01.hs
$ stack runhaskell src/01.{hs,txt}
```

To run Lua solutions:

```
$ lua src/01.{lua,txt}
```

To run Lua tests (requires busted, `luarocks install --local busted`):
```
$ busted -o TAP src
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
