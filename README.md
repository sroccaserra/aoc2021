# aoc2021

## Learnings

See also:

- <https://github.com/sroccaserra/aoc2015#learnings>
- <https://github.com/sroccaserra/aoc2018#learnings>
- <https://github.com/sroccaserra/aoc2019#learnings>
- <https://github.com/sroccaserra/aoc2020#learnings>

Contents:

- [#algorithms](#algorithms)
- [#linux](#linux)
- [#scheme](#scheme)
- [#lua](#lua)
- [#python](#python)
- [#haskell](#haskell)
- [#uxn](#uxn)
- [#go](#go)
- [#forth](#forth)
- [#c++](#c)
- [#rust](#rust)
- [#gnu-smalltalk](#gnu-smalltalk)
- [#kotlin](#kotlin)
- [#ruby](#ruby)
- [#x64-assembly](#x64-assembly)
- [#how-to-run](#how-to-run)

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

#### References

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

#### References

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

#### References

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
- Puzzle Template in Go ~ <https://github.com/dnnrly/puzzle-template>

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

#### References

- Gforth Manual ~ <https://gforth.org/manual/index.html>
- Create ~ <https://gforth.org/manual/CREATE.html>
- Execution Tokens ~ <https://gforth.org/manual/Execution-Tokens-Tutorial.html>
- Quotations ~ <https://gforth.org/manual/Quotations.html>
- General Files ~ <https://gforth.org/manual/General-files.html>
- The Input Stream ~ <https://gforth.org/manual/The-Input-Stream.html>
- Line Input and Conversion ~ <https://gforth.org/manual/Line-input-and-conversion.html>
- Number Conversion ~ <https://gforth.org/manual/Number-Conversion.html>
- Simple Numeric Output ~ <https://gforth.org/manual/Simple-numeric-output.html>
- Designing the stack effect ~ <https://gforth.org/manual/Designing-the-stack-effect-Tutorial.html>
- Debugging ~ <https://gforth.org/manual/Debugging.html>
- Examining Data and Code ~ <https://gforth.org/manual/Examining-data.html>
- Postpone Tutorial ~ <https://gforth.org/manual/POSTPONE-Tutorial.html>
- Literal Tutorial ~ <https://gforth.org/manual/Literal-Tutorial.html>
- Literals ~ <https://gforth.org/manual/Literals.html>
- Macros ~ <https://gforth.org/manual/Macros.html>
- The Forth Foundation Library (FFL) ~ <https://github.com/RickCarlino/ffl>

### C++

#### References

- C++ Reference ~ <https://en.cppreference.com/w/>
- Fluent C++ Posts ~ <https://www.fluentcpp.com/posts/>

Solutions:

- <https://github.com/RiotNu/advent-of-code>

### Rust

- The iterator returned by `into_iter` may yield any of `T`, `&T` or `&mut T`,
  depending on the context.
- The iterator returned by `iter` will yield `&T`, by convention.
- The iterator returned by `iter_mut` will yield `&mut T`, by convention.

The argument to a `for` loop must implement `IntoIterator`. There are two
different implementations of `IntoIterator` for `Vec` and `&Vec`. You get
values for `Vec` and references for `&Vec` because that's how the iterators are
defined.

```
impl<T> IntoIterator for Vec<T> {
    type Item = T;
    type IntoIter = IntoIter<T>
}

impl<'a, T> IntoIterator for &'a Vec<T> {
    type Item = &'a T;
    type IntoIter = Iter<'a, T>
}
```

When you use `a_vector` inside a `for..in` loop, Rust will call the
`IntoIterator::into_iter` trait method of the `Vec`, which takes ownership of
`self`. Therefore you cannot use `a_vector` afterwards.

```
use std::iter::IntoIterator;

// these are equivalent
for i in a_vector { /* ... */ }
for i in IntoIterator::into_iter(a_vector) { /* ... */ }
```

The index operator, on the other hands, calls the `Index::index` trait method
of the `Vec`, which takes `self` by reference. Additionally, it automatically
dereferences the value, so that if the items inside the vector implement
`Copy`, they will be copied out of the vector instead of borrowed (you need to
explicitly borrow if you want a reference):

```
use std::ops::Index;

// these are equivalent
let x = a_vector[0];
let x = *Index::index(&a_vector, 0);

// these are equivalent
let x = &a_vector[0];
let x = Index::index(&a_vector, 0);
```

#### References

Standard doc links:

- The Rust Programming Language (Book) ~ <https://doc.rust-lang.org/book/title-page.html>
- Rust by Example ~ <https://doc.rust-lang.org/stable/rust-by-example/>
- The Rust Standard Library ~ <https://doc.rust-lang.org/std/index.html>
- The Rust Reference ~ <https://doc.rust-lang.org/reference/index.html>
- `std::ops::Index` ~ <https://doc.rust-lang.org/std/ops/trait.Index.html>
- `std::ops::Index::index` ~ <https://doc.rust-lang.org/std/ops/trait.Index.html#tymethod.index>
- `std::iter::IntoIterrator::into_iter` ~ <https://doc.rust-lang.org/std/iter/trait.IntoIterator.html#tymethod.into_iter>
- `std::result` ~ <https://doc.rust-lang.org/std/result/>
- Function Pointer Types ~ <https://doc.rust-lang.org/reference/types/function-pointer.html>
- Module Source Filenames ~ <https://doc.rust-lang.org/reference/items/modules.html#module-source-filenames>
- Rust by Example - Read lines ~ <https://doc.rust-lang.org/rust-by-example/std_misc/file/read_lines.html>

Other refs & tools:

- Rustlings ~ <https://github.com/rust-lang/rustlings/>
- rust-analyzer ~ <https://github.com/rust-lang/rust-analyzer>
- Nom parser ~ <https://github.com/Geal/nom>
- A Gentle Introduction to Rust ~ <https://stevedonovan.github.io/rust-gentle-intro/readme.html>

Interesting SO questions:

- `iter`, `into_iter`, `iter_mut` ~ <https://stackoverflow.com/questions/34733811/what-is-the-difference-between-iter-and-into-iter>
- Vector or Vector reference to `for` loop ~ <https://stackoverflow.com/questions/43036279/what-does-it-mean-to-pass-in-a-vector-into-a-for-loop-versus-a-reference-to-a>
- Vectors borrowing and ownership ~ <https://stackoverflow.com/questions/61169889/vectors-borrowing-and-ownership>
- Differences between String and str ~ <https://stackoverflow.com/questions/24158114/what-are-the-differences-between-rusts-string-and-str>

### GNU Smalltalk

Apparently, GNU Smalltalk classes don't call `initialize` methods in `new` (?)

The `#inspect` message is useful in GNU Smalltalk too, it prints the receiver's
value to `stdout`.

Two ways to send a dynamic message to an object. Let `aSelector`, a symbol of
the message to be sent, and `anObjet`, the receiver:

```
anObject perform: aSelector with: aValue.
```

or:

```
aMessage := Message selector: aSelector argument: aValue.
aMessage sendTo: anObject.
```

For example, if `anObject` was `aSubmarine`, and the selector was `#forward:`,
`aSubmarine perform: #forward: with: aValue` would be equivalent to `aSubmarine
forward: aValue`.

#### References

- GNU Smalltalk Library Reference ~ <https://www.gnu.org/software/smalltalk/manual-base/gst-base.html>
- Turorial ~ <https://www.gnu.org/software/smalltalk/manual/gst.html#Tutorial>
- Creating Classes ~ <https://www.gnu.org/software/smalltalk/manual/html_node/Creating-classes.html>
- OrderedCollection ~ <https://www.gnu.org/software/smalltalk/manual-base/html_node/OrderedCollection.html#OrderedCollection>
- The Existing Hierarchy ~ <https://www.gnu.org/software/smalltalk/manual/html_node/The-existing-hierarchy.html>
- Sources ~ <https://github.com/gnu-smalltalk/smalltalk>

### Kotlin

#### References

- Data Classes ~ <https://kotlinlang.org/docs/data-classes.html>
- Kotlin command-line Compiler ~ <https://kotlinlang.org/docs/command-line.html>

### Ruby

#### References

- Ruby Syle Guide ~ <https://github.com/airbnb/ruby>

### x64 Assembly

This runs under Linux only.

See also: <https://github.com/sroccaserra/learning-x64-assembly>

Register mode: `%rdi` is the contents of register `%rdi`.

Immediate mode: `$0x1234` is the value `0x1234`. `$localvar` is the value of
`localvar` (the address represented by the symbol `localvar`).

Direct Memory mode: `0x1234` is the value at address `0x1234`. `localvar` is
the value at address `localvar`.

Register Indirect mode: `(%rbx)` is the value at the address contained in
`%rbx`.

When built with `as` or with `gcc -nostdlib`, command line arguments are passed
on the stack. The number of command line arguments is at `(%rsp)`. The address
of the name of the executable is at `8(%rsp)`. The adress of the first command
line argument is at `16(%rsp)`, etc.

When built with the stdlib (gcc default), the C runtime provides the `_start`
entry point, so in our assembly code we would define a `main` function as entry
point instead of `_start`.

When built with the stdlib, the command line arguments are not passed on the
stack. Our `main` function is called with argc in `%rdi`, and a `char**` in
`%rsi` (beware the number of indirections here, it's different than
previously).

To generate position-independant code, we can use `localvar(%rip)` or
`globalvar@GOTPCREL(%rip)` instead of `localvar` or `globalvar`. GOT = Global
Offset Table. Instructions like `movq $mystring, %rsi` can become `leaq
mystring(%rip), %rsi`.

Using gdb:
- Use `gdb --args build/01_s src/01.in` to pass arguments to the debugged executable
- Use `br *_start` to add a break to the start of the programm
- Use `start` to start the programm
- Use `disass` to see the assembly code listing
- Use `ni` to execute the current instruction
- Use `print/x $rax` to print the contents of `%rax` in hex
- Use `print/x *0x7fffffffda9b` to print contents of a memory address
- Use `x $rax` to explore the memory pointed by `%rax`
- Use `x <address>` to explore the contents of the address
- Use `x/4gx <address>` to see the contents of the address as hex, four 8 bytes chunks
- Use `x/s <address>` to see the contents of the address as null terminated string
- Use `x *<address>` to explore the contents pointed to by address

#### References

- `$ man syscalls`

Sites:

- x86 and amd64 instruction reference ~ <https://www.felixcloutier.com/x86/>
- MOV -- Move ~ <https://www.felixcloutier.com/x86/mov>
- LEA -- Load Effective Address ~ <https://www.felixcloutier.com/x86/lea>
- 64-bit system call numbers and entry vectors ~ <https://github.com/torvalds/linux/blob/master/arch/x86/entry/syscalls/syscall_64.tbl>
- Linux System Call Table ~ <https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md>
- fcntl.h ~ <https://github.com/torvalds/linux/blob/master/include/uapi/asm-generic/fcntl.h>
- Linux System Call Table ~ <http://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/>
- Learning Assembly ~ <https://github.com/danbev/learning-assembly/blob/master/README.md>
- Assembly Language, Calling Convention, and the Stack ~ <https://cs.brown.edu/courses/csci1310/2020/notes/l08.html>
- Stack frame layout on x86-64 ~ <https://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64/>
- Assembler Directives ~ <https://ftp.gnu.org/old-gnu/Manuals/gas-2.9.1/html_chapter/as_toc.html>

SO questions:

- Linux 64 command line parameters in Assembly ~ <https://stackoverflow.com/questions/3683144/linux-64-command-line-parameters-in-assembly>
- Why isn't movl from memory to memory allowed? ~ <https://stackoverflow.com/questions/33794169/why-isnt-movl-from-memory-to-memory-allowed>

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
$ make 01_tal
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

To run Node.js solutions:

```
$ node src/01.{js,in}
```

To run C++ solutions:

```
$ make 01_cpp
```

To run Rust solutions:

```
$ make 01_rs
```

To run GNU Smalltalk solutions:

```
$ make 01_st
```

To run Java solutions:

```
$ make 01_java
```

To run Kotlin solutions:

```
$ make 01_kt
```

To run Ruby solutions:

```
$ ruby src/01.{rb,in}
```

To run x64 Assembly solutions

```
$ make 01_s
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
