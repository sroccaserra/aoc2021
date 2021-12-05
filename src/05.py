import sys
import fileinput
from collections import Counter


def solve_1(pointPairs):
    return solve_2(filter(isHorizOrVert, pointPairs))


def solve_2(pointPairs):
    c = Counter()
    for pointPair in pointPairs:
        c.update(pointsBetween(pointPair))
    return sum(1 for k in c if c[k] > 1)


def isHorizOrVert(pointPair):
    (x1, y1), (x2, y2) = pointPair
    return x1 == x2 or y1 == y2


def pointsBetween(pointPair):
    (x1, y1), (x2, y2) = pointPair
    dx, dy = x2 - x1, y2 - y1
    n = max(abs(dx), abs(dy))
    inc_x = (1 if dx > 0 else -1) if dx != 0 else 0
    inc_y = (1 if dy > 0 else -1) if dy != 0 else 0
    return [(x1 + i*inc_x, y1 + i*inc_y) for i in range(n+1)]


if __name__ == '__main__' and not sys.flags.interactive:
    lines = [line.strip() for line in fileinput.input()]
    pairs = [line.split(' -> ') for line in lines]
    pointPairs = [[tuple([int(w) for w in s.split(',')]) for s in pair] for pair in pairs]
    print(solve_1(pointPairs))
    print(solve_2(pointPairs))
