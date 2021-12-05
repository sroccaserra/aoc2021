import sys
import fileinput
from collections import defaultdict


def solve_1(coordsPairs):
    grid = defaultdict(int)
    for coords in coordsPairs:
        markLine(grid, coords)
    return len([k for k in grid if grid[k] > 1])


def solve_2(coordsPairs):
    grid = defaultdict(int)
    for coords in coordsPairs:
        markLine(grid, coords, True)
    return len([k for k in grid if grid[k] > 1])


def markLine(grid, coords, with_diagonals=False):
    start, end = coords
    dx, dy = end[0] - start[0], end[1] - start[1]
    if not with_diagonals and dx != 0 and dy != 0:
        return

    n = max(abs(dx), abs(dy))
    inc_x = (1 if dx > 0 else -1) if dx != 0 else 0
    inc_y = (1 if dy > 0 else -1) if dy != 0 else 0
    for i in range(0, n+1):
        p = (start[0]+i*inc_x, start[1]+i*inc_y)
        grid[p] += 1


if __name__ == '__main__' and not sys.flags.interactive:
    lines = [line.strip() for line in fileinput.input()]
    pairs = [line.split(' -> ') for line in lines]
    coordsPairs = [[tuple([int(w) for w in s.split(',')]) for s in pair] for pair in pairs]
    print(solve_1(coordsPairs))
    print(solve_2(coordsPairs))
