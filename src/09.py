import sys
import fileinput
from collections import defaultdict
from queue import Queue


OUT = 10
WALL = 9


def solve_1(matrix):
    grid, lows = grid_and_low_points(matrix)
    s = 0
    for p in lows:
        s += grid[p] + 1
    return s


def solve_2(matrix):
    grid, lows = grid_and_low_points(matrix)
    a, b, c = sorted([basin_size(grid, p) for p in lows])[-3:]
    return a*b*c


def grid_and_low_points(matrix):
    lows = []
    grid = defaultdict(lambda:OUT)
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            grid[(x, y)] = matrix[y][x]
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if is_low(grid, x, y):
                lows.append((x, y))
    return grid, lows


def is_low(grid, x, y):
    h = grid[(x, y)]
    for n in neighbours(x, y):
        if grid[n] <= h:
            return False
    return True


def neighbours(x, y):
    return [(x+dx, y+dy) for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]]


def basin_size(grid, low):
    result = 0
    known = set()
    q = Queue()

    def count(p):
        nonlocal result, q, known
        result += 1
        q.put(p)
        known.add(p)

    count(low)
    while not q.empty():
        x, y = q.get()
        for n in flowing_neighbours(grid, x, y):
            if n not in known:
                count(n)

    return result


def flowing_neighbours(grid, x, y):
    h = grid[(x, y)]
    result = []
    for n in neighbours(x, y):
        hn = grid[n]
        if hn > h and hn not in [WALL, OUT]:
            result.append(n)
    return result


if __name__ == '__main__' and not sys.flags.interactive:
    matrix = [[int(c) for c in line.strip()] for line in fileinput.input()]
    print(solve_1(matrix))
    print(solve_2(matrix))
