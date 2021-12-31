module Common
  where

import Control.Applicative
import Data.Char (isDigit)
import Data.List(foldl1', group, sort, unfoldr)
import Data.Map (Map)
import qualified Data.Map as Map
import Data.Hashable
import Text.ParserCombinators.ReadP
import System.Environment
import Text.Printf

getDayRawInput :: Int -> IO String
getDayRawInput day = do
  args <- getArgs
  case args of
       [] -> readFile (printf "src/%02d.txt" day)
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

---
-- Coords

data Coord = Coord !Int !Int
           deriving (Show, Eq, Ord)

instance Hashable Coord where
  hash (Coord x y) = hash (x, y)
  hashWithSalt n (Coord x y) = hashWithSalt n (x, y)

_x :: Coord -> Int
_x (Coord x _) = x

_y :: Coord -> Int
_y (Coord _ y) = y

boundingBox :: [Coord] -> (Coord, Coord)
boundingBox cs = (Coord (minimum xs) (minimum ys), Coord (maximum xs) (maximum ys))
  where
    xs = map _x cs
    ys = map _y cs

bresenham :: Coord -> Coord -> [Coord]
bresenham pa@(Coord xa ya) pb@(Coord xb yb) = map maySwitch . unfoldr go $ (x1,y1,0)
  where
    steep = abs (yb - ya) > abs (xb - xa)
    maySwitch = if steep then (\(Coord x y) -> (Coord y x)) else id
    [(Coord x1 y1), (Coord x2 y2)] = sort [maySwitch pa, maySwitch pb]
    deltax = x2 - x1
    deltay = abs (y2 - y1)
    ystep = if y1 < y2 then 1 else -1
    go (xTemp, yTemp, error)
        | xTemp > x2 = Nothing
        | otherwise  = Just ((Coord xTemp yTemp), (xTemp + 1, newY, newError))
        where
          tempError = error + deltay
          (newY, newError) = if (2*tempError) >= deltax
                            then (yTemp+ystep,tempError-deltax)
                            else (yTemp,tempError)

-- `c` is the default char
-- example of building a `Map Coord Char` from a list of points:
-- m = Map.fromList $ zip points (range ('a', 'z') ++ range ('A', 'Z'))
showAsciiGrid :: Char -> Map Coord Char -> String
showAsciiGrid c m = unlines $ do
    y <- [minY..maxY]
    return [Map.findWithDefault c (Coord x y) m | x <- [minX..maxX]]
  where
    (Coord minX minY, Coord maxX maxY) = boundingBox $ Map.keys m
