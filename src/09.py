import sys
import fileinput
from collections import defaultdict


def solve_1(matrix):
    grid = defaultdict(lambda:10)
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            grid[(x, y)] = matrix[y][x]
    s = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if is_low(grid, x, y):
                s += grid[(x, y)] + 1
    return s


def solve_2(matrix):
    return matrix


def is_low(grid, x, y):
    h = grid[(x, y)]
    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if grid[(x+dx, y+dy)] <= h:
            return False
    return True



if __name__ == '__main__' and not sys.flags.interactive:
    matrix = [[int(c) for c in line.strip()] for line in fileinput.input()]
    print(solve_1(matrix))
    # print(solve_2(lines))
