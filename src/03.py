import sys
import fileinput


def solve_1(lines):
    nb_columns = len(lines[0])
    gamma = ''
    epsilon = ''
    for j in range(nb_columns):
        if most_frequent(j, lines) == '1':
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return to_num(gamma)*to_num(epsilon)


def solve_2(lines):
    nb_columns = len(lines[0])
    o2 = lines.copy()
    co2 = lines.copy()
    for j in range(nb_columns):
        c_1 = most_frequent(j, o2)
        c_2 = most_frequent(j, co2)
        if len(o2) > 1:
            o2 = [s for s in o2 if s[j] == c_1]
        if len(co2) > 1:
            co2 = [s for s in co2 if not s[j] == c_2]
    return to_num(o2[0])*to_num(co2[0])


def most_frequent(j, lines):
    nb_lines = len(lines)
    ones = 0
    zeros = 0
    for i in range(nb_lines):
        if '1' == lines[i][j]:
            ones += 1
        else:
            zeros += 1
    result = []
    if ones >= zeros:
        return '1'
    else:
        return '0'


def to_num(s):
    return int(s, 2)


if __name__ == '__main__' and not sys.flags.interactive:
    lines = [line.strip() for line in fileinput.input()]
    print(solve_1(lines))
    print(solve_2(lines))
