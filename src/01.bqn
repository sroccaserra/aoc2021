ns ← •ParseFloat¨ •FLines "01.in"

Solve1 ← +´·<⟜0·-˝˘2⊸↕
Solve2 ←  Solve1·+˝˘3⊸↕

•Show Solve1 ns
•Show Solve2 ns

##
# Tests

example ← 199‿200‿208‿210‿200‿207‿240‿269‿260‿263
7 (⊢!≡) Solve1 example
5 (⊢!≡) Solve2 example
