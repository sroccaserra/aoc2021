import sys
import fileinput


def solve_1(data):
    result = 0
    wanted = set([2, 3, 4, 7])
    for i in range(len(data)):
        output = data[i][1].split()
        for digit in output:
            if len(digit) in wanted:
                result += 1
    return result


def solve_2(data):
    numbers = []
    for line in data:
        patterns = [set(s) for s in line[0].split()]
        output = [set(s) for s in line[1].split()]
        known_patterns = {n: known_pattern_for(patterns, n) for n in range(10) if known_pattern_for(patterns, n)}
        digits =  [digit_for(known_patterns, p) for p in output]
        numbers.append(1000*digits[0]+100*digits[1]+10*digits[2]+digits[3])
    return sum(numbers)


def known_pattern_for(patterns, n):
    if n == 1:
        for p in patterns:
            if len(p) == 2:
                return p
    if n == 4:
        for p in patterns:
            if len(p) == 4:
                return p
    if n == 7:
        for p in patterns:
            if len(p) == 3:
                return p
    if n == 8:
        for p in patterns:
            if len(p) == 7:
                return p


"""
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....


 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
"""
def digit_for(known_patterns, pattern):
    n = len(pattern)
    if n == 2:
        return 1
    if n == 3:
        return 7
    if n == 4:
        return 4
    if n == 7:
        return 8
    if n == 6:
        p_4 = known_patterns[4]
        if p_4.union(pattern) == pattern:
            return 9
        p_7 = known_patterns[7]
        if p_7.union(pattern) == pattern:
            return 0
        return 6
    if n == 5:
        p_7 = known_patterns[7]
        if p_7.union(pattern) == pattern:
            return 3
        p_4 = known_patterns[4]
        if 2 == len(p_4.intersection(pattern)):
            return 2
        return 5


if __name__ == '__main__' and not sys.flags.interactive:
    data = [line.strip().split(' | ') for line in fileinput.input()]
    print(solve_1(data))
    print(solve_2(data))
