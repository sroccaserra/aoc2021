import Data.List (sort)

import Common (getDayLines)

main = do
  input <- getDayLines 10
  print $ partOne input
  print $ partTwo input

partOne = sum . map score
  where score = go []
        go stack (op:cs) | elem op "([{<" = go (op:stack) cs
        go (op:stack) (cl:cs) | matches op cl = go stack cs
        go _ (cl:_) = points cl
        go _ [] = 0
        points ')' = 3
        points ']' = 57
        points '}' = 1197
        points '>' = 25137

partTwo lines = scores !! (length scores `div` 2)
  where scores = sort $ filter (> 0) $ map score lines
        score = go []
        go stack (op:cs) | elem op "([{<" = go (op:stack) cs
        go (op:stack) (cl:cs) | matches op cl =  go stack cs
        go stack [] = foldl (\acc c -> acc*5 + points c) 0 stack
        go _ _ = 0
        points '(' = 1
        points '[' = 2
        points '{' = 3
        points '<' = 4

matches '(' ')' = True
matches '[' ']' = True
matches '{' '}' = True
matches '<' '>' = True
matches _ _ = False
