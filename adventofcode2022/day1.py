from time import perf_counter
t1 = perf_counter()
with open('input/day1.txt') as f:
    testinput = f.read()
    input = [[int(x) for x in l.split('\n')] for l in testinput.split('\n\n')]

def biggesttotals(input):
    mostcals = sorted(sum(l) for l in input)[-3:]
    return mostcals[-1], sum(mostcals)

print(f"Part 1: {biggesttotals(input)[0]}")
print(f"Part 2: {biggesttotals(input)[1]}")

t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")

# Part 1: 75622
# Part 2: 213159
# Elapsed time: 0.000873300014063715