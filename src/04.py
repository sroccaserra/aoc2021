import sys
import fileinput


def solve_1(grids_data, drawn_numbers):
    grids = init_grids(grids_data)
    return play_1(grids, drawn_numbers)


def solve_2(grids_data, drawn_numbers):
    grids = init_grids(grids_data)
    return play_2(grids, drawn_numbers)


def init_grids(grids_data):
    result = []
    for data in grids_data:
        unmarked = set()
        for l in data:
            for n in l:
                unmarked.add(n)
        result.append({'rs': rows(data), 'cs': columns(data), 'ns': unmarked, 'won': False})
    return result


def rows(data):
    return [set(row) for row in data]


def columns(data):
    result = []
    for j in range(len(data[0])):
        col = set()
        result.append(col)
        for i in range(len(data)):
            col.add(data[i][j])
    return result


def mark(grid, n):
    for row in grid['rs']:
        row.discard(n)
    for col in grid['cs']:
        col.discard(n)
    grid['ns'].discard(n)


def play_1(grids, drawn_numbers):
    for n in drawn_numbers:
        for grid in grids:
            mark(grid, n)
            if wins(grid):
                return score(grid, n)


def play_2(grids, drawn_numbers):
    nb_grids = len(grids)
    nb_wins = 0
    for n in drawn_numbers:
        for grid in grids:
            mark(grid, n)
            if not grid['won'] and wins(grid):
                grid['won'] = True
                nb_wins += 1
                if(nb_wins == nb_grids):
                    return score(grid, n)


def wins(grid):
    for r in grid['rs']:
        if 0 == len(r):
            return True
    for c in grid['cs']:
        if 0 == len(c):
            return True
    return False


def score(grid, n):
    return sum(grid['ns'])*n


if __name__ == '__main__' and not sys.flags.interactive:
    lines = [line.strip() for line in fileinput.input()]
    header = lines[0]
    ns = [[int(w) for w in line.split()] for line in lines[1:]]
    grids_data = []
    for i in range(len(ns)//6):
        grids_data.append(ns[i*6+1:i*6+6])
    for data in grids_data:
        assert 5 == len(data)
    drawn_numbers = [int(w) for w in header.split(',')]
    print(solve_1(grids_data, drawn_numbers))
    print(solve_2(grids_data, drawn_numbers))
