from time import perf_counter

t1 = perf_counter()
with open('input/day17.txt') as f:
    input = [l.strip() for l in f.readlines()][0]

rocks = [
    [(0, 0), (0, 0), (0, 0), (0, 0)],
    [(1, 1), (0, 2), (1, 1)], 
    [(0, 0), (0, 0), (0, 2)], 
    [(0, 3)], 
    [(0, 1), (0, 1)]
]

def visualisetower(tower):
    height = 0
    for column in tower:
        if max(column) > height:
            height = max(column)
    height += 1
    while height > 0:
        layer = '|'
        for column in tower:
            if height in column:
                layer += '#'
            else:
                layer += '.'
        layer += '|'
        print(layer)
        height -= 1
    base = '+'
    for _ in range(len(tower)):
        base += '-'
    base += '+'
    print(base)
        


def rockfall (jetseq, width, amount, pt2baseline = False):
    tower = []
    for _ in range(width):
        tower += [{0}]
    jet = 0
    rock = 0
    towerheight = 0
    increase = []

    scale = len(rocks) * len(jetseq) // 4

    for step in range(amount):
        falling = []
        settled = False
        minrock = towerheight + 4
        for c, col in enumerate(rocks[rock]):
            falling += [[c + 2, minrock + col[0], minrock + col[1]]]
        while not settled:
            if jetseq[jet] == '<':
                if falling[0][0] != 0:
                    if minrock > towerheight:
                        for col in falling:
                            col[0] -= 1
                    else:
                        crash = False
                        for col in falling:
                            if not crash:
                                for i in range(col[1], col[2] + 1):
                                    if i in tower[col[0] - 1]:
                                        crash = True
                                        break
                        if not crash:
                            for col in falling:
                                col[0] -= 1

            elif jetseq[jet] == '>':
                if falling[-1][0] != width - 1:
                    if minrock > towerheight:
                        for col in falling:
                            col[0] += 1
                    else:
                        crash = False
                        for col in falling:
                            if not crash:
                                for i in range(col[1], col[2] + 1):
                                    if i in tower[col[0] + 1]:
                                        crash = True
                                        break
                        if not crash:
                            for col in falling:
                                col[0] += 1
            else:
                raise Exception(f"Jet = {jet} = {jetseq[jet]}")
            jet = (jet + 1) % len(jetseq)

            if minrock - 1 <= towerheight:
                for col in falling:
                    if col[1] - 1 in tower[col[0]]:
                        settled = True
                        oldheight = towerheight
                        for c in falling:
                            for i in range(c[1], c[2] + 1):
                                tower[c[0]].add(i)
                            if c[2] > towerheight:
                                towerheight = c[2]
                        increase += [towerheight - oldheight]

                        if step == scale:
                            basetower = []
                            for stack in tower:
                                basetower += [stack]

                        break
                        
            if not settled:
                for col in falling:
                    col[1] -= 1
                    col[2] -= 1
                minrock -= 1
        rock = (rock + 1) % len(rocks)

    if pt2baseline:
        increasestring = ''.join(str(i) for i in increase)
        for rptlength in range(10, scale, 5):
            teststring = increasestring[scale:scale + rptlength]
            if 5*teststring in increasestring:
                rpt_increases = increase[scale:scale + rptlength]
                return rpt_increases

    return towerheight

def part2 (jetseq, width, amount):
    baselen = len(rocks) * len(jetseq) // 4
    rpt_increases = rockfall(jetseq, width, 6*baselen, True)
    rpt_height = 0
    for h in rpt_increases:
        rpt_height += h
    repeats = (amount - baselen)//len(rpt_increases)
    bigbaseheight = rockfall(jetseq, width, amount - (repeats*len(rpt_increases)))

    return bigbaseheight + repeats*rpt_height



print(f"Part 1: {rockfall(input, 7, 2022)}")
print(f"Part 2: {part2(input, 7, 1000000000000)}")

t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")

# Part 1: 3130
# Elapsed time: 0.011116699999547563

# Part 1: 3130
# Part 2: 1556521739139
# Elapsed time: 0.492911300003470