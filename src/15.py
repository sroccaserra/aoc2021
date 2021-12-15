import sys
import fileinput
from collections import deque


def solve(grid, scale):
    w = len(grid[0])
    h = len(grid)
    corner = (w*scale - 1,h*scale - 1)
    return lowest_risks(grid, w, h, scale, (0,0))[corner]


def neighbors(w_s, h_s, p):
    x, y = p
    increments = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cs = [(x + dx, y + dy) for (dx, dy) in increments]
    return [c for c in cs if 0 <= c[0] < w_s and 0 <= c[1] < h_s]


def lowest_risks(grid, w, h, scale, start):
    q = deque([start])
    result = {start: 0}
    w_s, h_s = w*scale, h*scale
    while q:
        p = q.popleft()
        for n in neighbors(w_s, h_s, p):
            risk = result[p] + compute_risk(grid, w, h, scale, n)
            if (n not in result) or risk < result[n]:
                q.append(n)
                result[n] = risk
    return result


def compute_risk(grid, w, h, scale, p):
    x, y = p
    # assert (0 <= x < w*scale and 0 <= y < h*scale)
    bonus = x//w + y//h
    res = grid[y%h][x%w] + bonus
    return (res - 1)%9 + 1


if __name__ == '__main__' and not sys.flags.interactive:
    grid = [[int(c) for c in line.strip()] for line in fileinput.input()]
    print(solve(grid, 1))
    print(solve(grid, 5))
