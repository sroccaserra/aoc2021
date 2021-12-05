import Data.List
import Text.ParserCombinators.ReadP

import Common (getParsedLines, Coord(..), unsigned, bresenham)

main = do
  input <- getParsedLines 5 parser
  print $ partTwo input

partTwo :: [(Coord, Coord)] -> Int
partTwo = length . filter ((> 1) . length) . group . sort . concatMap (uncurry bresenham)

parser = (,) <$> coordParser <* string " -> " <*> coordParser
coordParser = Coord <$> unsigned <* char ',' <*> unsigned
