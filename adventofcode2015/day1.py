from time import perf_counter
t1 = perf_counter()

with open('input/day1.txt') as f:
    lines = f.readlines()
    line = lines[0]
    floor = 0
    part2 = 0
    hitbasement = False
    
    for i, instruction in enumerate(line):
        if instruction == '(':
            floor += 1
        if instruction == ')':
            floor -= 1
            if not hitbasement:
                if floor == -1:
                    hitbasement = True
                    part2 = i + 1

    print('Part 1:', floor)
    print('Part 2 ', part2)


t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")

# Part 1: 232
# Part 2  1783
# Elapsed time: 0.002428399999644170