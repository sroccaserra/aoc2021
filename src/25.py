import sys
import fileinput


SIMPLE_EX = ['...>>>>>...']


def solve_1(floor):
    w = len(floor[0])
    h = len(floor)
    print(w, h)
    easts = set()
    souths = set()
    for y in range(h):
        for x in range(w):
            if floor[y][x] == '>':
                easts.add((x, y))
            if floor[y][x] == 'v':
                souths.add((x, y))
    i = 0
    display_cucumbers(w, h, easts, souths)
    while True:
        i = i + 1
        new_easts, new_souths = step(w, h, easts, souths)
        if new_easts == easts and new_souths == souths:
            return i
        easts = new_easts
        souths = new_souths
        print()
        display_cucumbers(w, h, easts, souths)
    return new_easts, new_souths


def display_cucumbers(w, h, easts, souths):
    for y in range(h):
        row = ''
        for x in range(w):
            if (x, y) in easts:
                row += '>'
            elif (x, y) in souths:
                row += 'v'
            else:
                row += '.'
        print(row)


def step(w, h, easts, souths):
    new_easts = set()
    new_souths = set()
    occupied = easts.union(souths)
    for e in easts:
        dest = east_of_the_sun(w, e)
        if dest in occupied:
            new_easts.add(e)
        else:
            new_easts.add(dest)
    occupied = new_easts.union(souths)
    for s in souths:
        dest = south_of_the_sun(h, s)
        if dest in occupied:
            new_souths.add(s)
        else:
            new_souths.add(dest)
    return new_easts, new_souths


def east_of_the_sun(w, p):
    (x, y) = p
    if x >= w - 1:
        return (0, y)
    return (x+1, y)

def south_of_the_sun(h, p):
    (x, y) = p
    if y >= h - 1:
        return (x, 0)
    return (x, y+1)


if __name__ == '__main__' and not sys.flags.interactive:
    floor = [line.strip() for line in fileinput.input()]
    print(solve_1(floor))
