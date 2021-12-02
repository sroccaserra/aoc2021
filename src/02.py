import sys
import fileinput

def solve_1(lines):
    pos = [0, 0]
    for move in moves:
        x = move[1]
        if move[0] == 'forward':
            pos[0] += x
        if move[0] == 'up':
            pos[1] -= x
        if move[0] == 'down':
            pos[1] += x
    return pos[0]*pos[1]

def solve_2(lines):
    pos = [0, 0]
    aim = 0
    for move in moves:
        x = move[1]
        if move[0] == 'forward':
            pos[0] += x
            pos[1] += x*aim
        if move[0] == 'up':
            aim -= x
        if move[0] == 'down':
            aim += x
    return pos[0]*pos[1]

if __name__ == '__main__' and not sys.flags.interactive:
    lines = [line.strip() for line in fileinput.input()]
    ws = [line.split() for line in lines]
    moves = [(w[0], int(w[1])) for w in ws]
    print(solve_1(moves))
    print(solve_2(lines))
