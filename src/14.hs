import Data.Map.Strict ((!))
import qualified Data.Map as Map
import Text.ParserCombinators.ReadP

import Common (getDayLines, parseLine, countByEq)

main = do
  (polymer:_:ruleLines) <- getDayLines 14
  let rules = Map.fromList $ map (parseLine parser) ruleLines
  print $  solve polymer rules 10
  print $  solve polymer rules 40

solve polymer rules n = maximum counts - minimum counts
  where pc = countPairs polymer
        lc = Map.fromList $ countByEq polymer
        (_, lc') = last $ take (succ n) $ iterate (step rules) (pc, lc)
        counts = Map.elems lc'

countPairs polymer = Map.fromList $ countByEq pairs
  where pairs = zip polymer (tail polymer)

step rules (pc, lc) = Map.foldlWithKey (addPair rules) (pc, lc) pc

addPair rules (pc, lc) pair@(left,right) n = ((f.g.h) pc, lc')
  where mid = rules ! pair
        f = Map.insertWith (+) pair (-n)
        g = Map.insertWith (+) (left, mid) n
        h = Map.insertWith (+) (mid, right) n
        lc' = Map.insertWith (+) mid n lc

parser = (,) <$> ((,) <$> get <*> get) <* string " -> " <*> get
