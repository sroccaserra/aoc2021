import Text.ParserCombinators.ReadP

import Common (getDayLines)

main = do
  input <- getDayLines 10
  print $ partOne input

partOne = sum . map score

score line = go line []
  where go [] _ = 0
        go (op:cs) stack | elem op "([{<" = go cs (op:stack)
        go (cl:cs) (op:stack) | matches op cl = go cs stack
        go (cl:_) _ = points cl

matches '(' ')' = True
matches '[' ']' = True
matches '{' '}' = True
matches '<' '>' = True
matches _ _ = False

points ')' = 3
points ']' = 57
points '}' = 1197
points '>' = 25137
