import sys
import fileinput
from types import SimpleNamespace
from collections import namedtuple, deque

State = namedtuple('State', ['w', 'x', 'y', 'z'])

REG_INDEX_FOR = {'w': 0, 'x': 1, 'y': 2, 'z': 3}


def solve_1(program):
    inps = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    state_1 = apply_reved_program(inps)
    state_2 = apply_program(program, inps)
    return state_1, state_2

def apply_program(program, inps):
    state = [0, 0, 0, 0]
    pc = 0
    n = 0
    for pc in range(len(program)):
        instruction = program[pc]
        if instruction[0] == 'inp':
            n = 0
        print(n, pc, instruction, state)
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


def apply_reved_program(inps):
    state = [0, 0, 0, 0]
    for i in range(len(inps)):
        a, b, c = REVED_PROGRAM[i]
        print(inps[i], (a,b,c))
        reved(state, inps[i], a, b, c)
        result = state[3]
        print(result)
    return state

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

def reved(state, inp, a, b, c):
    # if inp == state[3]%26 + b:
    #     return 26*state[3]//a
    # else:
    #     return state[3]//a + inp + c
    w = inp
    x = state[1]
    y = state[2]
    z = state[3]
    print('start', w, z)
    x = 0
    x = z       # 1 et 2 : on copie z dans x
    print(3, x, y, z)
    x = x%26    # donc on calcule le modulo de z0 par 26
    print(4, x, y, z)
    z = z // a   # noop, pas encore utilisé pour le moment.
    print(5, x, y, z)
    x += b      # on ajoute 12, on est à x = (z0%26) + 12
    print(6, x, y, z)
    x = 1 if x == w else 0  # x = 1 si l'input est égal à (z0%26) + 12
    print(7, x, y, z)
    x = 0 if x == 1 else 1  # not x   # x = 1 si l'input est différent de z0%26 + 12
    y = 0
    y = 25      # on ajoute 25 à y, en pratique on a mis 25 dans y
    print(10, x, y, z)
    y = y * x   # on met y à zéro si w est différent de z0%26+12
    print(11, x, y, z)
    y += 1      # on incrémente y (qui devient 1 ou 26)
    print(12, x, y, z)
    z = z * y   # z = (w == z0%26 + 12) ? z * 26 : z)
    y = 0
    print(14, x, y, z)
    y = w
    print(15, x, y, z)
    y = w + c
    print(16, x, y, z)
    y = y * x   # y = (w == z0%26+12) ? 0 : w + 7
    print(17, x, y, z)
    z = z + y   # result += (w == z0%26+12) ? 0 : w + 7
    print('end', z)
    state[3] = z


if __name__ == '__main__' and not sys.flags.interactive:
    program = [[w for w in line.strip().split()] for line in fileinput.input()]
    print(solve_1(program))
