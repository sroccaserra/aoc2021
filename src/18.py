import sys
import fileinput
from itertools import product
from copy import deepcopy


L = 0
R = 1


def solve_1(snail_numbers):
    sn = deepcopy(snail_numbers[0])
    reduce(sn)
    for i in range(1, len(snail_numbers)):
        next_sn = deepcopy(snail_numbers[i])
        sn = [sn, next_sn]
        reduce(sn)
    return magnitude(sn)


def solve_2(snail_numbers):
    res = 0
    for a, b in product(snail_numbers, repeat=2):
        s = [deepcopy(a), deepcopy(b)]
        reduce(s)
        mag = magnitude(s)
        if mag > res:
            res = mag
    return res


def reduce(sn):
    while True:
        annotate_tree(sn)
        op = find_operation(sn)
        apply_operation(sn, op)
        strip_tree(sn)
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
        if right_id + 1 < len(index_map):
            index_map[right_id+1]['value'] += right['value']
        parent.pop()
        parent.pop()
    else:
        value = node['value']
        left = value//2
        right = left + (value % 2)
        node['parent'][node['side']] = [left, right]


def find_operation(sn):
    explode = None
    split = None
    stack = [sn]
    while stack:
        node = stack.pop()
        if type(node) == list:
            stack.append(node[R])
            stack.append(node[L])
        else:
            if node['depth'] > 4:
                explode = {'name': 'explode', 'id': node['id']}
                break
            elif split is None and node['value'] >= 10:
                split = {'name': 'split', 'id': node['id']}
    return explode or split


def create_index_map(sn):
    result = []
    stack = [sn]
    while stack:
        node = stack.pop()
        if type(node) == list:
            stack.append(node[R])
            stack.append(node[L])
        else:
            result.append(node)
    return result


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
        return tree


if __name__ == '__main__' and not sys.flags.interactive:
    snail_numbers = [eval(line.strip()) for line in fileinput.input()]
    print(solve_1(snail_numbers))
    print(solve_2(snail_numbers))
