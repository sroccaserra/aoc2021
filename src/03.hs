import Data.List

import Common (getDayLines)

main = do
  input <- getDayLines 3
  let matrix = map (read . (:[])) <$> input
  print $ partOne matrix
  print $ partTwo matrix

partOne matrix = toDec gamma * toDec epsilon
  where nbColumns = length $ head matrix
        stats = map (colStat matrix) [0..nbColumns-1]
        gamma = map mostFrequent stats
        epsilon = map flipNumber gamma

partTwo matrix = toDec o2 * toDec co2
  where nbColumns = length $ head matrix
        o2 = head $ foldl stepO2 matrix [0..nbColumns-1]
        co2 = head $ foldl stepCO2 matrix [0..nbColumns-1]

colStat matrix n = foldl incStat (0, 0) $ map (!! n) matrix

incStat (x, y) 0 = (x + 1, y)
incStat (x, y) 1 = (x, y + 1)

mostFrequent (nbZeros, nbOnes) = if nbOnes >= nbZeros then 1 else 0

flipNumber c = if 0 == c then 1 else 0

toDec = foldl1' $ (+) . (*2)

stepO2 [lastRow] _ = [lastRow]
stepO2 matrix n = filter ((b==).(!!n)) matrix
  where nbColumns = length $ head matrix
        stats = map (colStat matrix) [0..nbColumns-1]
        b = mostFrequent $ stats !! n

stepCO2 [lastRow] _ = [lastRow]
stepCO2 matrix n = filter ((b==).(!!n)) matrix
  where nbColumns = length $ head matrix
        stats = map (colStat matrix) [0..nbColumns-1]
        b = flipNumber $ mostFrequent $ stats !! n
