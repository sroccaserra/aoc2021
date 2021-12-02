import Data.Char
import Text.ParserCombinators.ReadP

import Common (getParsedLines, unsigned)

main = do
  input <- getParsedLines 2 parser
  print $ partOne input
  print $ partTwo input

partOne moves = x*y
  where (x, y) = foldl step_1 (0, 0) moves

partTwo moves = x*y
  where (_, x, y) = foldl step_2 (0, 0, 0) moves

step_1 (x, y) ("forward ", n) = (x + n, y)
step_1 (x, y) ("up ", n) = (x, y - n)
step_1 (x, y) ("down ", n) = (x, y + n)

step_2 (aim, x, y) ("forward ", n) = (aim, x + n, y + n*aim)
step_2 (aim, x, y) ("up ", n) = (aim - n, x, y)
step_2 (aim, x, y) ("down ", n) = (aim + n, x, y)

parser :: ReadP (String, Int)
parser = (,) <$> munch1 (not . isDigit) <*> unsigned
