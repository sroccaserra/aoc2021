Parse ← ¯2⊸↓⋈•ParseFloat∘(¯1⊸↑)

Apply ← {
 "forward"‿n𝕊h‿a‿d: h‿a‿d+n‿0‿(a×n);
 "up"‿n𝕊𝕩: 𝕩+0‿(-n)‿0;
 "down"‿n𝕊𝕩: 𝕩+0‿n‿0
}

Solve ← {
  h‿a‿d ← 0‿0‿0 Apply´⌽ 𝕩
  (h×a)‿(h×d)
}

commands ← Parse¨•FLines•wdpath∾"/"∾⊑•args
•Show Solve commands

##
# Tests

# Parsing
"forward"‿5 (⊢!≡) Parse "forward 5"
# Applying
5‿0‿0 (⊢!≡) "forward"‿5 Apply 0‿0‿0
5‿5‿0 (⊢!≡) "down"‿5 Apply 5‿0‿0
13‿5‿40 (⊢!≡) "forward"‿8 Apply 5‿5‿0
# Solving
lines ← "forward 5"‿"down 5"‿"forward 8"‿"up 3"‿"down 8"‿"forward 2"
150‿900 (⊢!≡) Solve Parse¨ lines
