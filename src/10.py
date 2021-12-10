import sys
import fileinput


OPENING = '([{<'
MATCHING = {')': '(', ']': '[', '}': '{', '>': '<'}


def solve_1(lines):
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    result = 0
    for line in lines:
        stack = []
        for c in line:
            if c in OPENING:
                stack.append(c)
            else:
                cl = stack.pop()
                if cl != MATCHING[c]:
                    result += points[c]
    return result


def solve_2(lines):
    points = {'(': 1, '[': 2, '{': 3, '<': 4}
    scores = []
    for line in lines:
        stack = []
        is_corrupted = False
        for c in line:
            if c in OPENING:
                stack.append(c)
            else:
                op = stack.pop()
                if op != MATCHING[c]:
                    is_corrupted = True
                    break
        if not is_corrupted:
            score = 0
            for c in reversed(stack):
                score = score*5 + points[c]
            scores.append(score)
    return sorted(scores)[len(scores)//2]


if __name__ == '__main__' and not sys.flags.interactive:
    lines = [line.strip() for line in fileinput.input()]
    print(solve_1(lines))
    print(solve_2(lines))
