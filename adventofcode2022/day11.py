from time import perf_counter
import re
import copy

t1 = perf_counter()
with open('input/day11.txt') as f:
    part1input = [l.split('\n') for l in f.read().split('\n\n')]
    part2input = copy.deepcopy(part1input)


def parse(input):
    monkies = []
    for monkey in input:
        monkey[1] = re.split(': |, ', monkey[1])
        itemlist = []
        for item in monkey[1][1:]:
            itemlist += [int(item)]
        # print(itemlist)
        monkey[2] = re.split(' ', monkey[2])
        operation = [monkey[2][-2], monkey[2][-1]]
        # print(operation)
        monkey[3] = re.split(' ', monkey[3])
        test = [int(monkey[3][-1]), int(monkey[4][-1]), int(monkey[5][-1])]
        # print(test)
        monkies += [[itemlist, operation, test]]
    return monkies

# [79, 98]      items held
# ['*', '19']   operation
# [23, 2, 3]    test, true, false


def part1(input, rounds, three):
    monkies = parse(input)
    # print(monkies)
    inspections = []
    for _ in monkies:
        inspections += [0]
    if not three:
        divisor = 1
        for monkey in monkies:
            divisor *= monkey[2][0]
    for _ in range(rounds):
        for m, monkey in enumerate(monkies):
            for _ in range(len(monkey[0])):
                inspections[m] += 1
                item = monkey[0][0]
                monkey[0].pop(0)
                if monkey[1][1] == 'old':
                    operate = item
                else:
                    operate = int(monkey[1][1])
                if monkey[1][0] == '+':
                    item += operate
                elif monkey[1][0] == '*':
                    item *= operate
                else:
                    raise Exception('not * or +')
                if three:
                    item //= 3
                else:
                    item = item%divisor
                if item%monkey[2][0] == 0:
                    monkies[monkey[2][1]][0] += [item]
                else:
                    monkies[monkey[2][2]][0] += [item]
    inspections.sort()
    monkeybusiness = inspections[-1] * inspections[-2]
    return monkeybusiness

print(f"Part 1: {part1(part1input, 20, True)}")
print(f"Part 2: {part1(part2input, 10000, False)}")
# 452226

t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")

# Part 1: 111210
# Elapsed time: 0.002553800120949745

# Part 1: 111210
# Part 2: 15447387620
# Elapsed time: 0.374031799845397