import sys
import fileinput
from collections import deque


EX_0 = 'D2FE28'
EX_1 = '38006F45291200'
EX_2 = 'EE00D40C823060'
EX_3 = '8A004A801A8002F478'
EX_4 = '620080001611562C8802118E34'
EX_5 = 'C0015000016115A2E0802F182340'
EX_6 = 'A0016C880162017C3686B18A3D4780'


S = [0]


def solve_1(line):
    pc = 0
    rom = to_01_list(line)
    ast = []
    state = [pc, rom, ast]
    read_packets(state)
    return S[0]


def sum_versions(packets):
    if type(packets) == int:
        return 0


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
    #for ex in [EX_4]:
    #    print(solve_1(ex))
    print(solve_1(line))
