import sys
import fileinput
from collections import defaultdict, deque


OUT = -1
TIMES_BIGGER = 5


def solve_1(grid):
    x_max = max([p[0] for p in grid])
    y_max = max([p[1] for p in grid])
    return dijkstra(grid, (0,0))[(x_max, y_max)]


def solve_2(grid):
    w = 1 + max([p[0] for p in grid])
    h = 1 + max([p[1] for p in grid])
    corner = (w*TIMES_BIGGER-1,h*TIMES_BIGGER-1)
    return dijkstra_2(grid, (0,0))[corner]


def neighbors(grid, p):
    x, y = p
    cs = [(x+dx, y+dy) for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
    return [c for c in cs if grid[c] != OUT]


def dijkstra(grid, start):
    w = 1 + max([p[0] for p in grid])
    h = 1 + max([p[1] for p in grid])
    q = deque([start])
    risks = {start: 0}
    while len(q) > 0:
        p = q.popleft()
        for n in neighbors(grid, p):
            risk = risks[p] + grid[n]
            if (n not in risks) or risk < risks[n]:
                q.append(n)
                risks[n] = risk
    return risks


def neighbors_2(w, h, p):
    x, y = p
    cs = [(x+dx, y+dy) for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
    result = []
    for c in cs:
        x_n, y_n = c
        if 0 <= x_n and x_n < w*TIMES_BIGGER and 0 <= y_n and y_n < h*TIMES_BIGGER:
            result.append(c)
    return result


def dijkstra_2(grid, start):
    w = 1 + max([p[0] for p in grid])
    h = 1 + max([p[1] for p in grid])
    q = deque([start])
    risks = {start: 0}
    while len(q) > 0:
        p = q.popleft()
        for n in neighbors_2(w, h, p):
            risk = risks[p] + bigger_risk(grid, w, h, n)
            if (n not in risks) or risk < risks[n]:
                q.append(n)
                risks[n] = risk
    return risks


def bigger_risk(grid, w, h, p):
    x, y = p
    assert (0 <= x and x < w*TIMES_BIGGER and 0 <= y and y < h*TIMES_BIGGER)
    bonus = x//w+y//h
    res = (grid[(x%w, y%h)] + bonus)
    if res > 9:
        res = res - 9
    return res


if __name__ == '__main__' and not sys.flags.interactive:
    matrix = [[int(c) for c in line.strip()] for line in fileinput.input()]
    grid = defaultdict(lambda:OUT)
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            grid[(x, y)] = matrix[y][x]
    print(solve_1(grid.copy()))
    print(solve_2(grid.copy()))
