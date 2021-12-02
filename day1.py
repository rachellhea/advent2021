from itertools import tee

def n_wise(iterable, n=2):
    chunks = tee(iterable, n)
    for i in range(len(chunks)):
        for j in range(i):
            next(chunks[i], None)
    return zip(*chunks)

def solve_p1(inputs):
    return sum(map(int, (curr > prev for (prev, curr) in n_wise(inputs, 2))))

def solve_p2(inputs):
    return solve_p1([sum([a, b, c]) for (a, b, c) in n_wise(inputs, 3)])

with open('inputs/day1.in') as f:
    inputs = [int(x) for x in f]
    print(f'P1: {solve_p1(inputs)}')
    print(f'P2: {solve_p2(inputs)}')
