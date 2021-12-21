import sys
import fileinput


PLAYER_1_START = 8
PLAYER_2_START = 7

#PLAYER_1_START = 4
#PLAYER_2_START = 8

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


def create_dice():
    n = 1
    while True:
        yield n
        n += 1
        if n > 100:
            n -= 100


if __name__ == '__main__' and not sys.flags.interactive:
    print(solve_1(PLAYER_1_START, PLAYER_2_START))
