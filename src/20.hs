import Data.Maybe (fromJust)
import qualified Data.Map as Map

import Common (getDayLines, countByEq, toDec, Point(..))

main = do
  input <- getDayLines 20
  let algo = head input
  let lines = (tail.tail) input
  print $ solve 2 algo lines
  print $ solve 50 algo lines

solve n algo lines =  countLit (last . take (succ n) $ iterate (enhance algo) (0, lines))
  where countLit (_, lines) = fromJust . lookup '#' . countByEq $ foldl1 (++) lines

enhance algo (n, lines) = (succ n, lines')
  where w = length $ head lines
        h = length lines
        lines' = [[algo !! (index d m (Point x y)) | x <- [-1..w]] | y <- [-1..h]]
        m = Map.fromList (zipWith (,) coords (foldl1 (++) lines))
        coords = [Point x y | y <- [0..h-1], x <- [0..w-1]]
        d = if 0 == n `mod` 2 then '.' else (head algo)

index d m (Point x y) = fromInteger $ toDec $ toBit <$> map (\c -> Map.findWithDefault d c m) points
  where points = flip Point <$> [y-1..y+1] <*> [x-1..x+1]
        toBit c = if c == '#' then 1 else 0
