import sys
import fileinput


def solve(ns, days):
    sea = [0]*9
    for n in ns:
        sea[n] += 1
    for _ in range(days):
        sea = step(sea)
    return sum(sea)


def step(sea):
    result = [0]*9
    result[8] = sea[0]
    result[6] = sea[0]
    for i in range(8):
        result[i] += sea[i+1]
    return result


if __name__ == '__main__' and not sys.flags.interactive:
    line = next(fileinput.input()).strip()
    ns = [int(w) for w in line.split(',')]
    print(solve(ns, 80))
    print(solve(ns, 256))
