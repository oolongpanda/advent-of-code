from time import perf_counter
t1 = perf_counter()
with open('input/day3.txt') as f:
    input = [l.strip() for l in f.readlines()]
    input = input[0]

    def delivery2(input, part):
        xy = [[0,0],[0,0]]
        realrobo = 0
        visited = {(0, 0):2}
        for arrow in input:
            x, y = xy[realrobo]
            if arrow == '^':
                y += 1
            elif arrow == 'v':
                y -=1
            elif arrow == '>':
                x += 1
            elif arrow == '<':
                x -= 1
            else:
                print('aaaghhh', arrow)
            if (x, y) in visited:
                visited[(x, y)] += 1
            else:
                visited.update({(x, y): 1})
            xy[realrobo] = [x, y]
            if part == 2:
                if realrobo == 0:
                    realrobo = 1
                else:
                    realrobo = 0
        return len(visited)
    
    
    print('Part 1:', delivery2(input, 1))
    print('Part 2:', delivery2(input, 2))

            
    
t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")

# Part 1: 2081
# Part 2: 2341
# Elapsed time: 0.00941629999988435