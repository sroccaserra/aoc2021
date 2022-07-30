import sys
import fileinput


def solve_1(numbers):
    result = 0
    for i in range(len(numbers) - 1):
        if numbers[i+1] > numbers[i]:
            result += 1
    return result


def solve_2(numbers):
    HUGE = 9999999999
    p1, p2, p3 = HUGE, HUGE, HUGE
    result = 0
    for n in numbers:
        if n + p1 + p2 > p1 + p2 + p3:
            result += 1
        p1, p2, p3 = n, p1, p2
    return result


if __name__ == '__main__' and not sys.flags.interactive:
    numbers = [int(line.strip()) for line in fileinput.input()]
    print(solve_1(numbers))
    print(solve_2(numbers))
