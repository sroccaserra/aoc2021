# aoc2021

In this repository, I solved all 25 days for Advent of Code 2021, using mostly
Python and Haskell. This was both fun and really hard for me at the end. I had
to take a small break on day 24. I got back on time for day 25 and I'm really
proud of that. But there is more: then, for what it's worth, I solved the first
two days in 22 different languages. And took some notes along the way.

See also:

- <https://github.com/sroccaserra/aoc2015#learnings>
- <https://github.com/sroccaserra/aoc2018#learnings>
- <https://github.com/sroccaserra/aoc2019#learnings>
- <https://github.com/sroccaserra/aoc2020#learnings>
- <https://github.com/sroccaserra/aoc2022#learnings>

Contents:

- [#two-problems-22-languages](#two-problems-22-languages)
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
- [#x86-64-assembly](#x86-64-assembly)
- [#common-lisp](#common-lisp)
- [#erlang](#erlang)
- [#j](#j)
- [#apl](#apl)
- [#uiua](#uiua)
- [#how-to-run](#how-to-run)

## Two problems, 22 languages

For what it's worth, I solved the first two days in 22 different languages:

- APL
- BQN
- C++
- Common Lisp
- Elixir
- Erlang
- GNU Forth
- GNU Smalltalk
- Go
- Haskell
- J
- Java
- Kotlin
- Lua
- Node.js (JavaScript)
- Python 3
- Ruby
- Rust
- Scheme (Lisp)
- Uiua
- Uxntal
- x86-64 Assembly (with some low level Linux IO syscalls)

Some languages I know very well, some I had to learn from scratch. So please
tell me if I did it totally wrong in your favorite language. I enjoyed them all
though, and the first two days propose very simple problems so it should be at
least barely correct.

You can find theses solutions in the `src` directory, in `01.*` and `02.*`
files. The `*.in` files are my input files for the problems. Please note that
this is not a good naming convention for anything other than Advent of Code.

What is interesting about these first two days is that they invite you to
learn how to:

- Read some inputs
- Process input lines with simple parsing and a simple computation
- Create and pass around a small ad hoc data structure (for day two)
- Print some output
- Move the common code for generic stuff in a common file
- Require the common file

All this forms a good starting point to learn any programming language I guess?
If you know how to do that, you have everything you need to start writing
useful stuff that interacts with input data, maybe comming from other programs,
and pass your output to yet other programs. You also have everything you need
to start automating some tests for example.

Part of the intention here is this. If you are curious about programming
language X or Y, find any possible reason to write some code in it, some code
where you can check the correctness. Simple Advent of Code problems are one
way, there are others. A repl, or practicing TDD are other examples.

Below I tried to document some of my learnings. These are mostly notes for
myself, and not all languages are documented. But I hope you can find something
to enjoy here too. Cheers!

## Learnings

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
- Build ~ <https://pkg.go.dev/go/build>
- A Quick Guide to Go's Assembler ~ <https://go.dev/doc/asm>

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

### x86-64 Assembly

This runs under Linux only. Please note that this is mostly ⌨️ 🐈️ code, I'm
learning basics along the way.

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

Use `objdump -SD build/01.o` to explore generated code.

Using gdb:
- Use `tui reg general` to show registers window
- Use `layout asm` to show disassembly window
- Use `gdb --args build/01_s src/01.in` to pass arguments to the debugged executable
- Use `br *_start` to add a break to the start of the programm
- Use `start` to start the programm
- Use `disass` to see the assembly code listing
- Use `ni` to execute the current instruction
- Use `print/x $rax` or `p/x $rax` to print the contents of `%rax` in hex
- Use `print/x *0x7fffffffda9b` to print contents of a memory address
- Use `x $rax` to explore the memory pointed by `%rax`
- Use `x <address>` to explore the contents of the address
- Use `x/4gx <address>` to see the contents of the address as hex, four 8 bytes chunks
- Use `x/s <address>` to see the contents of the address as null terminated string
- Use `x *<address>` to explore the contents pointed to by address

```
(gdb) p/x $rsp
$2 = 0x7fffffffd570
(gdb) x/xg $rsp
0x7fffffffd570: 0x00007fffffffd594
(gdb) x/xg *(int**)$rsp
0x7fffffffd594: 0x0040200039333131
```

#### References

- [man 2 intro](https://man7.org/linux/man-pages/man2/intro.2.html)
- [man 2 syscalls](https://man7.org/linux/man-pages/man2/syscalls.2.html)
- [man 2 syscall](https://man7.org/linux/man-pages/man2/syscall.2.html)

Sites:

- x86-64 ~ <https://en.wikipedia.org/wiki/X86-64>
- x86 and amd64 instruction reference ~ <https://www.felixcloutier.com/x86/>
- MOV -- Move ~ <https://www.felixcloutier.com/x86/mov>
- LEA -- Load Effective Address ~ <https://www.felixcloutier.com/x86/lea>
- 64-bit system call numbers and entry vectors ~ <https://github.com/torvalds/linux/blob/master/arch/x86/entry/syscalls/syscall_64.tbl>
- unistd.h ~ <https://github.com/torvalds/linux/blob/master/include/uapi/asm-generic/unistd.h>
- Linux System Call Table ~ <https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md>
- fcntl.h ~ <https://github.com/torvalds/linux/blob/master/include/uapi/asm-generic/fcntl.h>
- Linux System Call Table ~ <http://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/>
- Learning Assembly ~ <https://github.com/danbev/learning-assembly/blob/master/README.md>
- Assembly Language, Calling Convention, and the Stack ~ <https://cs.brown.edu/courses/csci1310/2020/notes/l08.html>
- Stack frame layout on x86-64 ~ <https://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64/>

Tools:

- Using as ~ <https://sourceware.org/binutils/docs/as/>
- Assembler Directives ~ <https://sourceware.org/binutils/docs/as/Pseudo-Ops.html>
- Debugging with GDB ~ <https://sourceware.org/gdb/current/onlinedocs/gdb/index.html>
- objdump ~ <https://man7.org/linux/man-pages/man1/objdump.1.html>

SO questions:

- x86 Tag Info ~ <https://stackoverflow.com/tags/x86/info>
- Linux 64 command line parameters in Assembly ~ <https://stackoverflow.com/questions/3683144/linux-64-command-line-parameters-in-assembly>
- Why isn't movl from memory to memory allowed? ~ <https://stackoverflow.com/questions/33794169/why-isnt-movl-from-memory-to-memory-allowed>

### Common Lisp

- The reader upcases symbols, so `'forward` becomes `FORWARD`. The `#'intern`
  function does not upcase its value, so `(intern "forward")` becomes
  `|forward|`.
- Inside a symbol, `|`-enclosed parts preserve their case. `'what|? wow |this|
  also works|?` is ` |WHAT? wow THIS also works?|`
- Symbols prefixed by `:` are symbols from the `KEYWORD` package. `(intern
  "forward" "KEYWORD")` is `:|forward|`

References:

- HyperSpec ~ <http://www.lispworks.com/documentation/HyperSpec/Front/index.htm>
- SBLC ~ <https://www.sbcl.org/>
- SBCL User Manual ~ <https://www.sbcl.org/manual/index.html>
- Common-Lisp.net ~ <https://common-lisp.net/>
- CLiki - The Common Lisp Wiki ~ <https://cliki.net/>
- The Common Lisp Cookbook ~ <https://lispcookbook.github.io/cl-cookbook/>
- Data Structures ~ <https://lispcookbook.github.io/cl-cookbook/data-structures.html>
- Destructuring ~ <https://www.cs.cmu.edu/Groups/AI/html/cltl/clm/node252.html>
- Learn X in Y minutes - Where X=Common Lisp ~ <https://learnxinyminutes.com/docs/common-lisp/>

Tools & Libs:

- Libraries ~ <https://common-lisp.net/libraries>
- ASDF - Another System Definition Facility ~ <https://asdf.common-lisp.dev/>
- UIOP ~ <https://asdf.common-lisp.dev/uiop.html>
- UIOP ~ <https://gitlab.common-lisp.net/asdf/asdf/blob/master/uiop/README.md>
- Awesome Common Lisp ~ <https://github.com/CodyReichert/awesome-cl>
- Lisp Games Wiki ~ <https://github.com/lispgames/lispgames.github.io/wiki>

Books:

- Common Lisp the Language ~ <https://www.cs.cmu.edu/Groups/AI/html/cltl/clm/clm.html>
- Practical Common Lisp ~ <https://gigamonkeys.com/book/>
- Land of Lisp ~ <http://landoflisp.com/>

### Erlang

- To pass a function defined in an escript to another function in the same
  script, I had to add `-mode(compile).`

References:

- Erlang Docs ~ <https://www.erlang.org/doc/index.html>
- Efficiency Guide ~ <https://www.erlang.org/doc/efficiency_guide/users_guide.html>
- Programming Examples - Funs ~ <https://www.erlang.org/doc/programming_examples/funs.html>
- IO ~ <https://www.erlang.org/doc/man/io.html>
- Learn X in Y minutes - Where X=erlang ~ <https://learnxinyminutes.com/docs/erlang/>

### J

Notes for self, how I installed J on Linux:

- Download version J9.4 from <https://code.jsoftware.com/wiki/System/Installation/J9.4/Zips>
- Store it in ~/Applications/j9.4
- Execute recommanded steps for Linux
- Link ~/Applications/j9.4/bin/jconsole to ~/bin/jconsole

How I installed the 'plot' addon:

```ijs
$ sudo jconsole  # sudo is required if j is installed to /usr
   getscripts_j_ 'plot'  NB. Gives the category/module corresponding to 'plot'
   load 'pacman'  NB. Probably not required
   install 'graphics/plot'
   ...
```

If a verb has a noun on its left, it is executed as a dyadic verb with a left
and right operand.  If the verb does not have a noun on its left, it is
executed as monadic with just a right operand.  You must know the part of
speech of the names in a sentence to understand the execution order.  In the
sentence `result =. name1 verb2 5` you must know whether name1 is a verb, in
which case verb2 is executed monadically and the result is `name1(verb2(5))`,
or name1 is a noun, in which case verb2 is dyadic and the result is `(name1
verb2 5)`.

J uses the names x, y, u, v, m, and n to represent arguments to verbs and other
entities.  You should avoid using these names for other purposes.

Convention: pass `''` to a monad that doesn't need any argument.

You can ask the interpreter how it splits a line into words by using monad `;:`
: `;: '2 + 1 2 3'`

For any verb, including user-written verbs, you can ask the interpreter the
rank by typing verbname b. 0 : `#: b. 0`

Plotting values:

```ijs
load 'plot'
plot numbers
```

`x f&g y` ↔ `(g x) f (g y)`. For example, `x %&! y` is the quotient of the
'factorials' of `x` and `y`.

Verb trains as tacit functions: read them from the right, three at a time.
Three verbs form a fork and become a single verb. Then repeat: read from the
right, three at a time (Sierpinsky triangle?)

`2:` is a verb that always returns 2. `2: 4` returns 2. Usefull to introduce
constants in verb trains: `(#-2:)` is a fork that returns the length of a list
minus 2. Read it as `(# - 2:)`.

`":` as a monad (Format) can turn a number into a string. `datatype 2` returns
`integer`, `datatype ": 2` returns `integral`.

The fork where the first function is the identity, `] f g` would be the S
combinator. In J notation and rules, `(] f g) y` is `y f (g y)`. The S
combinator (with more math-like notation) is defined as: `S x y z -> x z (y
z)`. There would also be a similarity with the `<*>` operator in Haskell, as S
is `(<*>)` for the `((->) r)` Applicative instance (I don't really know, to be
explored and confirmed).

The fork is the S' combinator, or the starling', or the phoenix bird from
Haskell's Data.Aviary.Birds package. It is also the liftM2 function from the
Control.Monad package!

References:

- J (programming language) ~ <https://en.wikipedia.org/wiki/J_(programming_language)>
- The J programming language ~ <https://www.jsoftware.com/>
- Learning J ~ <https://www.jsoftware.com/help/learning/contents.htm>
- Preliminaries ~ <https://code.jsoftware.com/wiki/Help/JforC/Preliminaries>
- Loopless Code ~ <https://code.jsoftware.com/wiki/Help/JforC/Loopless_Code_I:_Verbs_Have_Rank>
- Primer contents ~ <https://www.jsoftware.com/help/primer/contents.htm>
- Files ~ <https://www.jsoftware.com/help/primer/files.htm>
- NuVoc 🤯 ~ <https://code.jsoftware.com/wiki/NuVoc>
- Hook ~ <https://code.jsoftware.com/wiki/Vocabulary/hook>
- Folds ~ <https://code.jsoftware.com/wiki/Vocabulary/fcap>
- When programs are data ~ <https://code.jsoftware.com/wiki/Help/JforC/When_Programs_Are_Data>
- `:` ~ <https://code.jsoftware.com/wiki/Vocabulary/com>
- Gerunds ~ <https://www.jsoftware.com/help/learning/14.htm>
- Compositions (Based on Conjunctions) ~ <https://www.jsoftware.com/help/dictionary/samp13.htm>
- Compositions (Based on Hooks and Forks) ~ <https://www.jsoftware.com/help/dictionary/samp14.htm>
- Trains ~ <https://www.jsoftware.com/help/dictionary/dictf.htm>
- Reading Tacit Verbs ~ <https://code.jsoftware.com/wiki/Guides/Reading_Tacit_Verbs>
- Cap ~ <https://www.jsoftware.com/help/dictionary/d502.htm>
- Cap ~ <https://code.jsoftware.com/wiki/Vocabulary/squarelfco>
- Searching and Matching Items: Fast List Operations (FLOs) ~ <https://code.jsoftware.com/wiki/Vocabulary/SpecialCombinations#FLOs>
- RefCard ~ <https://code.jsoftware.com/wiki/File:J602_RefCard_color_letter_current.pdf>

Tools:

- Addons Installation ~ <https://code.jsoftware.com/wiki/Addons/Installation>
- To install 'plot' ~ <https://stackoverflow.com/questions/23746407/j-languages-load-command>

Articles:

- Beyond Functional Programming: Manipulate Functions with the J Language ~ <https://www.adamtornhill.com/articles/jlang/beyondfunctional.html>
- Currying ~ <https://rosettacode.org/wiki/Currying#J>
- "The J Programming Language" by Tracy Harms (2013) ~ <https://www.youtube.com/watch?v=RWYkx6-L04Q>
- The S and K Combinators ~ <https://wiki.c2.com/?EssAndKayCombinators>
- 1 Problem, 16 Programming Languages ~ <https://www.youtube.com/watch?v=UVUjnzpQKUo>

Solutions:

- <https://github.com/jitwit/aoc/tree/a/J/21>
- <https://github.com/adamtornhill/apl-challenge-2014-in-J>

### APL

When running a program from `dyalogscript` (Dyalog APL), to access the `]box
on` and `]rows on` options you can (have to?) call this line (first line in
example below):

```apl
(⎕NS⍬).(_←enableSALT⊣⎕CY'salt')
]box on -style=max
]rows on
```

Nested APLs such as APL2 allow any array to be used as an element, including
scalar numbers or characters (written with quotes) as well as larger arrays. In
order to include a stranded array inside another array it must be
parenthesized. [...] Flat APLs impose the rule that all elements of arrays have
the same type, such as all character or all numeric. [...], and it has been
maintained in newer languages such as SHARP APL and J.

Although Reduce is `foldr1` in nature, one can use it like `foldr`, where a
designated starting value is modified by the rest of the values in sequence. In
this case, the start value (enclosed if not a simple scalar) is attached to the
right end of the vector of "modifiers", and then the entire vector is reduced.

```apl
     (⍉∘⌽↓)/2 1 2 1,⊂5 6⍴⍳30  ⍝ Trim a matrix from all four sides, by rotating the matrix after each trim
┌─────┐
│ 9 10│
│15 16│
│21 22│
└─────┘
```

In general, Reduce reduces one chosen axis (either implied by using the
last-axis form `f/` or first-axis `f⌿`, or explicitly by using function axis
`f/[x])` by evaluating each vector along the chosen axis into a scalar.

Rank: an array may have 0 or more axes or dimensions. The number of axes of an
array is known as its rank.  Dyalog APL supports arrays with a maximum of 15
axes.

Depth: if one or more items of an array is not a simple scalar (i.e. is another
array, or a `⎕OR`), the array is called a nested array. A nested array may
contain items which are themselves nested arrays.  The degree of nesting of an
array is called its depth.

A train such as `= / +` could be interpreted either as the two-train `(=/) +`,
Equals reduction atop Plus, or as a three train Equals Compress Plus.  Dialects
choose the first interpretation. To force the fork interpretation, we can add
right atop: `=⊢⍤/+`. See the reference about function-operator overloading.

References:

- Learn APL ~ <https://xpqz.github.io/learnapl/intro.html>
- Trainspotting ~ <https://xpqz.github.io/learnapl/tacit.html>
- APL Wiki ~ <https://aplwiki.com/wiki/Main_Page>
- Function Composition ~ <https://aplwiki.com/wiki/Function_composition>
- Reduce ~ <https://aplwiki.com/wiki/Reduce>
- Array Model ~ <https://www.aplwiki.com/wiki/Array_model>
- Arrays ~ <https://help.dyalog.com/latest/index.htm#Language/Introduction/Variables/Arrays.htm>
- Simple Examples ~ <https://aplwiki.com/wiki/Simple_examples>
- Function-Operator Overloading ~ <https://aplwiki.com/wiki/Function-operator_overloading#Mitigation>
- APLcart ~ <https://aplcart.info/>
- Mastering Dyalog APL ~ <https://mastering.dyalog.com/README.html>
- A Tour (de Force) of APL in 16 Expressions ~ <https://www.youtube.com/watch?v=e0rywC7-i0U>
- A Tour (de Force) of APL in 16 Expressions ~ <https://www.jsoftware.com/papers/tour_Bangalore/>
- APL a Day ~ <https://www.sacrideo.us/tag/apl-a-day/>
- Parsing content from files with `⎕CSV` ~ <https://www.youtube.com/watch?v=AHoiROI15BA>

Solutions:

- <https://aplwiki.com/wiki/Advent_of_Code>
- <https://github.com/codereport/Advent-of-Code-2022>
- <https://www.youtube.com/watch?v=p0bg5M_R2aQ>

### Uiua

- Use `/∘` to put all array elements on the stack

References:

- <https://www.uiua.org>

### C#

Solutions:

- <https://github.com/encse/adventofcode/tree/master/2021>

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

To run x86-64 Assembly solutions (Linux only):

```
$ make 01_s
```

To debug x86-64 Assembly solutions with gdb, you can add a `halt:` label in
your code, and:

```
$ make 01_sd
```

To run Common Lisp solutions:

```
$ sbcl --script src/01.{lisp,in}
```

or:

```
$ clisp src/01.lisp -- src/01.in
```

To run Erlang solutions:

```
$ escript src/01.{erl,in}
```

To run J solutions:

```
jconsole -js "input=:'src/01.in'" "load 'src/01.ijs'" "exit''"
```

To run the APL solutions:
```
$ dyalogscript src/01.apl
```

To run BQN solutions:
```
$ bqn src/01.{bqn,in}
```

To run Uiua solutions (tested with Uiua 0.4.1):
```
$ uiua run src/01.ua
```

To run C# solutions (`dotnet tool install -g dotnet-script`):
```
$ dotnet-script src/01.cs
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
