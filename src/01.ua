SplitLines ← &i "common/common.ua" "SplitLines"

SolveOne ← /+≡/>◫2
SolveTwo ← SolveOne≡/+◫3

Numbers ← ⊐≡parse SplitLines &fras"src/01.in"
∩&s ⊃SolveOne SolveTwo Numbers

---
TestLines ← {"199" "200" "208" "210" "200" "207" "240" "269" "260" "263"}
TestNumbers ← ⊐≡parse TestLines
199_200_208_210_200_207_240_269_260_263
⍤:≍, TestNumbers

⍤:≍, 7 SolveOne TestNumbers
⍤:≍, 5 SolveTwo TestNumbers
---
