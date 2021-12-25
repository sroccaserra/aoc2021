import sys
import fileinput
from types import SimpleNamespace
from collections import namedtuple, deque
from random import randint

State = namedtuple('State', ['w', 'x', 'y', 'z'])

REG_INDEX_FOR = {'w': 0, 'x': 1, 'y': 2, 'z': 3}


def solve_1(program):
    test_inputs = [
            deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]),
            deque([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
            deque([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),
            deque([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]),
            deque([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]),
            deque([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),
            deque([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]),
            deque([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]),
            deque([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]),
            deque([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]),
            deque([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]),
            deque([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]),
            deque([12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]),
            deque([13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]),
            deque([14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]),
            deque([14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
            deque([1, 12, 2, 11, 11, 8, 3, 10, 7, 2, 14, 12, 3, 8]),
            deque([11, 5, 7, 12, 11, 8, 9, 5, 10, 1, 9, 1, 1, 8]),
            deque([14, 2, 5, 7, 9, 10, 8, 10, 11, 4, 3, 9, 3, 9]),
            deque([1, 9, 6, 7, 9, 8, 4, 6, 4, 14, 14, 5, 3, 12]),
            deque([6, 9, 12, 5, 14, 13, 6, 12, 4, 2, 13, 8, 1, 11]),
            deque([9, 8, 7, 5, 4, 8, 3, 1, 1, 1, 7, 3, 5, 8]),
            deque([9, 7, 5, 2, 8, 9, 8, 1, 6, 3, 9, 7, 3, 5]),
            deque([4, 7, 8, 1, 2, 3, 2, 9, 9, 6, 7, 3, 4, 6]),
            deque([2, 8, 8, 6, 9, 3, 7, 8, 5, 2, 7, 3, 2, 3]),
            deque([9, 8, 6, 4, 1, 9, 9, 6, 3, 5, 5, 6, 2, 7]),
            deque([7, 5, 2, 4, 9, 9, 4, 3, 2, 8, 5, 4, 3, 6]),
            deque([5, 6, 8, 8, 7, 9, 1, 9, 9, 2, 9, 2, 4, 2]),
            deque([2, 7, 9, 9, 6, 3, 2, 7, 4, 5, 8, 2, 3, 5]),
            deque([7, 3, 5, 6, 5, 3, 9, 9, 9, 2, 2, 6, 8, 3]),
            deque([9, 1, 4, 1, 4, 6, 8, 9, 3, 9, 4, 7, 6, 3]),
            deque([6, 7, 6, 3, 3, 5, 5, 1, 3, 5, 3, 9, 1, 6]),
            deque([4, 2, 9, 5, 4, 1, 1, 2, 9, 5, 1, 1, 4, 3]),
            deque([1, 5, 5, 6, 1, 8, 4, 6, 3, 1, 8, 8, 4, 6]),
            deque([7, 4, 5, 5, 1, 6, 2, 6, 3, 1, 7, 1, 2, 5]),
            deque([6, 8, 3, 9, 3, 9, 2, 5, 8, 9, 1, 5, 7, 8]),
            deque([8, 7, 3, 6, 6, 1, 2, 2, 8, 9, 7, 4, 2, 8]),
            deque([1, 1, 7, 6, 9, 7, 4, 7, 5, 6, 9, 4, 5, 8]),
            deque([7, 5, 5, 8, 7, 1, 2, 4, 6, 2, 1, 8, 2, 6]),
            deque([8, 5, 9, 6, 2, 8, 2, 1, 8, 8, 4, 8, 3, 8]),
            deque([6, 5, 1, 9, 9, 4, 5, 6, 2, 6, 7, 6, 6, 8]),
            deque([7, 6, 2, 7, 4, 4, 2, 5, 1, 2, 6, 2, 1, 1]),
            deque([6, 5, 6, 8, 3, 4, 4, 1, 9, 2, 5, 2, 8, 7]),
            deque([5, 9, 3, 5, 5, 9, 6, 9, 2, 2, 1, 4, 9, 2]),
            deque([2, 7, 7, 4, 9, 2, 5, 1, 8, 2, 2, 9, 2, 1]),
            deque([8, 5, 4, 5, 5, 9, 4, 6, 8, 2, 1, 1, 5, 8]),
            deque([5, 3, 6, 2, 9, 6, 4, 2, 7, 8, 8, 2, 4, 5]),
            deque([7, 1, 5, 5, 1, 8, 6, 8, 4, 3, 2, 2, 4, 5]),
            deque([4, 3, 2, 4, 6, 1, 1, 5, 9, 4, 5, 8, 6, 4]),
            deque([5, 6, 6, 3, 5, 9, 7, 7, 6, 5, 1, 5, 9, 8]),
            deque([7, 2, 5, 6, 9, 3, 6, 9, 7, 4, 3, 4, 3, 2]),
            deque([4, 5, 9, 2, 5, 3, 6, 8, 1, 6, 2, 6, 7, 8]),
            deque([3, 5, 2, 3, 9, 7, 3, 8, 7, 2, 2, 9, 2, 6]),
            deque([6, 8, 1, 8, 3, 7, 2, 8, 6, 4, 9, 3, 5, 2]),
            deque([2, 5, 5, 9, 3, 9, 9, 9, 3, 7, 6, 2, 5, 7]),
            deque([3, 1, 9, 7, 3, 3, 6, 6, 6, 2, 6, 3, 6, 2]),
            deque([2, 7, 4, 2, 3, 5, 6, 1, 5, 3, 7, 6, 5, 4]),
            deque([9, 5, 1, 4, 1, 7, 1, 1, 9, 2, 4, 3, 1, 4]),
            deque([2, 3, 9, 7, 9, 2, 8, 4, 6, 5, 9, 2, 2, 8]),
            deque([2, 2, 3, 8, 2, 1, 7, 4, 5, 2, 2, 7, 6, 6]),
            deque([6, 9, 4, 4, 5, 4, 8, 9, 1, 7, 3, 4, 6, 6]),
            deque([8, 9, 5, 6, 1, 5, 3, 4, 3, 2, 6, 5, 3, 4]),
            deque([3, 7, 2, 1, 6, 1, 3, 4, 8, 2, 6, 8, 6, 3]),
            deque([4, 2, 6, 5, 6, 7, 1, 4, 5, 4, 9, 5, 5, 4]),
            deque([7, 3, 8, 1, 6, 5, 9, 6, 3, 7, 9, 3, 6, 3]),
            deque([6, 6, 8, 4, 6, 8, 6, 4, 9, 8, 4, 9, 6, 3]),
            deque([7, 5, 1, 9, 4, 5, 7, 4, 6, 9, 4, 5, 9, 6]),
            deque([3, 8, 4, 2, 6, 4, 4, 4, 3, 6, 8, 1, 9, 9]),
            deque([9, 3, 1, 5, 5, 1, 1, 4, 3, 9, 3, 5, 2, 8]),
            deque([6, 7, 5, 2, 4, 3, 1, 5, 6, 2, 7, 3, 3, 5]),
            deque([4, 4, 8, 4, 2, 3, 2, 8, 2, 5, 8, 1, 4, 7]),
            deque([5, 1, 3, 4, 7, 6, 4, 6, 4, 5, 8, 3, 4, 1]),
            deque([9, 5, 7, 7, 7, 9, 4, 1, 2, 3, 7, 5, 4, 7]),
            deque([7, 3, 5, 1, 2, 4, 4, 3, 3, 5, 7, 8, 4, 7]),
            deque([8, 9, 8, 9, 1, 8, 5, 2, 6, 3, 8, 1, 8, 2]),
            deque([1, 3, 5, 7, 9, 2, 4, 6, 8, 9, 9, 9, 9, 9]),
            deque([9, 9, 9, 9, 9, 8, 6, 4, 2, 9, 7, 5, 3, 1]),

            deque([1, 4, 4, 1, 9, 5, 4, 2, 2, 9, 3, 5, 9, 9]),
            deque([1, 2, 6, 1, 9, 3, 7, 2, 8, 5, 6, 5, 9, 4]),
            deque([1, 2, 1, 3, 1, 2, 7, 5, 1, 8, 2, 2, 8, 5]),
            deque([1, 1, 8, 4, 2, 5, 4, 2, 2, 9, 6, 5, 9, 6]),
            deque([1, 1, 2, 4, 6, 6, 7, 8, 1, 8, 9, 2, 6, 1]),
            deque([9, 3, 7, 4, 5, 8, 6, 4, 1, 8, 8, 4, 8, 5]), # 427
            deque([8, 3, 5, 1, 9, 1, 8, 1, 2, 9, 2, 6, 9, 6]), # 401
            deque([8, 9, 9, 8, 7, 3, 6, 4, 2, 9, 3, 6, 5, 4]), # 399
            deque([7, 3, 9, 1, 9, 4, 8, 6, 9, 3, 1, 9, 5, 4]), # 379
            deque([6, 1, 8, 4, 4, 9, 5, 3, 2, 9, 9, 3, 4, 3]), # 346
            deque([6, 7, 9, 5, 5, 8, 4, 2, 2, 9, 8, 4, 5, 1]), # 344
            deque([5, 3, 9, 1, 3, 3, 3, 1, 2, 9, 3, 2, 5, 2]), # 319
            deque([4, 2, 6, 3, 5, 4, 7, 5, 1, 8, 4, 4, 2, 6]), # 297
            deque([4, 8, 5, 1, 3, 9, 5, 3, 1, 8, 9, 2, 1, 1]), # 292
            deque([3, 9, 9, 2, 9, 3, 4, 2, 1, 8, 3, 8, 4, 1]), # 277
            deque([3, 2, 3, 1, 9, 6, 5, 3, 1, 8, 9, 8, 5, 2]), # 270
            deque([3, 7, 6, 7, 3, 3, 5, 3, 2, 9, 3, 2, 2, 1]), # 266
            deque([2, 9, 8, 9, 2, 9, 3, 1, 2, 9, 9, 1, 8, 5]), # 251
            deque([2, 6, 5, 7, 9, 7, 4, 2, 2, 9, 7, 8, 1, 6]), # 245
            deque([2, 3, 6, 9, 3, 8, 8, 6, 2, 9, 8, 2, 7, 4]), # 245
            deque([2, 2, 7, 4, 5, 8, 9, 7, 1, 8, 8, 4, 3, 3]), # 242
            deque([2, 8, 9, 9, 6, 6, 8, 6, 1, 8, 6, 5, 5, 2]), # 241
            deque([1, 8, 8, 8, 8, 9, 6, 4, 1, 8, 9, 7, 7, 4]), # 224
            deque([1, 7, 9, 1, 9, 6, 9, 7, 2, 9, 9, 8, 7, 4]), # 223
            deque([1, 7, 3, 4, 4, 6, 7, 5, 1, 8, 6, 3, 7, 4]), # 223
            deque([1, 7, 6, 1, 9, 9, 4, 2, 1, 8, 9, 4, 8, 6]), # 219
            deque([1, 2, 2, 1, 9, 3, 7, 5, 6, 9, 7, 8, 6, 3]), # 218
            deque([1, 7, 6, 1, 7, 9, 6, 4, 1, 8, 9, 6, 2, 3]), # 216
            deque([1, 4, 6, 1, 9, 6, 7, 5, 1, 8, 2, 1, 2, 2]), # 215
            deque([1, 2, 8, 9, 3, 4, 3, 1, 2, 9, 4, 2, 4, 1]), # 214
            deque([9, 9, 9, 5, 9, 4, 4, 2, 2, 9, 4, 8, 5, 6]), # 16
            deque([9, 7, 9, 1, 9, 3, 3, 1, 5, 9, 7, 8, 5, 4]), # 16
            deque([9, 9, 8, 1, 9, 7, 8, 6, 1, 8, 5, 4, 4, 6]), # 16
            deque([9, 7, 8, 1, 7, 4, 9, 7, 2, 9, 4, 6, 4, 4]), # 16
            deque([9, 6, 7, 5, 2, 8, 6, 4, 2, 9, 8, 1, 3, 3]), # 16
            deque([8, 4, 7, 1, 9, 8, 6, 4, 1, 8, 4, 3, 3, 1]), # 15
            deque([8, 6, 7, 7, 8, 2, 4, 2, 2, 9, 2, 7, 3, 3]), # 15
            deque([7, 1, 6, 1, 9, 9, 9, 7, 1, 8, 9, 1, 9, 6]), # 14
            deque([7, 6, 6, 8, 2, 5, 8, 6, 1, 8, 5, 1, 2, 3]), # 14
            deque([6, 4, 7, 1, 9, 4, 3, 1, 2, 7, 5, 9, 3, 1]), # 13
            deque([6, 5, 5, 1, 9, 2, 7, 5, 7, 3, 1, 7, 1, 2]), # 13
            deque([6, 8, 9, 1, 6, 9, 9, 7, 1, 8, 9, 5, 5, 5]), # 13
            deque([5, 9, 5, 3, 6, 2, 5, 3, 2, 9, 2, 5, 1, 6]), # 12
            deque([4, 8, 9, 1, 9, 2, 7, 5, 7, 8, 6, 7, 5, 5]), # 11
            deque([4, 4, 5, 4, 5, 3, 8, 6, 2, 9, 3, 4, 1, 1]), # 11
            deque([3, 5, 5, 1, 9, 4, 9, 7, 3, 8, 6, 9, 1, 2]), # 10
            deque([3, 9, 7, 1, 9, 6, 4, 2, 1, 8, 9, 8, 3, 6]), # 10
            deque([3, 7, 6, 1, 9, 4, 6, 4, 9, 9, 7, 9, 2, 4]), # 10
            deque([2, 9, 6, 6, 9, 4, 3, 1, 2, 9, 4, 8, 2, 6]), # 9
            deque([2, 9, 6, 6, 9, 4, 3, 1, 2, 9, 4, 8, 2, 6]), # 9
            deque([2, 7, 9, 1, 9, 7, 7, 5, 1, 8, 7, 4, 5, 2]), # 9
            deque([2, 7, 9, 1, 9, 2, 2, 6, 2, 9, 7, 7, 5, 4]), # 9
            deque([2, 7, 9, 1, 8, 3, 6, 4, 2, 9, 3, 7, 5, 4]), # 9
            deque([2, 5, 5, 1, 9, 4, 5, 6, 1, 8, 7, 9, 1, 2]), # 9
            deque([2, 4, 8, 4, 6, 8, 6, 4, 1, 8, 8, 5, 4, 1]), # 9
            deque([5, 3, 9, 1, 9, 3, 7, 5, 2, 9, 3, 4, 5, 4]), # 9
            deque([1, 4, 6, 1, 9, 4, 7, 5, 2, 9, 8, 7, 2, 1]), # 8
            deque([1, 9, 9, 4, 7, 4, 5, 3, 1, 8, 4, 6, 5, 6]), # 8
            deque([4, 7, 8, 1, 9, 9, 3, 1, 2, 9, 9, 3, 9, 2]), # 7
            deque([3, 3, 8, 1, 9, 1, 9, 7, 2, 9, 1, 3, 5, 1]), # 6
            deque([5, 9, 5, 3, 6, 2, 5, 3, 2, 9, 2, 5, 1, 6]), # 6
            deque([1, 6, 9, 1, 9, 7, 9, 7, 2, 9, 7, 4, 8, 1]), # 6
            deque([3, 2, 6, 1, 9, 1, 3, 1, 2, 9, 1, 1, 4, 1]), # 6
            deque([9, 7, 9, 1, 9, 1, 3, 1, 1, 8, 1, 4, 9, 5]), # 0 !
            deque([9, 7, 9, 1, 9, 1, 7, 5, 2, 9, 1, 4, 9, 5]), # 0 <-- zero!
            deque([9, 7, 9, 1, 9, 1, 9, 7, 2, 9, 1, 4, 9, 5]),
            ]
    # for inps in test_inputs:
    #     test(program, inps)
    # search_big(program)
    # search_random_for_max(program)
    search_random_for_min(program)
    test(program, deque([1, 1, 1, 1, 9, 1, 3, 1, 1, 8, 1, 4, 9, 5])) # 0 <-- zero!
    # Nombres forcés:                ^        ^     ^  ^  ^  ^  ^
    #                    0  1  2  3  4  5  6  7  8  9  0  1  2  3

# 91619131181135 (too high
# 54619153291161
# 51619153181131
# 51619131181131 <-- Ok.

def search_random_for_min(program):
    min_res = 999999999999999999999999999999999999
    min_res_inp = 0
    # for _ in range(100000):
    while True:
        rands = []
        for _ in range(14):
            rands.append(randint(1, 9))
        # rands[0] = randint(1, 5)
        rands[0] = 5
        rands[1] = 1
        # rands[2] = randint(1, 6)
        rands[2] = 6
        rands[3] = 1
        rands[4] = 9
        rands[5] = 1
        #rands[6] = 3
        # rands[7] = 1
        # rands[8] = 1
        # rands[9] = 8
        rands[9] = randint(8,9)
        rands[8] = 2 if rands[9] == 9 else 1
        # rands[11] = 1
        # rands[12] = 3
        # rands[13] = 5
        inps = deque(rands)
        state = apply_program(program, inps)
        if state[3] == 0 or state[3] <= min_res:
            min_res = state[3]
            min_res_inp = rands
            print(min_res_inp, min_res, '<------ min')

def search_random_for_max(program):
    min_res = 999999999999999999999999999999999999
    min_res_inp = 0
    # for _ in range(100000):
    while True:
        rands = []
        for _ in range(14):
            rands.append(randint(1, 9))
        # rands[3] = 1
        # rands[4] = 9
        # rands[9] = 9
        rands[0] = 9
        rands[1] = randint(7, 9)
        rands[2] = 9
        rands[3] = 1
        rands[4] = 9
        # rands[5] = 9
        rands[6] = 9
        rands[7] = 7
        rands[8] = 2
        rands[9] = 9
        # rands[9] = randint(8,9)
        # rands[8] = 2 if rands[9] == 9 else 1
        inps = deque(rands)
        state = apply_program(program, inps)
        if state[3] == 0:
            print(rands, '<---------- ZERO!!!')
            # break
        if state[3] < min_res:
            min_res = state[3]
            min_res_inp = rands
            print(min_res_inp, min_res, '<------ min')

def test(program, inps):
    state = apply_program(program, inps.copy())
    ref = state[3]
    result = apply_reved_program(ref, inps)
    assert ref == result, (ref, result)
    print(ref, result)

def apply_program(program, inps):
    state = [0, 0, 0, 0]
    pc = 0
    n = 0
    for pc in range(len(program)):
        instruction = program[pc]
        if instruction[0] == 'inp':
            n = 0
        # print(n, pc, instruction, state)
        n = n + 1
        apply_instruction(state, inps, instruction)
    return state

def apply_instruction(state, inps, instruction):
    op = instruction[0]
    a_index = REG_INDEX_FOR[instruction[1]]
    if op == 'inp':
        value = inps.popleft()
        state[a_index] = value
    elif op == 'add':
        add(state, a_index, instruction[2])
    elif op == 'mul':
        mul(state, a_index, instruction[2])
    elif op == 'div':
        div(state, a_index, instruction[2])
    elif op == 'mod':
        mod(state, a_index, instruction[2])
    elif op == 'eql':
        eql(state, a_index, instruction[2])
    else:
        assert False, instruction

def is_address(v):
    return v in ['w', 'x', 'y', 'z']


def add(state, a_index, b):
    if is_address(b):
        reg = REG_INDEX_FOR[b]
        rhs = state[reg]
    else:
        rhs = int(b)
    state[a_index] = state[a_index]+rhs

def mul(state, a_index, b):
    if is_address(b):
        reg = REG_INDEX_FOR[b]
        rhs = state[reg]
    else:
        rhs = int(b)
    state[a_index] = state[a_index]*rhs

def div(state, a_index, b):
    if is_address(b):
        reg = REG_INDEX_FOR[b]
        rhs = state[reg]
    else:
        rhs = int(b)
    state[a_index] = state[a_index]//rhs

def mod(state, a_index, b):
    if is_address(b):
        reg = REG_INDEX_FOR[b]
        rhs = state[reg]
    else:
        rhs = int(b)
    state[a_index] = state[a_index]%rhs

def eql(state, a_index, b):
    if is_address(b):
        reg = REG_INDEX_FOR[b]
        rhs = state[reg]
    else:
        rhs = int(b)
    lhs = state[a_index]
    if lhs == rhs:
        state[a_index] = 1
    else:
        state[a_index] = 0


def apply_reved_program(ref, inps):
    result = 0
    for i in range(len(inps)):
        a, b, c = REVED_PROGRAM[i]
        result = reved(result, inps[i], a, b, c)
    return result

REVED_PROGRAM = [
        (1, 12, 7),
        (1, 12, 8),
        (1, 13, 2),
        (1, 12, 11),
        (26, -3, 6),
        (1, 10, 12),
        (1, 14, 14),
        (26, -16, 13),
        (1, 12, 15),
        (26, -8, 10),
        (26, -12, 6),
        (26, -7, 10),
        (26, -6, 8),
        (26, -11, 5)]

def reved(previous, inp, a, b, c):
    if a == 26:
        is_possible = 1 <= previous % 26 + b <= 9
        target_inp = previous % 26 + b
        print(inp, (a, b, c), previous % 26, target_inp, is_possible, inp == target_inp)
    else:
        print(inp, (a, b, c))
    if previous % 26 == inp - b:
        result = previous // a
        print(previous, 'vvv', result)
    else:
        result = (previous//a) * 26 + inp + c
        print(previous, '^^^', result)
    return result


if __name__ == '__main__' and not sys.flags.interactive:
    program = [[w for w in line.strip().split()] for line in fileinput.input()]
    print(solve_1(program))
