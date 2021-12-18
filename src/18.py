import sys
import fileinput
from collections import deque

L = 0
R = 1

ID = 0
DEPTH = 1
VALUE = 2

def solve_1(snail_numbers):
    # sn = [[1,2],3]
    # sn = [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
    # sn = [[1,2],[[3,4],5]]
    # sn = [[[[[9,8],1],2],3],4]
    # sn = [7,[6,[5,[4,[3,2]]]]]
    # sn = [[6,[5,[4,[3,2]]]],1]
    # sn = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
    # sn = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]

# [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]],
# [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]],
# [7,[5,[[3,8],[1,4]]]],
# [[2,[2,2]],[8,[8,1]]],
# [2,9],
# [1,[[[9,3],9],[[9,0],[0,7]]]],
# [[[5,[7,4]],7],1],
# [[[[4,2],2],6],[8,7]]
#  ]
    sn = snail_numbers[0]
    reduce(sn)
    for i in range(1, len(snail_numbers)):
        sn = add(sn, snail_numbers[i])
        reduce(sn)
        print(sn)
    return magnitude(sn)

def reduce(sn):
    while True:
        print('------------------')
        print(sn)
        annotate_tree(sn)
        op = find_operation(sn)
        print(op)
        apply_operation(sn, op)
        strip_tree(sn)
        print(sn)
        # input('pause...')
        if op is None:
            break


def apply_operation(sn, op):
    if op is None:
        return
    i = op['id']
    index_map = create_index_map(sn)
    node = index_map[i]
    if op['name'] == 'explode':
        parent = node['parent']
        left = parent[L]
        right_id = left['id']
        left_id = parent[L]['id']
        right = parent[R]
        right_id = right['id']
        if left_id > 0:
            index_map[left_id-1]['value'] += left['value']
            pass
        if right_id + 1 < len(index_map):
            index_map[right_id+1]['value'] += right['value']
            pass
        parent.pop()
        parent.pop()
    else:
        value = node['value']
        left = value//2
        right = left + (value % 2)
        node['parent'][node['side']] = [left, right]


def find_operation(sn):
    stack = [sn]
    while stack:
        node = stack.pop()
        if type(node) == list:
            stack.append(node[R])
            stack.append(node[L])
        else:
            if node['depth'] > 4:
                return {'name': 'explode', 'id': node['id']}
    stack = [sn]
    while stack:
        node = stack.pop()
        if type(node) == list:
            stack.append(node[R])
            stack.append(node[L])
        else:
            if node['value'] >= 10:
                return {'name': 'split', 'id': node['id']}


def add(sn1, sn2):
    return [sn1, sn2]


def create_index_map(sn):
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
            parent[side] = {'id': i, 'depth': depth, 'value': sn, 'parent': parent, 'side': side, 'todo': None}
            i += 1
    go(sn, 0, None, None)


def strip_tree(sn):
    def go(sn, parent, side):
        if list == type(sn):
            if sn:
                go(sn[L], sn, L)
                go(sn[R], sn, R)
            else:
                parent[side] = 0
        else:
            if dict == type(sn):
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
