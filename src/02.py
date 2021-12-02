import sys
import fileinput

def solve_1(moves):
    pos = [0, 0]
    for move in moves:
        match move:
            case ('forward', x):
                pos[0] += x
            case ('up', x):
                pos[1] -= x
            case ('down', x):
                pos[1] += x
    return pos[0]*pos[1]

def solve_2(moves):
    pos = [0, 0]
    aim = 0
    for move in moves:
        match move:
            case ('forward', x):
                pos[0] += x
                pos[1] += x*aim
            case ('up', x):
                aim -= x
            case ('down', x):
                aim += x
    return pos[0]*pos[1]

if __name__ == '__main__' and not sys.flags.interactive:
    words = [line.strip().split() for line in fileinput.input()]
    moves = [(w[0], int(w[1])) for w in words]
    print(solve_1(moves))
    print(solve_2(moves))
