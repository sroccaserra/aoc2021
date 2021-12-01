import sys
import fileinput


def solve_1(lines):
    return lines


def solve_2(lines):
    return lines


if __name__ == '__main__' and not sys.flags.interactive:
    # line = next(fileinput.input()).strip()
    # ns = [int(w) for w in line.split()]
    lines = [line.strip() for line in fileinput.input()]
    print(solve_1(lines))
    # print(solve_2(lines))
