Solve1 ← +´·<˝˘2⊸↕
Solve2 ←  Solve1·+˝˘3⊸↕

ns ← •ParseFloat¨•FLines•wdpath∾"/"∾⊑•args
•Show (Solve1⋈Solve2) ns

##
# Tests

7‿5 (⊢!≡) (Solve1⋈Solve2) 199‿200‿208‿210‿200‿207‿240‿269‿260‿263
