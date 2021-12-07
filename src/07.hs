import Text.ParserCombinators.ReadP

import Common (getParsedLines, unsigned)

main = do
  input <- head <$> getParsedLines 7 parser
  print $ solve distanceFuelAdder input
  print $ solve incrementingFuelAdder input

solve fuelAdder ns = minimum $ map (\x -> foldl (fuelAdder x) 0 ns) [x1..x2]
  where x1 = minimum ns
        x2 = maximum ns

distanceFuelAdder x s n = s + abs(n - x)

incrementingFuelAdder x s n = s + div (steps*(steps+1)) 2
  where steps = abs(n - x)

parser :: ReadP [Int]
parser = sepBy1 unsigned (char ',')
