import sys
import fileinput
from collections import Counter
from itertools import combinations


def solve(scanners):
    nb_scanners = len(scanners)
    is_assembled = [False]*nb_scanners
    to_visit = [scanners[0]]
    is_assembled[0] = True
    assembled = [scanners[0]]
    distances = []
    while not all(is_assembled):
        scanner = to_visit.pop()
        for i, other in enumerate(scanners):
            if is_assembled[i]:
                continue
            matching, distance = find_matching(scanner, other)
            if matching is not None:
                distances.append(distance)
                assembled.append(matching)
                is_assembled[i] = True
                to_visit.append(matching)

    print(len(set().union(*assembled)))
    print(max_distance(distances))


def find_matching(scanner, other):
    for rotation in ROTATIONS:
        rotated = [multiply(rotation, p) for p in other]
        distances = Counter()
        for (rx, ry, rz) in rotated:
            for (x, y, z) in scanner:
                distances[(x-rx, y-ry, z-rz)] += 1
        (most_common_distance, n) = distances.most_common(1)[0]
        if n >= 12:
            dx, dy, dz = most_common_distance
            return set([(rx + dx, ry + dy, rz + dz) for (rx, ry, rz) in rotated]), (dx,dy,dz)
    return None, None


ROTATIONS = [
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


def max_distance(distances):
    result = 0
    for d1, d2 in combinations(distances, 2):
        (x1, y1, z1) = d1
        (x2, y2, z2) = d2
        d = abs(x2-x1)+abs(y2- y1)+abs(z2-z1)
        if d > result:
            result = d
    return result


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
    solve(scanners)
