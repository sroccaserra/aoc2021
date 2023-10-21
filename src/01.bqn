ns ← •ParseFloat¨ •FLines "01.in"

Solve1 ← +´·<⟜0·-˝˘2⊸↕
Solve2 ←  Solve1·+˝˘3⊸↕

•Show (Solve1⋈Solve2) ns

##
# Tests

7‿5 (⊢!≡) (Solve1⋈Solve2) 199‿200‿208‿210‿200‿207‿240‿269‿260‿263
