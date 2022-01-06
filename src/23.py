import sys
import fileinput
import re
from collections import deque
from heapq import heappush, heappop, heapify


ENERGY_FOR = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

def solve_1(filled_maze):
    for r in filled_maze:
        print(r)
    return start_cost_and_room_stacks(filled_maze)

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
