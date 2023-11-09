Lines ← &i "common/common.ua" "Lines"

Input ← Lines &fras "src/01.in"

SolveOne ← /+≡/>◫2
SolveTwo ← SolveOne≡/+◫3

∩&s ⊃SolveOne SolveTwo ⊐≡parse Input

---
TestLines ← {"199" "200" "208" "210" "200" "207" "240" "269" "260" "263"}
TestNumbers ← ⊐≡parse TestLines
⍤∶≍, 7 SolveOne TestNumbers
⍤∶≍, 5 SolveTwo TestNumbers
---
