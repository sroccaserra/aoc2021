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
    sn = [[1,2],[[3,4],5]]
    print(sn)
    print(create_map(sn))
    annotate_tree(sn)
    print(sn)
    return magnitude(sn)


def add(sn1, sn2):
    return annotate_tree([sn1, sn2])


def create_map(sn):
    ns = []
    stack = [(sn, 0)]
    while stack:
        node, d = stack.pop()
        if type(node) == list:
            stack.append((node[R], d+1))
            stack.append((node[L], d+1))
        else:
            ns.append(node)
    return ns


def annotate_tree(sn):
    i = 0
    def go(sn, depth, parent, side):
        nonlocal i
        if list == type(sn):
            go(sn[L], depth+1, sn, L)
            go(sn[R], depth+1, sn, R)
        else:
            parent[side] = {'id': i, 'depth': depth, 'value': sn, 'parent': parent, 'side': side}
            i += 1
    go(sn, 0, None, None)


def strip_tree(sn):
    def go(sn, parent, side):
        if list == type(sn):
            go(sn[L], sn, L)
            go(sn[R], sn, R)
        else:
            parent[side] = sn['value']
    go(sn, None, None)


def magnitude(tree):
    if list == type(tree):
        return 3*magnitude(tree[L]) + 2*magnitude(tree[R])
    else:
        if dict == type(tree):
            return tree['value']
        else:
            return tree


if __name__ == '__main__' and not sys.flags.interactive:
    # line = next(fileinput.input()).strip()
    # ns = [int(w) for w in line.split()]
    lines = [eval(line.strip()) for line in fileinput.input()]
    print(solve_1(lines))
