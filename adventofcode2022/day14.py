from time import perf_counter

t1 = perf_counter()
with open("input/day14.txt") as f:
    input = [
        [[int(x) for x in y.split(",")] for y in l.split(" -> ")]
        for l in f.read().split("\n")
    ]


def rockmodel(input):
    rocks = {}
    maxpoint = 0
    for line in input:
        for p, point in enumerate(line[:-1]):
            a = min(point, line[p + 1])
            b = max(point, line[p + 1])
            if b[1] > maxpoint:
                maxpoint = b[1]
            for x in range(a[0], b[0] + 1):
                for y in range(a[1], b[1] + 1):
                    if x in rocks:
                        if y not in rocks[x]:
                            rocks[x] += [y]
                    else:
                        rocks.update({x: [y]})
    for rock in rocks:
        rocks[rock].sort()
    return rocks, maxpoint + 2


def sandstep(x, y, rocks):
    if y > rocks[x][-1]:
        return "falling", (x, y)
        # you fall below the rocks to your eternal doom
    for s, central_y in enumerate(rocks[x]):
        if y < central_y:
            y = central_y - 1
            break
    if x - 1 in rocks:
        if central_y not in rocks[x - 1]:
            x = x - 1
            y = central_y
            return sandstep(x, y, rocks)
        else:
            if x + 1 in rocks:
                if central_y not in rocks[x + 1]:
                    x = x + 1
                    y = central_y
                    return sandstep(x, y, rocks)
                else:
                    rocks[x].insert(s, y)
                    return "settled", rocks
                    # 'tis settled
            else:
                return "falling", (x, y)
                # you fall right to your eternal doom
    else:
        return "falling", (x, y)
        # you fall left to your eternal doom


def main(input, part):
    rocks, floor = rockmodel(input)
    settled = 0
    finished = False
    if part == 1:
        while not finished:  # for the whole cascade
            outcome = sandstep(500, 0, rocks)
            if outcome[0] == "settled":
                settled += 1
                rocks = outcome[1]
            if outcome[0] == "falling":
                finished = True
    elif part == 2:
        while not finished:
            outcome = sandstep(500, 0, rocks)
            if outcome[0] == "settled":
                settled += 1
                rocks = outcome[1]
                if rocks[500][0] == 0:
                    finished = True
            if outcome[0] == "falling":
                x = outcome[1][0]
                for i in range(x - 1, x + 2):
                    if i in rocks:
                        if rocks[i][-1] < floor:
                            rocks[i] += [floor]
                    else:
                        rocks.update({i: [floor]})
    return settled


print(f"Part 1: {main(input, 1)}")
print(f"Part 2: {main(input, 2)}")


t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")


# Part 1: 825
# Part 2: 26729
# Elapsed time: 1.308971000005840