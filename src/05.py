import sys
import fileinput
from collections import defaultdict


def solve_1(pointPairs):
    grid = defaultdict(int)
    for pointPair in pointPairs:
        markLine(grid, pointPair)
    return len([k for k in grid if grid[k] > 1])


def solve_2(pointPairs):
    grid = defaultdict(int)
    for pointPair in pointPairs:
        markLine(grid, pointPair, True)
    return len([k for k in grid if grid[k] > 1])


def markLine(grid, pointPair, with_diagonals=False):
    (x1, y1), (x2, y2) = pointPair
    dx, dy = x2 - x1, y2 - y1
    if not with_diagonals and dx != 0 and dy != 0:
        return

    n = max(abs(dx), abs(dy))
    inc_x = (1 if dx > 0 else -1) if dx != 0 else 0
    inc_y = (1 if dy > 0 else -1) if dy != 0 else 0
    for i in range(0, n+1):
        p = (x1+i*inc_x, y1+i*inc_y)
        grid[p] += 1


if __name__ == '__main__' and not sys.flags.interactive:
    lines = [line.strip() for line in fileinput.input()]
    pairs = [line.split(' -> ') for line in lines]
    pointPairs = [[tuple([int(w) for w in s.split(',')]) for s in pair] for pair in pairs]
    print(solve_1(pointPairs))
    print(solve_2(pointPairs))
