import Data.List (foldl')
import Text.ParserCombinators.ReadP

import Common (getParsedLines, Point(..), neighbors, emptyPq, updatePq, removeMinPq)

main = do
  input <- getParsedLines 15 parser
  print $ solve input 1
  print $ solve input 5

solve grid scale = lowestRiskUcs grid w h scale
  where w = length . head $ grid
        h = length grid

lowestRiskUcs grid w h scale = go frontier
  where (w_s, h_s) = (w*scale, h*scale)
        src = Point 0 0
        dst = Point (pred w_s) (pred h_s)
        frontier = updatePq emptyPq (0, src)
        go pq = if point == dst
                   then pastCost
                   else go pq''
          where ((pastCost, point), pq') = removeMinPq pq
                ns = neighbors w_s h_s point
                pq'' = foldl' (processNeighbor grid w h pastCost) pq' ns

processNeighbor grid w h pastCost pq n = updatePq pq (pastCost + cost, n)
  where cost = computeRisk grid w h n

computeRisk grid w h (Point x y) = succ (mod (pred value) 9)
  where bonus = div x w + div y h
        value = grid !! (mod y h) !! (mod x w) + bonus

parser :: ReadP [Int]
parser = many1 $ read . (:[]) <$> get
