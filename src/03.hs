import Data.List
import Text.ParserCombinators.ReadP

import Common (getDayRawInput)

main = do
  input <- lines <$> getDayRawInput 3
  let matrix = map (read . (:[])) <$> input
  print $ partOne matrix

partOne matrix = toDec gamma * toDec epsilon
  where nbColumns = length $ head matrix
        stats = map (colStat matrix) [0..nbColumns-1]
        gamma = map mostFrequent stats
        epsilon = map flipNumber gamma

colStat matrix n = foldl incStat (0, 0) $ col n matrix

incStat (x, y) 0 = (x + 1, y)
incStat (x, y) 1 = (x, y + 1)

col n = map (!! n)

mostFrequent (nbZeros, nbOnes) = if nbOnes >= nbZeros then 1 else 0

flipNumber c = if 0 == c then 1 else 0

toDec = foldl1' $ (+) . (*2)
