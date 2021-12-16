import sys
import fileinput
from collections import deque
from heapq import heappush, heappop


def solve(grid, scale):
    w = len(grid[0])
    h = len(grid)
    return lowest_risk_ucs(grid, w, h, scale, (0, 0))


def lowest_risk_ucs(grid, w, h, scale, src):
    w_s, h_s = w*scale, h*scale
    # starting risk is not counted, we set it to 0
    risks = {src: 0}
    q = [(0, src)]
    while q:
        risk, p = heappop(q)
        for n in neighbors(w_s, h_s, p):
            new_risk = risk + compute_risk(grid, w, h, scale, n)
            if n not in risks or new_risk < risks[n]:
                risks[n] = new_risk
                heappush(q, (new_risk, n))
    dst = (w_s - 1, h_s - 1)
    return risks[dst]


def neighbors(w_s, h_s, p):
    x, y = p
    increments = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cs = [(x + dx, y + dy) for (dx, dy) in increments]
    return [c for c in cs if 0 <= c[0] < w_s and 0 <= c[1] < h_s]


def compute_risk(grid, w, h, scale, p):
    x, y = p
    # assert (0 <= x < w*scale and 0 <= y < h*scale)
    bonus = x//w + y//h
    res = grid[y%h][x%w] + bonus
    return (res - 1)%9 + 1


def lowest_risk_first_try(grid, w, h, scale, start):
    w_s, h_s = w*scale, h*scale
    q = deque([start])
    risks = {start: 0}
    while q:
        p = q.popleft()
        for n in neighbors(w_s, h_s, p):
            risk = risks[p] + compute_risk(grid, w, h, scale, n)
            if (n not in risks) or risk < risks[n]:
                q.append(n)
                risks[n] = risk
    dest = (w_s - 1, h_s - 1)
    return risks[dest]


def lowest_risk_2(grid, w, h, scale, start):
    w_s, h_s = w*scale, h*scale
    dest = (w_s - 1, h_s - 1)
    risks = {}
    q = [(0, start)]
    while q:
        risk, p = heappop(q)
        risk += compute_risk(grid, w, h, scale, p)
        if p not in risks or risk < risks[p]:
            risks[p] = risk
            if p == dest:
                break
            for n in neighbors(w_s, h_s, p):
                heappush(q, (risks[p], n))
    return risks[dest] - risks[start]


if __name__ == '__main__' and not sys.flags.interactive:
    grid = [[int(c) for c in line.strip()] for line in fileinput.input()]
    print(solve(grid, 1))
    print(solve(grid, 5))
