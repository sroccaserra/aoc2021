import sys
import fileinput


"""
 .
. |
 .
. |
 .

 .
| |
 -
. |
 .

 -
. |
 .
. |
 .
"""

def solve_1(data):
    result = 0
    wanted = set([2, 3, 4, 7])
    for i in range(len(data)):
        output = data[i][1]
        digits = output.split(' ')
        for digit in digits:
            if len(digit) in wanted:
                result += 1

    return result


def solve_2(data):
    return data


if __name__ == '__main__' and not sys.flags.interactive:
    data = [line.strip().split(' | ') for line in fileinput.input()]
    print(solve_1(data))
    # print(solve_2(data))
