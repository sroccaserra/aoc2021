solve1 ← +/∘(</⍨∘2)
solve2 ← solve1∘(+/⍨∘3)

contents ← ⊃ ⎕NGET'src/01.in'1
numbers ← ⍎¨ contents
⎕ ← solve1 numbers
⎕ ← solve2 numbers
