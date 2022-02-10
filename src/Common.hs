module Common
  where

import Control.Applicative
import Data.Char (isDigit)
import Data.Hashable
import Data.HashMap.Strict (HashMap, (!), (!?))
import qualified Data.HashMap.Strict as HashMap
import Data.List(foldl', foldl1', group, sort, unfoldr)
import Data.Map (Map)
import qualified Data.Map as Map
import Data.Set (Set)
import qualified Data.Set as Set
import System.Environment
import Text.ParserCombinators.ReadP
import Text.Printf

getDayRawInput :: Int -> IO String
getDayRawInput day = do
  args <- getArgs
  case args of
       [] -> readFile (printf "src/%02d.in" day)
       "-":_ -> getContents
       fileName:_ -> readFile fileName

getDayLines :: Int -> IO [String]
getDayLines day = lines <$> getDayRawInput day

getDayLine :: Int -> IO String
getDayLine day = head <$> getDayLines day

getParsedLines :: Int -> ReadP a -> IO [a]
getParsedLines day parser = map (parseLine parser) <$> getDayLines day

parseLine :: ReadP a -> String -> a
parseLine p = fst . last . readP_to_S p

unsigned :: ReadP Int
unsigned = read <$> munch1 isDigit

signed :: ReadP Int
signed = option id sign <*> unsigned
  where
    sign :: ReadP (Int -> Int)
    sign = (id <$ char '+') <|> (negate <$ char '-')


---
-- Lists

countByEq :: Eq a => Ord a => [a] -> [(a, Int)]
countByEq = map (\ps@(p:_) -> (p, length ps)) . group . sort

---
-- Misc

toDec = foldl1' $ (+) . (*2)

neighbors w h (x, y) = filter (isInBound w h) $ candidates
  where candidates = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        isInBound w h (x, y) = (0 <= x) && (x < w) && (0 <= y) && (y < h)

---
-- Points

data Point = Point !Int !Int
           deriving (Show, Eq, Ord)

instance Hashable Point where
  hash (Point x y) = hash (x, y)
  hashWithSalt n (Point x y) = hashWithSalt n (x, y)

_x :: Point -> Int
_x (Point x _) = x

_y :: Point -> Int
_y (Point _ y) = y

boundingBox :: [Point] -> (Point, Point)
boundingBox cs = (Point (minimum xs) (minimum ys), Point (maximum xs) (maximum ys))
  where
    xs = map _x cs
    ys = map _y cs

neighborPoints w h (Point x y) = filter (isInBound w h) $ candidates
  where candidates = [Point (x-1) y, Point (x+1) y, Point x (y-1), Point x (y+1)]
        isInBound w h (Point x y) = (0 <= x) && (x < w) && (0 <= y) && (y < h)

bresenham :: Point -> Point -> [Point]
bresenham pa@(Point xa ya) pb@(Point xb yb) = map maySwitch . unfoldr go $ (x1,y1,0)
  where
    steep = abs (yb - ya) > abs (xb - xa)
    maySwitch = if steep then (\(Point x y) -> (Point y x)) else id
    [(Point x1 y1), (Point x2 y2)] = sort [maySwitch pa, maySwitch pb]
    deltax = x2 - x1
    deltay = abs (y2 - y1)
    ystep = if y1 < y2 then 1 else -1
    go (xTemp, yTemp, error)
      | xTemp > x2 = Nothing
      | otherwise  = Just ((Point xTemp yTemp), (xTemp + 1, newY, newError))
      where
        tempError = error + deltay
        (newY, newError) = if (2*tempError) >= deltax
                              then (yTemp+ystep,tempError-deltax)
                              else (yTemp,tempError)

-- `c` is the default char
-- example of building a `Map Point Char` from a list of points:
-- m = Map.fromList $ zip points (range ('a', 'z') ++ range ('A', 'Z'))
showAsciiGrid :: Char -> Map Point Char -> String
showAsciiGrid c m = unlines $ do
    y <- [minY..maxY]
    return [Map.findWithDefault c (Point x y) m | x <- [minX..maxX]]
  where
    (Point minX minY, Point maxX maxY) = boundingBox $ Map.keys m

---
-- Search & Priority Queue

-- Uniform Cost Search
ucs adjs computeCost src dst = fst . fst $ until isDone visit ((0, src), emptyPq)
  where isDone = (== dst) . snd . fst
        visit ((cost, vertex), frontier) = removeMinPq frontier'
          where ns = adjs vertex
                frontier' = foldl' (processNeighbor cost) frontier ns
        processNeighbor pastCost pq n = updatePq pq (pastCost + computeCost n, n)

data PriorityQueue n v = Pq (Set (n, v)) (HashMap v n)

-- The set plays the role of a heap, and the map keeps track of visited values
emptyPq = Pq Set.empty HashMap.empty

updatePq :: (Ord n, Ord v, Eq v, Hashable v) => PriorityQueue n v -> (n, v) -> PriorityQueue n v
updatePq (Pq h m) (newPriority, value)
  | (not $ HashMap.member value m) || (newPriority < (m ! value))
    = Pq (Set.insert (newPriority, value) h) (HashMap.insert value newPriority m)
updatePq pq _ = pq

-- Visited values have their priority set to minBound in the map
removeMinPq :: (Bounded n, Ord n, Eq v, Hashable v) => PriorityQueue n v -> ((n, v), PriorityQueue n v)
removeMinPq (Pq h m) = if Just minBound == m !? value
                          then removeMinPq (Pq h' m)
                          else ((priority, value), Pq h' (HashMap.insert value minBound m))
  where ((priority, value), h') = Set.deleteFindMin h
