import sys
import fileinput
from collections import Counter


def solve(polymer, rules, n):
    pair_counter = Counter()
    for i in range(len(polymer)-1):
        pair = polymer[i:i+2]
        pair_counter[pair] += 1
    letter_counter = Counter(polymer)
    for _ in range(n):
        step(rules, pair_counter, letter_counter)
    ordered = letter_counter.most_common()
    return ordered[0][1] - ordered[-1][1]


def step(rules, pc, lc):
    for pair, n in pc.copy().items():
        mid = rules[pair]
        left = pair[0]
        right = pair[1]

        pc[pair] -= n
        lc[mid] += n
        pc[left+mid] += n
        pc[mid+right] += n


if __name__ == '__main__' and not sys.flags.interactive:
    lines = [line.strip() for line in fileinput.input()]
    polymer = lines[0]
    rulePairs = [line.split(' -> ') for line in lines[2:]]
    rules = {r[0]: r[1] for r in rulePairs}
    print(solve(polymer, rules, 10))
    print(solve(polymer, rules, 40))
