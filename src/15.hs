import Text.ParserCombinators.ReadP

import Common (getParsedLines, neighbors, ucs)

main = do
  input <- getParsedLines 15 parser
  print $ solve input 1
  print $ solve input 5

solve grid scale = lowestRisk grid w h scale
  where w = length . head $ grid
        h = length grid

lowestRisk grid w h scale = ucs adjs computeCost src dst
  where (w_s, h_s) = (w*scale, h*scale)
        src = (0, 0)
        dst = (pred w_s, pred h_s)
        adjs = neighbors w_s h_s
        computeCost = computeRisk grid w h

computeRisk grid w h (x, y) = succ (mod (pred value) 9)
  where bonus = div x w + div y h
        value = grid !! (mod y h) !! (mod x w) + bonus

parser :: ReadP [Int]
parser = many1 $ read . (:[]) <$> get
