import sys
import fileinput
from collections import defaultdict


def solve(coords, instructions):
    d, n = instructions[0]
    if d == 'x':
        coords = fold_x(coords, n)
    else:
        coords = fold_y(coords, n)
    show(coords)
    for d, n in instructions[1:]:
        if d == 'x':
            coords = fold_x(coords, n)
        else:
            coords = fold_y(coords, n)
    show(coords)


def fold_y(coords, y_f):
    result = []
    for x, y in coords:
        if y < y_f:
            result.append((x, y))
        else:
            result.append([x, 2*y_f-y])
    return result


def fold_x(coords, x_f):
    result = []
    for x, y in coords:
        if x < x_f:
            result.append((x, y))
        else:
            result.append([2*x_f-x, y])
    return result


def show(coords):
    cs = defaultdict(lambda:'.')
    for x, y in coords:
        cs[(x, y)] = '#'

    xs = [coord[0] for coord in coords]
    ys = [coord[1] for coord in coords]

    result = 0
    for y in range(min(ys), max(ys)+1):
        print()
        for x in range(min(xs), max(xs)+1):
            c = cs[(x, y)]
            if c == '#':
                result += 1
            print(c, end='')
    print(f'\n{result}')


if __name__ == '__main__' and not sys.flags.interactive:
    lines = [line.strip() for line in fileinput.input()]
    coords = [[int(w) for w in line.split(',')] for line in lines if line and line[0] in "0123456789"]
    instructions = [(line[11], int(line[13:])) for line in lines if line and line[0] == 'f']
    solve(coords, instructions)
