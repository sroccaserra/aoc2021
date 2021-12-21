import sys
import fileinput


PLAYER_1_START = 8
PLAYER_2_START = 7

# PLAYER_1_START = 4
# PLAYER_2_START = 8


def solve_1(p1_start, p2_start):
    dice = create_dice()
    p1_pos = p1_start
    p2_pos = p2_start
    p1_score = 0
    p2_score = 0
    nb_rolls = 0

    while True:
        s = 0
        for _ in range(3):
            nb_rolls += 1
            d = next(dice)
            s += d
        p1_pos = (p1_pos + s - 1)%10 + 1
        p1_score += p1_pos
        if p1_score >= 1000:
            break

        s = 0
        for _ in range(3):
            nb_rolls += 1
            d = next(dice)
            s += d
        p2_pos = (p2_pos + s - 1)%10 + 1
        p2_score += p2_pos
        if p2_score >= 1000:
            break

    return nb_rolls*p2_score


P1 = 0
P2 = 1
POSSIBLE_MOVES = [3, 4, 5, 6, 7, 8, 9,]
UNIVERSES_FOR_MOVES = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


def solve_2(p1_start, p2_start):
    """

    `(0 0) -- [1 j1 (4 21) (8 21)]`
    state = (1, P1, (4, 21), (8, 21))
    """
    wins = [0, 0]
    to_visit = [(1, P1, (p1_start, 21), (p2_start, 21))]
    m = {}
    find_wins(wins, to_visit)
    return max(wins)


def find_wins(wins, to_visit):
    while to_visit:
        state = to_visit.pop()
        # print(wins, state, to_visit)

        next_states = generate_next(state)
        player = turn(state)
        all_wins = True
        for ns in next_states:
            if goal(player, ns) > 0:
                to_visit.append(ns)
                all_wins = False
            else:
                wins[player] += nb_universes(ns)

    return wins, to_visit


def generate_next(state):
    result = []
    player = turn(state)
    other = other_player(player)
    n = nb_universes(state)
    p = pos(player, state)
    op = pos(other, state)
    g = goal(player, state)
    og = goal(other, state)
    for pm in POSSIBLE_MOVES:
        new_n = n*UNIVERSES_FOR_MOVES[pm]
        new_pos = advance(p, pm)
        new_goal = g - new_pos
        if player == P1:
            result.append((new_n, P2, (new_pos, new_goal), (op, og)))
        else:
            result.append((new_n, P1, (op, og), (new_pos, new_goal)))
    return result


def other_player(player):
    if player == P1:
        return P2
    return P1

def advance(start, move):
    return (start + move - 1)%10 + 1

def nb_universes(state):
    return state[0]

def turn(state):
    return state[1]

def pos(player, state):
    return state[2+player][0]

def goal(player, state):
    return state[2+player][1]

def create_dice():
    n = 1
    while True:
        yield n
        n += 1
        if n > 100:
            n -= 100


if __name__ == '__main__' and not sys.flags.interactive:
    print(solve_1(PLAYER_1_START, PLAYER_2_START))
    print(solve_2(PLAYER_1_START, PLAYER_2_START))
