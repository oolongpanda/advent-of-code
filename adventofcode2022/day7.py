from time import perf_counter
t1 = perf_counter()
with open('input/day7.txt') as f:
    input = [l.split(' ') for l in f.read().split('\n')]

def wtf(terminal):
    directory = {('/',): 0}
    filepath = ['/']
    for line in terminal:
        if line[0] == '$':
            if line[1] == 'cd':
                listing = False
                if line[2] == '/':
                    filepath = ['/']
                elif line[2] == '..':
                    filepath.pop(-1)
                else:
                    filepath += [line[2]]
            elif line[1] == 'ls':
                listing = True
            else:
                raise Exception('$ but not cd or ls')
        elif listing:
            if line[0] == 'dir':
                filepath += [line[1]]
                directory.update({tuple(filepath): 0})
                filepath.pop(-1)
            else:
                size = int(line[0])
                upthepath = filepath.copy()
                while len(upthepath) != 0:
                    directory[tuple(upthepath)] += size
                    upthepath.pop(-1)
    return(directory)

def part1 (input):
    directory = wtf(input)
    sum = 0
    for file in directory:
        if directory[file] <= 100000:
            sum += directory[file]
    return sum

def part2 (input, total, needed):
    directory = wtf(input)
    sizes = []
    for file in directory:
        sizes += [directory[file]]
    sizes.sort()
    space = total - sizes[-1]
    for file in sizes:
        if file + space >= needed:
            return file
    raise Exception('No big enough file')


print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input, 70000000, 30000000)}")


t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")

# Part 1: 1348005
# Part 2: 12785886
# Elapsed time: 0.002752800006419420