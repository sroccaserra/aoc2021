import Data.Set (Set)
import qualified Data.Set as Set
import Data.HashMap.Strict (HashMap, (!), (!?))
import qualified Data.HashMap.Strict as HashMap
import Text.ParserCombinators.ReadP

import Common (getParsedLines, Coord(..))

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
        frontier = updatePq emptyPq src 0
        go pq = if point == dst
                   then pastCost
                   else go pq''
          where ((point, pastCost), pq') = removeMinPq pq
                ns = neighbors w_s h_s point
                pq'' = foldl (processNeighbor grid w h scale pastCost) pq' ns

processNeighbor grid w h scale pastCost pq n = updatePq pq n (pastCost + cost)
  where cost = computeRisk grid w h scale n

neighbors w_s h_s (Coord x y) = filter (isInBound w_s h_s) $ candidates
  where candidates = [Coord (x-1) y, Coord (x+1) y, Coord x (y-1), Coord x (y+1)]
        isInBound w h (Coord x y) = (0 <= x) && (x < w) && (0 <= y) && (y < h)

computeRisk grid w h scale (Coord x y) = (res - 1) `mod` 9 + 1
  where bonus = div x w + div y h
        res = grid !! (mod y h) !! (mod x w) + bonus

data PriorityQueue = Pq (Set (Int, Coord)) (HashMap Coord Int)

emptyPq = Pq Set.empty HashMap.empty

updatePq :: PriorityQueue -> Coord -> Int -> PriorityQueue
updatePq (Pq h m) state newPriority
  | (not $ HashMap.member state m) || (newPriority < (m ! state))
    = Pq (Set.insert (newPriority, state) h) (HashMap.insert state newPriority m)
updatePq pq _ _ = pq

done = -100000

removeMinPq :: PriorityQueue -> ((Coord, Int), PriorityQueue)
removeMinPq (Pq h m) = if Just done == m !? point
                                      then removeMinPq (Pq h' m)
                                      else ((point, priority), Pq h' (HashMap.insert point done m))
  where ((priority, point), h') = Set.deleteFindMin h

parser :: ReadP [Int]
parser = many1 $ read . (:[]) <$> get
