import sys
import fileinput

from collections import deque

def solve_1(numbers):
    other_lines = numbers.copy()
    n = 0
    for i in range(len(numbers)-1):
        if other_lines[i+1] > numbers[i]:
            n += 1
    return n

def solve_2(numbers):
    ns_1 = deque(numbers)
    ns_1.pop()
    ns_1.pop()
    ns_2 = deque(numbers)
    ns_2.popleft()
    ns_2.pop()
    ns_3 = deque(numbers)
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
    numbers = [int(line.strip()) for line in fileinput.input()]
    print(solve_1(numbers))
    print(solve_2(numbers))
