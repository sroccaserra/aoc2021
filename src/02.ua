Split ← &i "common/common.ua" "Split"
SplitLines ← &i "common/common.ua" "SplitLines"

Parse ← ⍜(⊡1)(⊐parse) ⊐Split" "
SelectValues ← |2 ×⌕□⊙⊃≡⊢≡(⊔⊏1)
Acc ← |2 +⊂:×⊙(⊢.)⊏1,

Solve ← (|1.2
  ⊞(SelectValues∩⊔) {"forward" "down" "up"} □
  ⍉⊟:-/∘
  ∧Acc:0_0_0
  ∩(/×⊏)0_2,0_1
)

Commands ← ∵Parse SplitLines &fras"src/02.in"
Solve Commands

---
TestLines ← {"forward 5" "down 5" "forward 8" "up 3" "down 8" "forward 2"}

TestCommands ← .∵Parse TestLines
⍤:≍,[{"forward" 5} {"down" 5} {"forward" 8} {"up" 3} {"down" 8} {"forward" 2}]

SelectValues "forward" TestCommands
⍤:≍,[5 0 8 0 0 2]

⊞(SelectValues∩⊔) {"forward" "down" "up"} □TestCommands
⍤:≍,[5_0_8_0_0_2
     0_5_0_0_8_0
     0_0_0_3_0_0]

⍉⊟:-/∘[5_0_8_0_0_2 0_5_0_0_8_0 0_0_0_3_0_0]
⍤:≍,[5_0 0_5 8_0 0_¯3 0_8 2_0]

⍤:≍,5_0_0 Acc5_0 0_0_0
⍤:≍,5_5_0 Acc0_5 5_0_0
⍤:≍,13_5_40 Acc8_0 5_5_0

⍤:≍,15_10_60 ∧Acc [5_0 0_5 8_0 0_¯3 0_8 2_0] 0_0_0

⍤:≍,150_900 ⊂: Solve TestCommands

# Not used, but I learned something
+⊂:⊙:40 5_5_0 8_0
⍤:≍,+⊃⋅∘⟜(⊂:)40 5_5_0 8_0

# More mathy solution, from https://github.com/dzaima/aoc/blob/master/2021/BQN/2.bqn
⊃≡⊢≡(parse⊢⇌⊔) TestLines
Firsts ←
Values ←
f ← =@f Firsts
d ← /-⊞="ud" Firsts
Aims ← \+× d Values
Horiz ← /+× f Values
⍤.=150 ×Horiz⊢⇌Aims
⍤.=900 ×Horiz/+×Values×f Aims

# Parse with primitives only
PrimitiveParse ← {⊃(▽≥@a.)(-@0⊢⇌)}⊔
∵PrimitiveParse TestLines
⍤:≍,[{"forward" 5} {"down" 5} {"forward" 8} {"up" 3} {"down" 8} {"forward" 2}]
---
