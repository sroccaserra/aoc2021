import sys
import fileinput


def solve(fuel_fn, ns):
    result = 10000000000
    for x in range(min(ns), max(ns)+1):
        s = sum([fuel_fn(x, n) for n in ns])
        if s < result:
            result = s
    return result


def distanceFuel(x, n):
    return abs(n-x)


def incrementingFuel(x, n):
    steps = abs(n-x)
    return (steps+1)*steps//2


if __name__ == '__main__' and not sys.flags.interactive:
    line = next(fileinput.input()).strip()
    ns = [int(w) for w in line.split(',')]
    print(solve(distanceFuel, ns))
    print(solve(incrementingFuel, ns))
