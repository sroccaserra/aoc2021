import sys
import fileinput
from collections import deque


def solve_1(lines):
    sn = [[1,2],3]
    sn = [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
    print(sn)
    print(create_map(sn))
    return create_tree_dfs(sn)


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

ID = [0]

def augment_tree(sn, t):
    if list == type(sn):
        augment_tree(sn[0], t)
        augment_tree(sn[1], t)
    else:
        pass



def create_tree_dfs(sn):
    stack = [(sn, 0, 'l')]
    i = 0
    root = []
    current = root
    left = None
    right = None
    levels = []
    while stack:
        node, d, side = stack.pop()
        if type(node) == list:
            levels.append(current)
            new = []
            current.append(new)
            current = new
            stack.append((node[1], d+1, 'r'))
            stack.append((node[0], d+1, 'l'))
        else:
            i = i+1
            current.append(node)
            if 'r' == side:
                current = levels.pop()

    return root[0]

class Tree:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.value is not None


if __name__ == '__main__' and not sys.flags.interactive:
    # line = next(fileinput.input()).strip()
    # ns = [int(w) for w in line.split()]
    lines = [eval(line.strip()) for line in fileinput.input()]
    print(solve_1(lines))
