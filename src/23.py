import sys
import fileinput
import re


ENERGY_FOR = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
FREE = '.'

DISTANCES = [
        [3, 5, 7, 9,],
        [2, 4, 6, 8,],
        [2, 2, 4, 6,],
        [4, 2, 2, 4,],
        [6, 4, 2, 2,],
        [8, 6, 4, 2,],
        [9, 7, 5, 3,],]

##
# TODO

# - Générer les mouvements possibles du couloir vers les chambres
# - Faire la recherche de minimum


def solve_1(filled_maze):
    for r in filled_maze:
        print(r)
    m = {}

    cost, state = start_cost_and_state(filled_maze)
    state_key = encode_state(state)
    m[state_key] = cost

    ns = neighbors_with_cost(state)
    cost, state = ns[4]
    state_key = encode_state(state)
    m[state_key] = cost
    print(decode_state(state_key))
    ns = neighbors_with_cost(state)
    return len(ns), ns


def neighbors_with_cost(state):
    hallway, rooms = state
    return [apply_move(move, hallway, rooms) for move in possible_moves(hallway, rooms)]


def apply_move(move, hallway, rooms):
    cost, dst, room_index = move
    room = rooms[room_index]
    hallway = hallway[0:dst]+room[-1] + hallway[dst+1:]
    rooms = list(rooms)
    rooms[room_index] = room[:-1]
    return cost, (hallway, rooms)


def possible_moves(hallway, rooms):
    return possible_moves_to_rooms(hallway, rooms) + possible_moves_to_hallway(hallway, rooms)


def possible_moves_to_rooms(hallway, rooms):
    return []


def possible_moves_to_hallway(hallway, rooms):
    """
    i: 01 2 3 4 56
       .. . . . ..
         a b c d
    j:   0 1 2 3

    i = 0, j = 0 => 01  range(0, 2) pivot = 2
    i = 1, j = 0 => 1
    i = 2, j = 0 => 2
    i = 3, j = 0 => 23
    i = 4, j = 0 => 234

    i = 0, j = 1 => 012 range(0, 3) pivot = 3
    i = 1, j = 1 => 12  range(1, 3)
    i = 2, j = 1 => 2   range(2, 3)
    i = 3, j = 1 => 3   range(3, 4)
    i = 4, j = 1 => 34  range(3, 5)
    i = 5, j = 1 => 345 range(3, 6)

    i = 0, j = 2 => 0123 range(0, 4) pivot = 4

    i = 0, j = 3 => 0123 range(0, 5) pivot = 5

    pivot = j+2 !

    if i < pivot
    """
    result = []
    for dst_i in range(len(hallway)):
        c = hallway[dst_i]
        if c != FREE:
            continue
        for src_j in range(len(rooms)):
            room = rooms[src_j]
            if len(room) == 0:
                continue

            pivot = src_j + 2
            if dst_i < pivot:
                in_betweens = range(dst_i, pivot)
            else:
                in_betweens = range(pivot, dst_i+1)
            is_reachable = True
            for k in in_betweens:
                if hallway[k] != FREE:
                    is_reachable = False
                    continue
            if not is_reachable:
                continue

            amphipod = room[-1]
            distance = DISTANCES[dst_i][src_j]
            cost = distance*ENERGY_FOR[amphipod]
            result.append((cost, dst_i, src_j))
    return result


def encode_state(state):
    hallway, rooms = state
    return hallway, tuple([tuple(r) for r in rooms])


def decode_state(state_key):
    hallway = state_key[0]
    rooms = [list(r) for r in state_key[1]]
    return hallway, rooms


def start_cost_and_state(filled_maze):
    rooms = []
    cost = 0
    max_depth = 2
    for j, expected in [(3, 'A'), (5, 'B'), (7, 'C'), (9, 'D')]:
        room = []
        rooms.append(room)
        is_at_destination = True
        depth = max_depth + 1
        for i in reversed(range(2, 2+max_depth)):
            c = filled_maze[i][j]
            depth -= 1
            if is_at_destination and c == expected:
                continue
            is_at_destination = False
            cost += depth*ENERGY_FOR[c]
            room.append(c)
    hallway = FREE*7
    return cost, (hallway, rooms)


if __name__ == '__main__' and not sys.flags.interactive:
    lines = [line.strip() for line in fileinput.input()]
    w = len(lines[0])
    filled_maze = [line.center(w, ' ') for line in lines]
    print(solve_1(filled_maze))
