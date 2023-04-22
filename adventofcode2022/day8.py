from time import perf_counter

t1 = perf_counter()
with open("input/day8.txt") as f:
    input = [[[int(i), " "] for i in list(l)] for l in f.read().split("\n")]


def part1(input):
    seen_trees = 0
    for line in input:
        left_block = -1
        for point in line:
            if point[0] > left_block:
                if point[1] == " ":
                    seen_trees += 1
                point[1] = "N"
                left_block = point[0]
    for line in input:
        right_block = -1
        for point in reversed(line):
            if point[0] > right_block:
                if point[1] == " ":
                    seen_trees += 1
                point[1] = "N"
                right_block = point[0]
    for column in range(len(input[0])):
        above_block = -1
        for point in range(len(input)):
            if input[point][column][0] > above_block:
                if input[point][column][1] == " ":
                    seen_trees += 1
                input[point][column][1] = "N"
                above_block = input[point][column][0]
    for column in range(len(input[0])):
        below_block = -1
        for point in range(len(input) - 1, -1, -1):
            if input[point][column][0] > below_block:
                if input[point][column][1] == " ":
                    seen_trees += 1
                input[point][column][1] = "N"
                below_block = input[point][column][0]
    return seen_trees


def part2(input):
    for line in input:
        for point in line:
            point[1] = []
    for l, line in enumerate(input):
        for p, point in enumerate(line):
            if l == 0 or p == 0 or l == len(input) - 1 or p == len(line) - 1:
                point[1] = [0]
            else:
                distance = 0
                while p - distance - 1 >= 0:
                    distance += 1
                    if input[l][p - distance][0] >= point[0]:
                        break
                point[1] += [distance]

                distance = 0
                while p + distance + 1 < len(line):
                    distance += 1
                    if input[l][p + distance][0] >= point[0]:
                        break
                point[1] += [distance]

                distance = 0
                while l - distance - 1 >= 0:
                    distance += 1
                    if input[l - distance][p][0] >= point[0]:
                        break
                point[1] += [distance]

                distance = 0
                while l + distance + 1 < len(input):
                    distance += 1
                    if input[l + distance][p][0] >= point[0]:
                        break
                point[1] += [distance]

    highest_scenic = 0
    for line in input:
        for point in line:
            scenic = 1
            for i in point[1]:
                scenic *= i
            if scenic > highest_scenic:
                highest_scenic = scenic
    return highest_scenic


print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input)}")


t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")

# Part 1: 1785
# Part 2: 345168
# Elapsed time: 0.03580750012770295
