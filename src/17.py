import sys
import fileinput
import re


EX = 'target area: x=20..30, y=-10..-5'

NEAR = -1
HIT = 0
FAR = 1


def solve_1(target):
    max_y = 0
    for v_y in range(1,100):
        shot, new_max_y = shoot_y(target, v_y)
        if HIT == shot:
            max_y = new_max_y
    return max_y


def solve_2(target):
    n = 0
    for v_y in range(-100, 100):
        for v_x in range(1, 500):
            shot = shoot(target, v_x, v_y)
            if HIT == shot:
                n += 1
    return n


def shoot_y(target, v_y):
    _, _, y_min, y_max = target
    y = 0
    max_y = 0

    while y_max < y:
        y += v_y
        if y > max_y:
            max_y = y
        v_y = v_y - 1

    if y_min <= y:
        result_y = HIT
    else:
        result_y = FAR

    return result_y, max_y


def shoot(target, v_x, v_y):
    x_min, x_max, y_min, y_max = target
    x, y = 0, 0

    while x < x_max and y_min < y:
        x += v_x
        y += v_y
        v_x = max(0, v_x - 1)
        v_y = v_y - 1
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return HIT

    if v_x == 0:
        return NEAR

    return FAR


if __name__ == '__main__' and not sys.flags.interactive:
    line = next(fileinput.input()).strip()
    # line = EX
    r = r'x=([-0-9]*)\.\.([-0-9]*), y=([-0-9]*)\.\.([-0-9]*)'
    ws = re.search(r, line).groups()
    ns = [int(w) for w in ws]
    print(solve_1(ns))
    print(solve_2(ns))
