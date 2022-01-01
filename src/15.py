import sys
import fileinput
from collections import deque
from heapq import heappush, heappop, heapify
from priority_queue import PriorityQueue


def solve(grid, scale):
    w = len(grid[0])
    h = len(grid)
    return lowest_risk_ucs(grid, w, h, scale)


# Note: see file history for other versions
def lowest_risk_ucs(grid, w, h, scale):
    w_s, h_s = w*scale, h*scale
    src = (0, 0)
    dst = (w_s - 1, h_s - 1)
    frontier = PriorityQueue([(src, 0)])
    while True:
        state, past_cost = frontier.removeMin()
        if state == dst:
            return past_cost
        for n in neighbors(w_s, h_s, state):
            cost = compute_risk(grid, w, h, n)
            frontier.update(n, past_cost + cost)


def lowest_risk_ucs_aima(grid, w, h, scale, src):
    """
    See: https://github.com/aimacode/aima-python/blob/master/search.py
    """
    w_s, h_s = w*scale, h*scale
    dst = (w_s - 1, h_s - 1)
    node = (0, src)
    frontier = []
    heappush(frontier, node)
    explored = set()
    while frontier:
        cost, p = heappop(frontier)
        if p == dst:
            return cost
        explored.add(p)
        for n in neighbors(w_s, h_s, p):
            n_cost = cost + compute_risk(grid, w, h, n)
            if n not in explored and not contains(frontier, n):
                heappush(frontier, (n_cost, n))
            elif contains(frontier, n):
                if n_cost < getvalue(frontier, n):
                    delitem(frontier, n)
                    heappush(frontier, (n_cost, n))
    return None


def contains(q, key):
    return any([item == key for _, item in q])


def getvalue(q, key):
    for value, item in q:
        if item == key:
            return value
    raise KeyError(str(key) + ' is not in the priority queue')


def delitem(q, key):
    try:
        del q[[item == key for _, item in q].index(True)]
    except ValueError:
        raise KeyError(str(key) + ' is not in the priority queue')
    heapify(q)


def neighbors(w_s, h_s, p):
    x, y = p
    increments = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cs = [(x + dx, y + dy) for (dx, dy) in increments]
    return [c for c in cs if 0 <= c[0] < w_s and 0 <= c[1] < h_s]


def compute_risk(grid, w, h, p):
    x, y = p
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
            risk = risks[p] + compute_risk(grid, w, h, n)
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
        risk += compute_risk(grid, w, h, p)
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
