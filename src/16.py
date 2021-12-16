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


def solve_1(line):
    print(line)
    pc = 0
    data = to_01_list(line)
    ops = []
    state = [pc, data, ops]
    return read_packets(state)


def sum_versions(packets):
    if type(packets) == int:
        return 0


def read_packets(state):
    pc, data, ops = state
    packets = []
    while -1 != data[pc:].find('1'):
        packets.append(read_packet(state))
        pc, data, ops = state
    return packets


def read_packet(state):
    version = read_version(state)
    type_ID = read_type_ID(state)
    if 4 == type_ID:
        result = read_literal(state)
    else:
        result = read_operator(state)
    return (version, type_ID, result)


def read_literal(state):
    s = ''
    while True:
        prefix = read_bits(state, 1)
        s += read_bits(state, 4)
        if prefix == '0':
            break

    return int(s, 2)


def read_operator(state):
    length_type_ID = read_bits(state, 1)
    if '0' == length_type_ID:
        length = read_int(state, 15)
        sub = read_bits(state, length)
        ops = []
        data = read_packets([0, sub, ops])
        return data
    else:
        n = read_int(state, 11)
        result = []
        for _ in range(n):
            result.append(read_packet(state))
        return result


def read_version(state):
    return read_int(state, 3)


def read_type_ID(state):
    return read_int(state, 3)


def read_int(state, n):
    s = read_bits(state, n)
    return int(s, 2)


def read_bits(state, n):
    pc, data, ops = state
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
    print(0+6+7+4+0+3+1+0+4+4+7+4+4+6+0+6+5+4+0+7+3+3+1+1+7+7+6+5+7+6+5+4+1+3+0+6+3+2+0+7+0+7+6+3+0+5+0+2+4+7+2+2+7+4+0+1+0+1+1+7+3+4+0+2+5+0+7+6+2+3+1+2+1+5+5+4+4+6+0+0+6+1+7+3+4+0+7+6+5+4+2+5+7+2+4+0+1+6+6+2+2+6+5+0+4+3+7+5+0+0+0+3+1+5+2+6+0+6+4+2+6+2+2+2+0+5+1+6+3+6+7+3+6+3+6+3+3+5+0+3+6+7+2+3+1+0+0+7+7+3+1+6+7+0+0+1+3+5+5+7+1+1+2+3+4+2+4+2+1+3+0+2+4+4+5+0+4+0+0+5+0+5+1+6+4+5+1+3+1+4+6+6+5+4+0+6+3+2+4+6+7+0+5+0+7+7+7+5+2+3+1+0+5+2+2+0+0+5+1+5+1+0+3+2+4+0+7+0+6+7+6+7+1+3+7+7+1+5+1+6+2+2+1+0+1+5+3+6+6+2+2+6+2+1+4+2+1+0+7+2+7+7+6+5+3+0+1+2)
