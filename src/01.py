import sys
import fileinput

from collections import deque

def solve_1(lines):
    other_lines = lines.copy()
    n = 0
    for i in range(len(lines)-1):
        if other_lines[i+1] > lines[i]:
            n += 1
    return n

def solve_2(lines):
    ns_1 = deque(lines)
    ns_1.pop()
    ns_1.pop()
    ns_2 = deque(lines)
    ns_2.popleft()
    ns_2.pop()
    ns_3 = deque(lines)
    ns_3.popleft()
    ns_3.popleft()
    n = 0
    for i in range(len(ns_1)-1):
        s1 = ns_1[i]+ ns_2[i]+ ns_3[i]
        s2 = ns_1[i+1]+ ns_2[i+1]+ ns_3[i+1]
        if s2 > s1:
            n += 1
    return n

if __name__ == '__main__' and not sys.flags.interactive:
    lines = [int(line.strip()) for line in fileinput.input()]
    print(solve_1(lines))
    print(solve_2(lines))
