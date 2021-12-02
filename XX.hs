import Text.ParserCombinators.ReadP

import Common (getParsedLines)

main = do
  input <- getParsedLines X parser
  print $ partOne input

partOne = id

parser :: ReadP 
parser = 
