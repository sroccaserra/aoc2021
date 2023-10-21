ToNum ← ⊑-⟜'0'
Parse ← ¯2⊸↓⋈ToNum∘(¯1⊸↑)
Match ← {𝕏𝕨}´

Apply ← {
  c𝕊h‿a‿d:
  Match c‿{
    "forward"‿v: h‿a‿d+v‿0‿(a×v);
    "up"‿v: h‿a‿d+0‿(-v)‿0;
    "down"‿v: h‿a‿d+0‿v‿0;
    𝕩: 𝕩!0
  }
}

Solve ← {
  vals ← 0‿0‿0 Apply´⌽ 𝕩
  ×´¨(0‿1⊸⊏⋈0‿2⊸⊏)vals
}

cs ← Parse¨•FLines•wdpath∾"/"∾⊑•args
•Show Solve cs

##
# Tests

lines ← "forward 5"‿"down 5"‿"forward 8"‿"up 3"‿"down 8"‿"forward 2"
"forward"‿5 (⊢!≡) Parse ⊑lines
150‿900 (⊢!≡) Solve Parse¨ lines
