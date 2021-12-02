
def traverse_xy(inputs):
    x, y = 0, 0
    for (c, v) in inputs:
        if c == 'forward':
            x += v
        elif c == 'down':
            y += v
        elif c == 'up':
            y -= v
    return (x, y)

def solve_p1(inputs):
    final_xy = traverse_xy(inputs)
    return final_xy[0] * final_xy[1]

def traverse_aim(inputs):
    x, y, aim = 0, 0, 0
    for (c, v) in inputs:
        if c == 'down':
            aim += v
        elif c == 'up':
            aim -= v
        elif c == 'forward':
            x += v
            y += aim * v
    return (x, y)

def solve_p2(inputs):
    final_xy = traverse_aim(inputs)
    return final_xy[0] * final_xy[1]

with open('inputs/day2.in') as f:
    inputs = [(line.split()[0], int(line.split()[1])) for line in f]
    print(f'P1: {solve_p1(inputs)}')
    print(f'P2: {solve_p2(inputs)}')
