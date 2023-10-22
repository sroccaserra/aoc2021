ToNum ← ⊑-⟜'0'
Parse ← ¯2⊸↓⋈ToNum∘(¯1⊸↑)
Match ← {𝕏𝕨}´

ToVec ← {
  c‿n:
  Match c‿{
    "forward": n‿0;
    "up": 0‿(-n);
    "down": 0‿n;
    𝕩: 𝕩!0
  }
}

Apply ← {
  command𝕊h‿a‿d:
  f‿v ← ToVec command
  (h+f)‿(a+v)‿(d+a×f)
}

Solve ← { ×´¨(0‿1⊸⊏⋈0‿2⊸⊏)0‿0‿0 Apply´⌽ 𝕩 }

cs ← Parse¨•FLines•wdpath∾"/"∾⊑•args
•Show Solve cs

##
# Tests

# Parsing
lines ← "forward 5"‿"down 5"‿"forward 8"‿"up 3"‿"down 8"‿"forward 2"
"forward"‿5 (⊢!≡) Parse ⊑lines
5‿0 (⊢!≡) ToVec "forward"‿5
0‿(-3) (⊢!≡) ToVec "up"‿3
0‿2 (⊢!≡) ToVec "down"‿2
# Computing
5‿0‿0 (⊢!≡) "forward"‿5 Apply 0‿0‿0
5‿5‿0 (⊢!≡) "down"‿5 Apply 5‿0‿0
13‿5‿40 (⊢!≡) "forward"‿8 Apply 5‿5‿0
# Solving
150‿900 (⊢!≡) Solve Parse¨ lines
