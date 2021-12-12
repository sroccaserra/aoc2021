import sys
import fileinput
from collections import defaultdict
from queue import deque


def backtrack(a, context):
    if is_a_solution(a, context):
        process_solution(a, context)
        return
    cs = construct_candidates(a, context)
    for c in cs:
        backtrack(a+[c], context)


def is_a_solution(a, context):
    return a and a[-1] == context['dst']


def process_solution(a, context):
    # print([a[i] for i in range(len(a))])
    context['nb_solutions'] += 1


def construct_candidates(a, context):
    if a == []:
        return [context['src']]
    graph = context['graph']
    result = graph[a[-1]].copy()
    result.discard('start')
    for v in a:
        if v.islower() and v in result:
            if not context['allow_doubles'] or has_two_low(a):
                result.remove(v)
    return result


def has_two_low(a):
    for i in range(1, len(a)):
        if not a[i].islower():
            continue
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                return True
    return False


def solve_1(graph):
    context = {'graph': graph, 'nb_solutions': 0, 'src': 'start', 'dst': 'end', 'allow_doubles': False}
    backtrack([], context)
    return context['nb_solutions']


def solve_2(graph):
    context = {'graph': graph, 'nb_solutions': 0, 'src': 'start', 'dst': 'end', 'allow_doubles': True}
    backtrack([], context)
    return context['nb_solutions']


def solve_2_2(graph):
    q = deque()
    q.append(('start', set(['start']), None))
    result = 0
    while len(q) != 0:
        pos, seen, double = q.popleft()
        if pos == 'end':
            result += 1
        else:
            for adj in graph[pos]:
                if adj not in seen:
                    next_seen = seen.copy()
                    if adj.islower():
                        next_seen.add(adj)
                    q.append((adj, next_seen, double))
                elif adj in seen and double is None and adj not in ['start', 'end']:
                    q.append((adj, seen, adj))
    return result


if __name__ == '__main__' and not sys.flags.interactive:
    edges = [tuple(line.strip().split('-')) for line in fileinput.input()]
    graph = defaultdict(set)
    for e in edges:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    print(solve_1(graph))
    print(solve_2(graph))
