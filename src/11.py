import sys
import fileinput


def solve_1(ns):
    s = 0
    for _ in range(100):
        s += step(ns)
    return s


def solve_2(ns):
    n = 0
    while not is_all_zero(ns):
        step(ns)
        n += 1
    return n


def step(ns):
    result = 0
    h = len(ns)
    w = len(ns[0])
    flashed = set()
    for y in range(h):
        for x in range(w):
            n = ns[y][x]
            ns[y][x] = n + 1
            if n == 9:
                flashed.add((x,y))
                result += 1
    while len(flashed) != 0:
        previously_flashed = flashed.copy()
        flashed = set()
        for p in previously_flashed:
            x, y = p
            neighbors = [
                    (x-1, y-1), (x, y-1), (x+1, y-1),
                    (x-1, y), (x+1, y),
                    (x-1, y+1), (x, y+1), (x+1, y+1)]
            for ne in neighbors:
                xn, yn = ne
                if 0 <= xn and xn < w and 0 <= yn and yn < h:
                    n = ns[yn][xn]
                    ns[yn][xn] = n + 1
                    if n == 9:
                        flashed.add(ne)
                        result += 1
    for y in range(h):
        for x in range(w):
            if ns[y][x] > 9:
                ns[y][x] = 0
    return result


def is_all_zero(ns):
    for row in ns:
        for n in row:
            if n > 0:
                return False
    return True


if __name__ == '__main__' and not sys.flags.interactive:
    ns = [[int(c) for c in line.strip()] for line in fileinput.input()]
    print(solve_1([r.copy() for r in ns.copy()]))
    print(solve_2([r.copy() for r in ns.copy()]))
