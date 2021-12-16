import sys
import fileinput
from collections import deque


# Part one examples
EX_00 = 'D2FE28'
EX_01 = '38006F45291200'
EX_02 = 'EE00D40C823060'
EX_03 = '8A004A801A8002F478'
EX_04 = '620080001611562C8802118E34'
EX_05 = 'C0015000016115A2E0802F182340'
EX_06 = 'A0016C880162017C3686B18A3D4780'

# Part two examples
EX_07 = 'C200B40A82'
EX_08 = '04005AC33890'
EX_09 = '880086C3E88112'
EX_10 = 'CE00C43D881120'
EX_11 = 'D8005AC2A8F0'
EX_12 = 'F600BC2D8F'
EX_13 = '9C005AC2F8F0'
EX_14 = '9C0141080250320F1802104A08'

S = [0]


def solve_1(line):
    pc = 0
    rom = to_01_list(line)
    ast = []
    state = [pc, rom, ast]
    read_packets(state)
    return S[0]


def solve_2(line):
    pc = 0
    rom = to_01_list(line)
    ast = []
    state = [pc, rom, ast]
    read_packets(state)
    return eval_ast(ast[0])


def eval_ast(ast):
    (_, type_ID, data) = ast
    if type_ID == 0:
        result = 0
        for operand in data:
            result += eval_ast(operand)
        return result
    if type_ID == 1:
        result = 1
        for operand in data:
            result *= eval_ast(operand)
        return result
    if type_ID == 2:
        result = min([eval_ast(operand) for operand in data])
        return result
    if type_ID == 3:
        result = max([eval_ast(operand) for operand in data])
        return result
    if type_ID == 4:
            return data
    if type_ID == 5:
        if eval_ast(data[0]) > eval_ast(data[1]):
            return 1
        return 0
    if type_ID == 6:
        if eval_ast(data[0]) < eval_ast(data[1]):
            return 1
        return 0
    if type_ID == 7:
        if eval_ast(data[0]) == eval_ast(data[1]):
            return 1
        return 0
    return type_ID, data, result


def read_packets(state):
    pc, rom, _ = state
    packets = []
    while -1 != rom[pc:].find('1'):
        packets.append(read_packet(state))
        pc, rom, _ = state


def read_packet(state):
    version = read_version(state)
    S[0] += version
    type_ID = read_type_ID(state)
    if 4 == type_ID:
        read_literal(version, type_ID, state)
    else:
        read_operator(version, type_ID, state)


def read_literal(version, type_ID, state):
    s = ''
    while True:
        prefix = read_bits(state, 1)
        s += read_bits(state, 4)
        if prefix == '0':
            break

    n = int(s, 2)
    state[2].append((version, type_ID, n))


def read_operator(version, type_ID, state):
    length_type_ID = read_bits(state, 1)
    if '0' == length_type_ID:
        length = read_int(state, 15)
        sub_rom = read_bits(state, length)
        sub_ast = []
        read_packets([0, sub_rom, sub_ast])
    else:
        n = read_int(state, 11)
        pc, rom, _ = state
        sub_rom = rom[pc:]
        sub_state = [0, sub_rom, []]
        for _ in range(n):
            read_packet(sub_state)
        state[0] += sub_state[0]
        sub_ast = sub_state[2]
    state[2].append((version, type_ID, sub_ast))


def read_version(state):
    return read_int(state, 3)


def read_type_ID(state):
    return read_int(state, 3)


def read_int(state, n):
    s = read_bits(state, n)
    return int(s, 2)


def read_bits(state, n):
    pc, data, _ = state
    state[0] += n
    return ''.join(data[pc:pc+n])


def to_01_list(line):
    bits = ''
    for i in range(len(line)//2):
        k = i*2
        n = int(line[k:k+2], 16)
        s = f'{n:08b}'
        bits += s
    return bits


if __name__ == '__main__' and not sys.flags.interactive:
    line = next(fileinput.input()).strip()
    print(solve_1(line))
    print(solve_2(line))
