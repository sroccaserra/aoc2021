ToNum ← ⊑-⟜'0'
Parse ← ¯2⊸↓⋈ToNum∘(¯1⊸↑)
Match ← {𝕏𝕨}´

Apply ← {
  Match 𝕩‿{
    "forward"‿v: 1‿0×v;
    "up"‿v: 0‿¯1×v;
    "down"‿v: 0‿1×v;
    𝕩: 𝕩!0
  }
}

Solve1 ← ×´·+´Apply¨

cs ← Parse¨•FLines•wdpath∾"/"∾⊑•args
•Show Solve1 cs

##
# Tests

lines ← "forward 5"‿"down 5"‿"forward 8"‿"up 3"‿"down 8"‿"forward 2"
"forward"‿5 (⊢!≡) Parse ⊑lines
150 (⊢!≡) Solve1 Parse¨ lines
