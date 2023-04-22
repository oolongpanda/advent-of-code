from time import perf_counter
t1 = perf_counter()
with open('input/day3.txt') as f:
    input = [l.strip() for l in f.readlines()]

def priority(letter):
    priority = ord(letter)
    if priority <= ord('Z'):
        priority -= (ord('A') - 27)
    else:
        priority -= (ord('a') - 1)

    return priority

def parsehalves(input):
    parsed = []
    for rucksack in input:
        halfway = int(len(rucksack)/2)
        halfa = str(rucksack[:halfway])
        halfb = str(rucksack[halfway:])
        parsed += [[halfa, halfb]]
    return parsed

def part1 (input):
    input = parsehalves(input)
    totalpriority = 0
    for rucksack in input:
        
        # halfa = set(rucksack[0])
        # halfb = set(rucksack[1])
        # common = halfa & halfb
        # totalpriority += priority(next(iter(common)))

        for itemA in rucksack[0]:
            if itemA in rucksack[1]:
                totalpriority += priority(itemA)
                break

    return totalpriority

def part2 (input):
    badgetotal = 0
    for i in range(0, len(input), 3):
        set1 = set(input[i])
        set2 = set(input[i+1])
        set3 = set(input[i+2])
        common = set1 & set2 & set3
        if len(common) == 1:
            badgetotal += priority(next(iter(common)))
        else:
            print ('aaaah', common)
    return badgetotal

print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input)}")

t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")

# Part 1: 7428
# Part 2: 2650
# Elapsed time: 0.002270200056955218