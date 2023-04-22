from time import perf_counter

t1 = perf_counter()
with open("input/day4.txt") as f:
    input = [
        [[int(x) for x in y.split("-")] for y in l.split(",")]
        for l in f.read().split("\n")
    ]


def part1(input):
    fulloverlaps = 0
    anyoverlaps = 0
    for pair in input:
        a1, a2 = pair[0][0], pair[0][1]
        b1, b2 = pair[1][0], pair[1][1]
        elfa = {i for i in range(a1, a2 + 1)}
        elfb = {i for i in range(b1, b2 + 1)}
        if elfa.issubset(elfb) or elfb.issubset(elfa):
            fulloverlaps += 1
        if elfa.intersection(elfb):
            anyoverlaps += 1

    return fulloverlaps, anyoverlaps


def main(input):
    answer = part1(input)
    print(f"Part 1: {answer[0]}")
    print(f"Part 2: {answer[1]}")


main(input)

t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")

# Part 1: 518
# Part 2: 909
# Elapsed time: 0.007967200130224228
