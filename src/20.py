import sys
import fileinput
from collections import defaultdict
from itertools import chain


def solve(algo, grid, times):
    defaults = ['.', algo[0]]
    image = grid
    for i in range(times):
        image = enhance(algo, defaults[i%2], image)
    return sum(map(lambda c: c == '#', chain.from_iterable(image)))


def enhance(algo, default, grid):
    w = len(grid[0])
    h = len(grid)
    infinite = defaultdict(lambda:default)
    for y in range(h):
        for x in range(w):
            infinite[(x, y)] = grid[y][x]
    result = []
    d = 1
    for y in range(-d, h+d):
        row = ''
        for x in range(-d, w+d):
            i = index(infinite, x, y)
            row += algo[i]
        result.append(row)
    return result


def index(infinite, x, y):
    s = ''
    for dx, dy in [(-1, -1), (0, -1), (1, -1),(-1, 0), (0, 0), (1, 0),(-1, 1), (0, 1), (1, 1)]:
        p = (x+dx, y+dy)
        c = infinite[p]
        if c == '#':
            s += '1'
        else:
            s += '0'
    return int(s, 2)


if __name__ == '__main__' and not sys.flags.interactive:
    lines = [line.strip() for line in fileinput.input()]
    print(solve(lines[0], lines[2:], 2))
    print(solve(lines[0], lines[2:], 50))
