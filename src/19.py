import sys
import fileinput
from collections import Counter


def solve_1(scanners):
    nb_scanners = len(scanners)
    is_aligned = [False]*nb_scanners
    to_visit = [scanners[0]]
    is_aligned[0] = True
    aligned = [scanners[0]]
    memo = {}
    while not all(is_aligned):
        scanner = to_visit.pop()
        for i, other in enumerate(scanners):
            if is_aligned[i]:
                print('aligned', i)
                continue
            print(i)
            matching = find_matching(memo, scanner, other)
            if matching is not None:
                print('matching', i)
                aligned.append(matching)
                is_aligned[i] = True
                to_visit.append(matching)
    return len(set().union(*aligned))


def find_matching(memo, scanner, other):
    for i, t in enumerate(TRANSFOS):
        transformed = [transform(memo, i, p) for p in other]
        distances = Counter()
        for (tx, ty, tz) in transformed:
            for (x, y, z) in scanner:
                distances[(x-tx, y-ty, z-tz)] += 1
        (most_common_distance, n) = distances.most_common(1)[0]
        if n >= 12:
            dx, dy, dz = most_common_distance
            return set([(tx + dx, ty + dy, tz + dz) for (tx, ty, tz) in transformed])
    return None


def transform(memo, i, p):
    if (i, p) in memo:
        return memo[(i, p)]
    t = TRANSFOS[i]
    result = multiply(t, p)
    memo[(i, p)] = result
    return result


TRANSFOS = [
        [[1, 0, 0],[0, 1, 0], [0, 0, 1]],
        [[1, 0, 0],[0, -1, 0], [0, 0, -1]],
        [[1, 0, 0],[0, 0, -1], [0, 1, 0]],
        [[1, 0, 0],[0, 0, 1], [0, -1, 0]],
        [[-1, 0, 0],[0, 1, 0], [0, 0, -1]],
        [[-1, 0, 0],[0, -1, 0], [0, 0, 1]],
        [[-1, 0, 0],[0, 0, 1], [0, 1, 0]],
        [[-1, 0, 0],[0, 0, -1], [0, -1, 0]],

        [[0, 1, 0],[1, 0, 0], [0, 0, -1]],
        [[0, -1, 0],[1, 0, 0], [0, 0, 1]],
        [[0, 0, 1],[1, 0, 0], [0, 1, 0]],
        [[0, 0, -1],[1, 0, 0], [0, -1, 0]],
        [[0, 1, 0],[-1, 0, 0], [0, 0, 1]],
        [[0, -1, 0],[-1, 0, 0], [0, 0, -1]],
        [[0, 0, -1],[-1, 0, 0], [0, 1, 0]],
        [[0, 0, 1],[-1, 0, 0], [0, -1, 0]],

        [[0, 0, -1],[0, 1, 0], [1, 0, 0]],
        [[0, 0, 1],[0, -1, 0], [1, 0, 0]],
        [[0, 1, 0],[0, 0, 1], [1, 0, 0]],
        [[0, -1, 0],[0, 0, -1], [1, 0, 0]],
        [[0, 0, 1],[0, 1, 0], [-1, 0, 0]],
        [[0, 0, -1],[0, -1, 0], [-1, 0, 0]],
        [[0, 1, 0],[0, 0, -1], [-1, 0, 0]],
        [[0, -1, 0],[0, 0, 1], [-1, 0, 0]],
        ]

def multiply(m, p):
    result = [0, 0, 0]
    for i in range(3):
        r = m[i]
        for j in range(3):
            result[i] += r[j]*p[j]
    return tuple(result)

if __name__ == '__main__' and not sys.flags.interactive:
    lines = [line.strip() for line in fileinput.input()]
    scanners = []
    for line in lines:
        if len(line) == 0:
            continue
        if line[4] == 's':
            scanner = set()
            scanners.append(scanner)
        else:
            scanner.add(tuple([int(w) for w in line.split(',')]))

    print(solve_1(scanners))
