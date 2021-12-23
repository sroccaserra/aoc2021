import sys
import fileinput
import re


ENERGY_FOR = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

TOP = 1
MIDDLE = 2
BOTTOM = 3

DEST_FOR = {'A': 3, 'B': 5, 'C': 7, 'D': 9}


def solve_1(filled_maze):
    for r in filled_maze:
        print(r)
    state = find_starting_positions(filled_maze)
    maze = empty_maze(filled_maze)
    dp = {}
    return find_minimum_cost(dp, maze, state)


def find_minimum_cost(dp, maze, state):
    key = tuple(sorted(state))
    if key in dp:
        return dp[key]
    if len(dp)+1 % 100 == 0:
        print(len(dp))
    moveable_amphipods = find_moveable_amphipods(state)
    if len(moveable_amphipods) == 0:
        dp[key] = 0
        print('hey!')
        return 0
    possible_results = []
    for a in moveable_amphipods:
        possible_moves = find_possible_moves(maze, state, a)
        if (len(possible_moves)) > 0:
            print(possible_moves)
        for move in possible_moves:
            new_state = apply_move(state, move)
            possible_results.append(energy_for(move)+find_minimum_cost(dp, maze, new_state))
    result = min(possible_results)
    dp[key] = result
    return result


def find_moveable_amphipods(state):
    result = []
    for a in state:
        letter, (x, y) = a
        if x in [3, 5, 7, 9] and y == TOP:
            # a's move is not finished, it is the only one that can continue
            return [a]
        if y == TOP:
            result.append(a)
            continue
        if x != DEST_FOR[letter]:
            result.append(a)
            continue
        if y == BOTTOM:
            continue
        other_pos = other_same_pos(state, a)
        if other_pos == (x, BOTTOM):
            continue
        result.append(a)

    return result


def find_possible_moves(maze, state, amphipod):
    letter, (xa, ya) = amphipod
    neighbors = [(xa+1, ya), (xa-1, ya), (xa, ya+1), (xa, ya-1)]
    non_walls = [(xn, yn) for xn, yn in neighbors if '.' == maze[yn][xn]]
    return [(letter, (xa, ya), (xn, yn)) for xn, yn in non_walls if not is_occupied(state, (xn, yn))]


def apply_move(state, move):
    letter, src, dst = move
    result = [a for a in state if a != (letter, src)]
    result.append((letter, dst))
    return result


def energy_for(move):
    letter = move[0]
    return ENERGY_FOR[letter]

def other_same_pos(state, amphipod):
    (letter, pos) = amphipod
    for other_letter, other_pos in state:
        if other_letter == letter and other_pos != pos:
            return other_pos


def is_occupied(state, position):
    for _, p in state:
        if position == p:
            return True
    return False


def empty_maze(filled_maze):
    return [re.sub('[A-D]', '.', row) for row in filled_maze]


def find_starting_positions(maze):
    w = len(maze[0])
    h = len(maze)
    result = []
    for y in range(h):
        for x in range(w):
            if maze[y][x] in 'ABCD':
                result.append((maze[y][x], (x, y)))
    return result


if __name__ == '__main__' and not sys.flags.interactive:
    lines = [line.strip() for line in fileinput.input()]
    w = len(lines[0])
    filled_maze = [line.center(w, ' ') for line in lines]
    print(solve_1(filled_maze))
