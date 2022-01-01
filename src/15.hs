import Data.List (foldl')
import Text.ParserCombinators.ReadP

import Common (getParsedLines, Coord(..), emptyPq, updatePq, removeMinPq)

main = do
  input <- getParsedLines 15 parser
  print $ solve input 1
  print $ solve input 5

solve grid scale = lowestRiskUcs grid w h scale
  where w = length . head $ grid
        h = length grid

lowestRiskUcs grid w h scale = go frontier
  where (w_s, h_s) = (w*scale, h*scale)
        src = Coord 0 0
        dst = Coord (w_s -1) (h_s -1)
        frontier = updatePq emptyPq (0, src)
        go pq = if point == dst
                   then pastCost
                   else go pq''
          where ((pastCost, point), pq') = removeMinPq pq
                ns = neighbors w_s h_s point
                pq'' = foldl' (processNeighbor grid w h pastCost) pq' ns

processNeighbor grid w h pastCost pq n = updatePq pq (pastCost + cost, n)
  where cost = computeRisk grid w h n

neighbors w_s h_s (Coord x y) = filter (isInBound w_s h_s) $ candidates
  where candidates = [Coord (x-1) y, Coord (x+1) y, Coord x (y-1), Coord x (y+1)]
        isInBound w h (Coord x y) = (0 <= x) && (x < w) && (0 <= y) && (y < h)

computeRisk grid w h (Coord x y) = (res - 1) `mod` 9 + 1
  where bonus = div x w + div y h
        res = grid !! (mod y h) !! (mod x w) + bonus

parser :: ReadP [Int]
parser = many1 $ read . (:[]) <$> get
