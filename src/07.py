import sys
import fileinput


def solve_1(ns):
    result = 10000000000
    for n in range(min(ns), max(ns)+1):
        s = 0
        for i in ns:
            s += abs(i-n)
        if s < result:
            result = s
    return result


def solve_2(ns):
    result = 10000000000
    for n in range(min(ns), max(ns)+1):
        s = 0
        for i in ns:
            times = abs(i-n)
            s += (times+1)*times//2
        if s < result:
            result = s
    return result


if __name__ == '__main__' and not sys.flags.interactive:
    line = next(fileinput.input()).strip()
    ns = [int(w) for w in line.split(',')]
    print(solve_1(ns))
    print(solve_2(ns))
