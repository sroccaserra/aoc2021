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

# - Traiter le blocage dans le couloir
# - Générer les mouvements possibles du couloir vers les chambres
# - Faire la recherche de minimum


def solve_1(filled_maze):
    for r in filled_maze:
        print(r)
    start_cost, rooms = start_cost_and_room_stacks(filled_maze)
    hallway = FREE*7
    m = {}
    state_key = encode_state(hallway, rooms)
    m[state_key] = start_cost
    print(decode_state(state_key))
    return neighbors_with_cost((hallway, rooms))


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
    result = []
    for dst_i in range(len(hallway)):
        c = hallway[dst_i]
        if c != '.':
            continue
        for src_j in range(len(rooms)):
            room = rooms[src_j]
            if len(room) == 0:
                continue
            amphipod = room[-1]
            distance = DISTANCES[dst_i][src_j]
            cost = distance*ENERGY_FOR[amphipod]
            result.append((cost, dst_i, src_j))
    return result


def encode_state(hallway, rooms):
    return hallway, tuple([tuple(r) for r in rooms])


def decode_state(state_key):
    hallway = state_key[0]
    rooms = [list(r) for r in state_key[1]]
    return hallway, rooms


def start_cost_and_room_stacks(filled_maze):
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
    return cost, rooms


if __name__ == '__main__' and not sys.flags.interactive:
    lines = [line.strip() for line in fileinput.input()]
    w = len(lines[0])
    filled_maze = [line.center(w, ' ') for line in lines]
    print(solve_1(filled_maze))
