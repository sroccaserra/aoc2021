EOL ← "\r\n"
Split ← |2 ⊜□¬∊,
Lines ← |1 Split EOL

Input ← Lines &fras "src/01.in"

SolveOne ← /+≡/>◫2
SolveTwo ← SolveOne≡/+◫3

⊃SolveOne SolveTwo ≡(parse ⊔) Input

---
TestLines ← "199"_"200"_"208"_"210"_"200"_"207"_"240"_"269"_"260"_"263"
TestNumbers ← ≡parse TestLines
⍤∶≍, 7 SolveOne TestNumbers
⍤∶≍, 5 SolveTwo TestNumbers
---
