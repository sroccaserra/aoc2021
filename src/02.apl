'display' 'disp'⎕CY'dfns'

forward ← ,∘0
up ← 0,-
down ← 0∘,

Acc ← { _ a _ ← ⍵ ⋄ u v ← ⍺ ⋄ ⍵ + u v (a×u) }

Solve ← {
  hPos d1 d2 ← ↑(Acc/⌽(⊆0 0 0)∘, ⍎¨ ⍵)
  (hPos×d1) (hPos×d2)
}

lines ← ⊃ ⎕NGET'src/02.in'1
⎕ ← Solve lines

⍝⍝
⍝ Tools

print ← { ⎕ ← disp ⍵ }
⍝ Assert
A ← { 0∊⍵:(⍕ ⍺) ⎕SIGNAL 8 ⋄ 1:shy←0 }
⍝ Assert Equals
E ← ⊢A≡

⍝⍝
⍝ Tests

⍝ command functions
5 0 E forward 5
0 6 E down 6
0 ¯6 E up 6
⍝ Reducing
5 0 0 E 5 0 Acc 0 0 0
5 5 0 E 0 5 Acc 5 0 0
13 5 40 E 8 0 Acc 5 5 0
5 0 0 E ↑Acc/(5 0) (0 0 0)
13 5 40 E ↑Acc/(8 0) (0 5) (5 0) (0 0 0)
⍝ Solving
lines ← 'forward 5' 'down 5' 'forward 8' 'up 3' 'down 8' 'forward 2'
150 900 E Solve lines

⍝⍝
⍝ Unused, but I learned something

Words ← ' '∘(≠⊆⊢)
'forward' (,'5') E Words 'forward 5'

Parse ← (1∘↑,(⍎2∘⊃)) Words
'forward' 5 E Parse 'forward 5'

Solve1 ← ×/(+⌿∘↑⍎¨)
150 E Solve1 lines
