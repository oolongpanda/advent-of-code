from time import perf_counter
t1 = perf_counter()
with open('input/day5.txt') as f:
    input = f.read().split("\n\n")
start, instructions = input[0].split('\n'), input[1].split('\n')

def parsestart(start):
    no_stacks = (int((len(start[-1]) + 1)/4))
    stacks = [[] for _ in range(no_stacks)]
    for line in start[:-1]:
        for stack in range(no_stacks):
            item = line[4*stack + 1]
            if item != ' ':
                stacks[stack].insert(0,item)
    return stacks

def parseinstructions(instructions):
    parsed = []
    for instruction in instructions:
        broken = instruction.split(' ')
        parsed += [[int(broken[1]), int(broken[3]), int(broken[5])]]
    return(parsed)


def part1(start, instructions):
    crates = parsestart(start)
    instructions = parseinstructions(instructions)
    for instruction in instructions:
        for _ in range(instruction[0]):
            item = crates[instruction[1] - 1][-1]
            crates[instruction[1] - 1].pop(-1)
            crates[instruction[2] - 1] += item
    topstr = ''
    for stack in crates:
        topstr += stack[-1]
    return topstr

def part2 (start, instructions):
    crates = parsestart(start)
    instructions = parseinstructions(instructions)
    for instruction in instructions:

        amount, a, b = instruction[0], instruction[1]-1, instruction[2]-1
        items = crates[a][amount*-1:]
        crates[b] += items
        crates[a] = crates[a][:len(crates[a])-amount]
    topstr = ''
    for stack in crates:
        topstr += stack[-1]
    return topstr



print(f"Part 1: {part1(start, instructions)}")
print(f"Part 2: {part2(start, instructions)}")

t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")

# Part 1: TLFGBZHCN
# Part 2: QRQFHFWCL
# Elapsed time: 0.00247210008092224