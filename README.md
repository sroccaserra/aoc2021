# aoc2021

## Learnings

See also:

- <https://github.com/sroccaserra/aoc2015#learnings>
- <https://github.com/sroccaserra/aoc2018#learnings>
- <https://github.com/sroccaserra/aoc2019#learnings>
- <https://github.com/sroccaserra/aoc2020#learnings>

### Algorithms

- Breadth-First Search
    - Introduction to Algorithms, Third Edition, 22.2, p. 594
    - Artificial Intelligence: a Modern Approach, Third Edition 3.4.1, p. 81
    - The Algorithm Design Manual, 5.6, p. 162
    - <https://en.wikipedia.org/wiki/Breadth-first_search>

- Depth-First Search
    - Introduction to Algorithms, Third Edition, 22.3, p. 603
    - Artificial Intelligence: a Modern Approach, Third Edition 3.4.3, p. 85
    - The Algorithm Design Manual, 5.8, p. 169
    - <https://en.wikipedia.org/wiki/Depth-first_search>

- Topological Sort
    - Introduction to Algorithms, Third Edition, 22.4, p. 612
        - Of a DAG, using DFS
    - <https://en.wikipedia.org/wiki/Topological_sorting>

- Uniform Cost Search
    - Artificial Intelligence: a Modern Approach, Third Edition 3.4.2, p. 83
    - <https://ojs.aaai.org/index.php/SOCS/article/view/18191>
    - <https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Practical_optimizations_and_infinite_graphs>

- Dijkstra's Algorithm
    - Introduction to Algorithms, Third Edition, 24.3, p. 658
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

- Dynamic programming: to solve a DP problem with two players, we can swap
  arguments in the recursive call, see day 21 part two (Lua).

### Linux

- On Linux, `/usr/bin/time -v ...` gives the memory usage (see `Maximum resident set size`).

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
$ lua src/01.lua <src/01.txt
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
