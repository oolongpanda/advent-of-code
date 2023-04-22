from time import perf_counter
import copy

t1 = perf_counter()
with open('input/day10.txt') as f:
    part1input = [l.split(' ') for l in f.read().split('\n')]
    part2input = copy.deepcopy(part1input)

def part1(input):
    for l, line in enumerate(input):
        if line[0] == 'addx':
            v = int(line[1])
            input.insert(l+1, ['add', v])
    x = 1
    signal = 0
    for cycle, line in enumerate(input):
        if line[0] == 'add':
            x += line[1]
        if (cycle + 22)%40 == 0:
            signal += x * (cycle + 2)
    return signal

def part2(input):
    for l, line in enumerate(input):
        if line[0] == 'addx':
            v = int(line[1])
            input.insert(l+1, ['add', v])
    x = 1
    crt_line = -1
    crt = []
    for _ in range(6):
        crt += ['']
    for cycle, line in enumerate(input):
        if (cycle)%40 == 0:
            crt_line += 1
        if (cycle)%40 in [x-1, x, x+1]:
            # crt[crt_line] += '██'
            crt[crt_line] += '##'
        else:
            crt[crt_line] += '  '
        if line[0] == 'add':
            x += line[1]
    return crt


print(f"Part 1: {part1(part1input)}")
print('Part 2:')
for line in part2(part2input):
    print(line)


t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")

# Part 1: 14320
# Part 2:
# ██████      ████    ██████    ██████    ██    ██    ████    ██████        ████
# ██    ██  ██    ██  ██    ██  ██    ██  ██  ██    ██    ██  ██    ██        ██
# ██    ██  ██        ██    ██  ██████    ████      ██    ██  ██    ██        ██
# ██████    ██        ██████    ██    ██  ██  ██    ████████  ██████          ██
# ██        ██    ██  ██        ██    ██  ██  ██    ██    ██  ██        ██    ██
# ██          ████    ██        ██████    ██    ██  ██    ██  ██          ████
# Elapsed time: 0.00372359994798898