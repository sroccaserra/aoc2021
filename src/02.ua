Split ← &i "common/common.ua" "Split"

Parse ← ⍜(⊡1)(⊐parse) ⊐Split" "
SelectValues ← |2 ×⌕□∶⊙∶≡⊢∶≡(⊔⊏1).
Acc ← ∘

SolveOne ← (|1
  ⊞(SelectValues ∶∩⊔) {"forward" "down" "up"} □
  ⍉⊟∶-/∘
)

---
TestLines ← {"forward 5" "down 5" "forward 8" "up 3" "down 8" "forward 2"}

TestCommands ← .∵Parse TestLines
⍤∶≍, [{"forward" 5} {"down" 5} {"forward" 8} {"up" 3} {"down" 8} {"forward" 2}]

SelectValues TestCommands "forward"
⍤∶≍,[5 0 8 0 0 2]

⊞(SelectValues ∶∩⊔) {"forward" "down" "up"} □TestCommands
⍤∶≍, [5_0_8_0_0_2
      0_5_0_0_8_0
      0_0_0_3_0_0]

⍉⊟∶-/∘[5_0_8_0_0_2 0_5_0_0_8_0 0_0_0_3_0_0]
⍤∶≍, [5_0 0_5 8_0 0_¯3 0_8 2_0]

/Acc⇌⊂{0_0_0}≡□[5_0 0_5 8_0 0_¯3 0_8 2_0]

SolveOne TestCommands

dump∘
---
