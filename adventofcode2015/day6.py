from time import perf_counter
t1 = perf_counter()
with open('input/day6.txt') as f:
    input = [l.strip().split(' ') for l in f.readlines()]
    for i in input:
        if i[0] == 'turn':
            i.pop(0)
        i.pop(2)
        a,b = i[1].split(',')
        i[1] = (int(a), int(b))
        a,b = i[2].split(',')
        i[2] = (int(a), int(b))
    
    def day6(input, part):
        line1 = []
        for i in range(1000):
            line1 += [0]
        grid1 = []
        for i in range(1000):
            grid1 += [line1.copy()]
        if part == 1:
            for i in input:
                if i[0] == 'on':
                    for x in range(i[1][0], i[2][0]+1):
                        for y in range(i[1][1], i[2][1]+1):
                            grid1[y][x] = 1
                elif i[0] == 'off':
                    for x in range(i[1][0], i[2][0]+1):
                        for y in range(i[1][1], i[2][1]+1):
                            grid1[y][x] = 0
                elif i[0] == 'toggle':
                    for x in range(i[1][0], i[2][0]+1):
                        for y in range(i[1][1], i[2][1]+1):
                            if grid1[y][x] == 1:
                                grid1[y][x] = 0
                            else:
                                grid1[y][x] = 1
                else:
                    print(i)
        if part == 2:
            for i in input:
                if i[0] == 'on':
                    for x in range(i[1][0], i[2][0]+1):
                        for y in range(i[1][1], i[2][1]+1):
                            grid1[y][x] += 1
                elif i[0] == 'off':
                    for x in range(i[1][0], i[2][0]+1):
                        for y in range(i[1][1], i[2][1]+1):
                            if grid1[y][x] > 0:
                                grid1[y][x] -= 1
                elif i[0] == 'toggle':
                    for x in range(i[1][0], i[2][0]+1):
                        for y in range(i[1][1], i[2][1]+1):
                            grid1[y][x] += 2
                else:
                    print(i)
                
        on = 0
        for line in grid1:
            for light in line:
                on += light
        return on
    
    def part(input):
        return 0


    print(f"Part 1: {day6(input, 1)}")
    print(f"Part 2: {day6(input, 2)}")

# Part 1: 400410
# Part 2: 15343601
# Elapsed time: 3.1238328999606892

t2 = perf_counter()
print(f"Elapsed time: {t2-t1}"