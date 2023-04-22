from time import perf_counter

t1 = perf_counter()
with open('input/day9.txt') as f:
    input = [l.split(' ') for l in f.read().split('\n')]


def tailmove(head, tail):
    if head[0] - tail[0] == 2:
        tail[0] += 1
        if head[1] > tail[1]:
            tail[1] += 1
        elif head[1] < tail[1]:
            tail[1] -= 1
    elif head[0] - tail[0] == -2:
        tail[0] -= 1
        if head[1] > tail[1]:
            tail[1] += 1
        elif head[1] < tail[1]:
            tail[1] -= 1
    elif head[1] - tail[1] == 2:
        tail[1] += 1
        if head[0] > tail[0]:
            tail[0] += 1
        elif head[0] < tail[0]:
            tail[0] -= 1
    elif head[1] - tail[1] == -2:
        tail[1] -= 1
        if head[0] > tail[0]:
            tail[0] += 1
        elif head[0] < tail[0]:
            tail[0] -= 1
    return tail

def part1 (input, knots):
    tailvisited = {(0,0)}
    head = [0,0]
    rope = []
    for _ in range(knots):
        rope += [[0,0]]
    
    for line in input:
        direction, distance = line[0], int(line[1])
        for _ in range(distance):
            if direction == 'R':
                head[0] += 1
            elif direction == 'L':
                head[0] -= 1
            elif direction == 'U':
                head[1] += 1
            elif direction == 'D':
                head[1] -= 1
            rope[0] = head

            for k, knot in enumerate(rope):
                if k > 0:
                    tail = tailmove(rope[k-1], knot)
                    rope[k] = tail
            tailvisited.add(tuple(i for i in tail))
    return len(tailvisited)



print(f"Part 1: {part1(input, 2)}")
print(f"Part 2: {part1(input, 10)}")




t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")

# Part 1: 5907
# Part 2: 2303
# Elapsed time: 0.0534820000175386