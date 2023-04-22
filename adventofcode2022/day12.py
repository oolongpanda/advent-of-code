from time import perf_counter
from queue import PriorityQueue

t1 = perf_counter()
with open('input/day12.txt') as f:
    input = [l.strip() for l in f.readlines()]



def underestimation(current_point, costsofar, end_point):
    newestimate = costsofar + abs(current_point[0] - end_point[0]) + abs(current_point[1] - end_point[1])
    return newestimate



def part1 (input, start = False):
    S = False
    E = False
    while not S or not E:
        for l, line in enumerate(input):
            for p, point in enumerate(line):
                if point == 'S':
                    S = (l, p)
                    if start:
                        point = 'a'
                if point == 'E':
                    E = (l, p)
    if start:
        S = start
    q = PriorityQueue()
    q.put((underestimation(S, 0, E), S, 0))

    # stateplus = (priority, coordinates, movessofar)
    been_here = set()
    while not q.empty():
        stateplus = q.get()
        state, moves_so_far = stateplus[1], stateplus[2]
        letter = input[state[0]][state[1]]

        if state not in been_here:
            been_here.add(state)

            #up
            if state[0] != 0:
                move = input[state[0] - 1][state[1]]
                coordinates = (state[0] - 1, state[1])
                if move == 'E' and letter == 'z':
                    return moves_so_far + 1
                # if ord(move) <= ord(letter) + 1 or letter == 'S':
                if ord(move) <= ord(letter) + 1 or letter == 'S':
                    if (underestimation(coordinates, moves_so_far + 1, E), coordinates, moves_so_far + 1) not in q.queue:
                        # print((underestimation(coordinates, moves_so_far + 1, E), coordinates, moves_so_far + 1))
                        q.put((underestimation(coordinates, moves_so_far + 1, E), coordinates, moves_so_far + 1))

            #down
            if state[0] != len(input) - 1:
                move = input[state[0] + 1][state[1]]
                coordinates = (state[0] + 1, state[1])
                if move == 'E' and letter == 'z':
                    return moves_so_far + 1
                if ord(move) <= ord(letter) + 1 or letter == 'S':
                    if (underestimation(coordinates, moves_so_far + 1, E), coordinates, moves_so_far + 1) not in q.queue:
                        # print((underestimation(coordinates, moves_so_far + 1, E), coordinates, moves_so_far + 1))
                        q.put((underestimation(coordinates, moves_so_far + 1, E), coordinates, moves_so_far + 1))

            #left
            if state[1] != 0:
                move = input[state[0]][state[1] - 1]
                coordinates = (state[0], state[1] - 1)
                if move == 'E' and letter == 'z':
                    return moves_so_far + 1
                if ord(move) <= ord(letter) + 1 or letter == 'S':
                    if (underestimation(coordinates, moves_so_far + 1, E), coordinates, moves_so_far + 1) not in q.queue:
                        # print((underestimation(coordinates, moves_so_far + 1, E), coordinates, moves_so_far + 1))
                        q.put((underestimation(coordinates, moves_so_far + 1, E), coordinates, moves_so_far + 1))

            #right
            if state[1] != len(input[0]) - 1:
                move = input[state[0]][state[1] + 1]
                coordinates = (state[0], state[1] + 1)
                if move == 'E' and letter == 'z':
                    return moves_so_far + 1
                if ord(move) <= ord(letter) + 1 or letter == 'S':
                    if (underestimation(coordinates, moves_so_far + 1, E), coordinates, moves_so_far + 1) not in q.queue:
                        # print((underestimation(coordinates, moves_so_far + 1, E), coordinates, moves_so_far + 1))
                        q.put((underestimation(coordinates, moves_so_far + 1, E), coordinates, moves_so_far + 1))

def part2 (input):
    a_points = []
    min_a = len(input) * len(input[0])
    for l, line in enumerate(input):
        for p, point in enumerate(line):
            if point == 'a' or point == 'S':
                a_points += [(l, p)]
    # print(a_points)
    for a in a_points:
        distance = part1(input, a)
        if distance:
            if distance < min_a:
                min_a = distance
    return min_a


print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input)}")



t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")

# Part 1: 352
# Elapsed time: 0.0394983000005595