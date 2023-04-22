import hashlib
from time import perf_counter
t1 = perf_counter()
with open('input/day4.txt') as f:
    input = [l.strip() for l in f.readlines()][0]

    def findnumber(key, start, zeros):
        tocheck = ''
        numberadding = 0
        while True:
            tocheck = key + str(numberadding)
            result = hashlib.md5(tocheck.encode()).hexdigest()
            good = True
            for i in result[0:zeros]:
                if i != '0':
                    good = False
                    break
            if good:
                return numberadding
            numberadding += 1
    
    part1 = findnumber(input, 0, 5)
    print('Part 1:', part1)
    print('Part 2:', findnumber(input, part1, 6))

t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")

# Part 1: 254575
# Part 2: 1038736
# Elapsed time: 1.461205300001893