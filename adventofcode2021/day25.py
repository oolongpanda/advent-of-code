from re import I
from time import perf_counter
t1_start = perf_counter()

with open("input/day25.txt") as f:
    input = [l.strip('\n') for l in f.readlines()]
    map = []
    for i in input:
        map += [list(str(i))]

    def pretty (map):
        print('\n')
        for row in map:
            line = ''
            for i in row:
                line += i
            print(line)

    def cucumbermove (map):
        anymove = False
        width = len(map[0])
        for r, row in enumerate(map): #east
            prevmove = False
            endmoved = False
            for s, spot in enumerate(row):
                if spot == '.' and map[r][s-1] == '>' and prevmove == False:
                    row[s] = '>'
                    if s == 0:
                        endmoved = True
                    else:
                        row[s-1] = '.'
                    prevmove = True
                    anymove = True
                else:
                    prevmove = False
            if endmoved:
                row[-1] = '.'
        
        for s in range(width):
            endmoved = False
            prevmove = False
            for r, row in enumerate(map): #south
                if row[s] == '.' and map[r-1][s] == 'v' and prevmove == False:
                    row[s] = 'v'
                    if r == 0:
                        endmoved = True
                    else:
                        map[r-1][s] = '.'
                    prevmove = True
                    anymove = True
                else:
                    prevmove = False
            if endmoved:
                map[-1][s] = '.'
        return map, anymove

    def bruteforce(map):
        move = 0
        while True:
            move += 1
            map, thisgo = cucumbermove(map)
            if thisgo == False:
                return move
            if move > 2000:
                return False
                

    print(f"Task 1: {bruteforce(map)}")

    # Task 1: 579
    # Elapsed time: 2.8637063

    t1_stop = perf_counter()
    print("Elapsed time:", t1_stop - t1_start