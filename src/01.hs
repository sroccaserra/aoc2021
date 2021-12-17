import Common (getDayLines)

main = do
  input <- getDayLines 1
  let ns = read <$> input :: [Int]
  print $ partOne ns
  print $ partTwo ns

partOne ns = length $ filter (> 0) diffs
  where diffs = zipWith (-) (tail ns) ns

partTwo = partOne . sums

sums (x:y:z:rest) = (x + y + z):sums (y:z:rest)
sums _ = []
