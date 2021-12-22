import sys
import fileinput
from collections import defaultdict


def solve_1(instructions):
    reactor = defaultdict(lambda:'off')
    for status, ranges in instructions:
        for x in range(ranges[0][0], ranges[0][1]+1):
            if (x<-50) or (x > 50):
                continue
            for y in range(ranges[1][0], ranges[1][1]+1):
                if (y<-50) or (y > 50):
                    continue
                for z in range(ranges[2][0], ranges[2][1]+1):
                    if (z<-50) or (z > 50):
                        continue
                    reactor[(x, y, z)] = status

    result = 0
    for v in reactor.values():
        if v == 'on':
            result += 1
    return result


def solve_2(instructions):
    weighted_rects = []
    for status, ranges in instructions:
        x1, y1, z1 = ranges[0][0], ranges[1][0], ranges[2][0]
        x2, y2, z2 = ranges[0][1], ranges[1][1], ranges[2][1]
        rect = ((x1, y1, z1), (x2, y2, z2))
        weight = 1 if status == "on" else -1
        to_add = []
        for prev_weight, prev_rect in weighted_rects:
            if intersects(rect, prev_rect):
                common = common_rect(rect, prev_rect)
                if prev_weight == -1 and weight == -1:
                    to_add.append((1, common))
                if prev_weight == 1 and weight == -1:
                    to_add.append((-1, common))
                if prev_weight == -1 and weight == 1:
                    to_add.append((1, common))
                elif prev_weight == 1 and weight == 1:
                    to_add.append((-1, common))

        if weight == 1:
            weighted_rects.append((1, rect))
        weighted_rects += to_add

    result = 0
    for weight, rect in weighted_rects:
        result += weight*volume(rect)
    return result


def volume(rect):
    (x1, y1, z1) = rect[0]
    (x2, y2, z2) = rect[1]
    dx = 1 + abs(x2 - x1)
    dy = 1 + abs(y2 - y1)
    dz = 1 + abs(z2 - z1)
    return dx*dy*dz


def intersects(r1, r2):
    (r1x1, r1y1, r1z1) = r1[0]
    (r1x2, r1y2, r1z2) = r1[1]
    (r2x1, r2y1, r2z1) = r2[0]
    (r2x2, r2y2, r2z2) = r2[1]

    return segments_intersect(r1x1, r1x2, r2x1, r2x2) and \
            segments_intersect(r1y1, r1y2, r2y1, r2y2) and \
            segments_intersect(r1z1, r1z2, r2z1, r2z2)


def segments_intersect(a1, a2, b1, b2):
    return a2 >= b1 and b2 >= a1


def common_rect(r1, r2):
    (r1x1, r1y1, r1z1) = r1[0]
    (r1x2, r1y2, r1z2) = r1[1]
    (r2x1, r2y1, r2z1) = r2[0]
    (r2x2, r2y2, r2z2) = r2[1]
    topleftback = (max(r1x1, r2x1), max(r1y1, r2y1), max(r1z1, r2z1))
    bottomrightfront = (min(r1x2, r2x2),min(r1y2, r2y2),min(r1z2, r2z2))
    return (topleftback, bottomrightfront)


if __name__ == '__main__' and not sys.flags.interactive:
    lines = [line.strip().split() for line in fileinput.input() if line[0] != '#']
    instructions = [(status, [[int(w) for w in r[2:].split('..')] for r in ranges.split(',')]) for (status, ranges) in lines]
    print(solve_1(instructions))
    print(solve_2(instructions))
