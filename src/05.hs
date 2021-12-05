import Data.List
import Text.ParserCombinators.ReadP

import Common (getParsedLines, Coord(..), unsigned, bresenham)

main = do
  input <- getParsedLines 5 parser
  print $ partOne input
  print $ partTwo input

partOne = partTwo . filter isHorizontalOrVertical

partTwo :: [(Coord, Coord)] -> Int
partTwo = length . filter ((> 1) . length) . group . sort . concatMap (uncurry bresenham)

isHorizontalOrVertical (Coord x1 y1, Coord x2 y2) = x1 == x2 || y1 == y2

parser = (,) <$> coordParser <* string " -> " <*> coordParser
coordParser = Coord <$> unsigned <* char ',' <*> unsigned
