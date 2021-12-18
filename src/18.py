import sys
import fileinput
from collections import deque

L = 0
R = 1

ID = 0
DEPTH = 1
VALUE = 2

def solve_1(lines):
    sn = [[1,2],3]
    sn = [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
    print(sn)
    print(create_map(sn))
    augment_tree(sn)
    return sn


def create_map(sn):
    ns = []
    stack = [(sn, 0)]
    while stack:
        node, d = stack.pop()
        if type(node) == list:
            stack.append((node[1], d+1))
            stack.append((node[0], d+1))
        else:
            ns.append(node)
    return ns


def augment_tree(sn):
    i = 0
    def augment_tree_rec(sn, depth, parent, side):
        nonlocal i
        if list == type(sn):
            augment_tree_rec(sn[0], depth+1, sn, L)
            augment_tree_rec(sn[1], depth+1, sn, R)
        else:
            parent[side] = (i, depth, sn)
            i += 1
    augment_tree_rec(sn, 0, None, None)


if __name__ == '__main__' and not sys.flags.interactive:
    # line = next(fileinput.input()).strip()
    # ns = [int(w) for w in line.split()]
    lines = [eval(line.strip()) for line in fileinput.input()]
    print(solve_1(lines))
