import sys
import fileinput
from collections import defaultdict


def solve(algo, grid, times):
    defaults = ['.', '#']
    image = grid
    for i in range(times):
        image = enhance(algo, defaults[i%2], image)
    n = 0
    for l in image:
        for c in l:
            if c == '#':
                n += 1
    return n


def enhance(algo, default, grid):
    w = len(grid[0])
    h = len(grid)
    floor = defaultdict(lambda:default)
    for y in range(h):
        for x in range(w):
            floor[(x, y)] = grid[y][x]

    result = []
    d = 2
    for y in range(-d, h+d):
        row = ''
        for x in range(-d, w+d):
            i = index(floor, x, y)
            row += algo[i]
        result.append(row)

    return result


def index(floor, x, y):
    s = ''
    for dx, dy in [(-1, -1), (0, -1), (1, -1),(-1, 0), (0, 0), (1, 0),(-1, 1), (0, 1), (1, 1)]:
        p = (x+dx, y+dy)
        c = floor[p]
        if c == '#':
            s += '1'
        else:
            s += '0'
    return int(s, 2)


if __name__ == '__main__' and not sys.flags.interactive:
    lines = [line.strip() for line in fileinput.input()]
    print(solve(lines[0], lines[2:], 2))
    print(solve(lines[0], lines[2:], 50))
