import Data.Set (union)
import qualified Data.Set as Set

import Common (getDayLines)

main = do
  input <- getDayLines 25
  print $ solve input

solve floor = succ . length . takeWhile (\a -> step w h a /= a) $ iterate (step w h) (easts, souths)
  where w = length $ head floor
        h = length floor
        easts = Set.fromList [(x, y) | x <- [0..w-1], y <- [0..h-1], (floor !! y) !! x == '>']
        souths = Set.fromList [(x, y) | x <- [0..w-1], y <- [0..h-1], (floor !! y) !! x == 'v']

step w h (easts, souths) = (easts', souths')
  where occupied = union easts souths
        tryEast e | Set.member dest occupied = e
          where dest = eastOfTheSun w e
        tryEast e = eastOfTheSun w e
        easts' = Set.map tryEast easts
        occupied' = union easts' souths
        trySouth e | Set.member dest occupied' = e
          where dest = southOfTheMoon h e
        trySouth e = southOfTheMoon h e
        souths' = Set.map trySouth souths

-- asString w h (easts, souths) = [[asChar (x, y) | x <- [0..w-1]] | y <- [0..h-1]]
--   where asChar p = if Set.member p easts then '>' else (if Set.member p souths then 'v' else '.')

eastOfTheSun w (x, y) | x == w-1 = (0, y)
eastOfTheSun _ (x, y) = (x + 1, y)

southOfTheMoon h (x, y) | y == h-1 = (x, 0)
southOfTheMoon _ (x, y) = (x, y + 1)
