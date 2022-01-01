import Data.List
import Text.ParserCombinators.ReadP

import Common (getParsedLines, unsigned, Point(..))

main = do
  input <- getParsedLines 5 parser
  print $ partOne input
  print $ partTwo input

partOne = partTwo . filter isHorizOrVert
  where isHorizOrVert (Point x1 y1, Point x2 y2) = x1 == x2 || y1 == y2

partTwo = length . filter ((> 1) . length) . group . sort . concatMap (uncurry pointsBetween)

pointsBetween p@(Point x1 y1) (Point x2 y2) = take (n+1) (iterate inc p)
  where (dx, dy) = (x2 - x1, y2 - y1)
        incX = if dx == 0 then 0 else if dx > 0 then 1 else -1
        incY = if dy == 0 then 0 else if dy > 0 then 1 else -1
        n = max (abs dx) (abs dy)
        inc (Point x y) = Point (x + incX) (y + incY)

parser = (,) <$> coordParser <* string " -> " <*> coordParser
coordParser = Point <$> unsigned <* char ',' <*> unsigned
