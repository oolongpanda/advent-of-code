from time import perf_counter

t1 = perf_counter()
with open('input/day15.txt') as f:
    input = [l.strip() for l in f.readlines()]

    
def parse(input):
    parsed = []
    for line in input:
        toadd = []
        number = ''
        numbers = False
        for character in line:
            if character == ',' or character == ':':
                numbers = False
                toadd += [int(number)]
                number = ''
            if numbers:
                number += character
            if character == '=':
                numbers = True
        toadd += [int(number)]
        parsed += [toadd]
    return (parsed)


def part1(input, y_line):
    input = parse(input)
    nobeacon = []
    beacons_on_line = set()
    for line in input:
        manhattan = abs(line[0] - line[2]) + abs(line[1] - line[3])
        if line[1] - manhattan <= y_line and y_line <= line[1] + manhattan:
            remaining_manhattan = manhattan - abs(line[1] - y_line)
            nobeacon += [(line[0] - remaining_manhattan, line[0] + remaining_manhattan)]
            if line[3] == y_line:
                beacons_on_line.add(line[2])
    plus = []
    minus = []
    for line in nobeacon:
        addplus = []
        addminus = []
        addplus += [line]
        for plusline in plus:
            if max(plusline[0], line[0]) <= min(plusline[1], line[1]):
                addminus += [(max(plusline[0], line[0]), min(plusline[1], line[1]))]
        for minusline in minus:
            if max(minusline[0], line[0]) <= min(minusline[1], line[1]):
                addplus += [(max(minusline[0], line[0]), min(minusline[1], line[1]))]
        plus += addplus
        minus += addminus
    sum = len(beacons_on_line) * -1
    for line in plus:
        sum += max(line) - min(line) + 1
    for line in minus:
        sum -= max(line) - min(line) + 1
    return sum



def part2(input, min, max):
    input = parse(input)
    for testline in input:
        manhattan = abs(testline[0] - testline[2]) + abs(testline[1] - testline[3])
        
        # x = +ve manhattan, y = 0 -> x = 0, y = +ve manhattan
        
        addx, addy = manhattan + 1, 0
        while addx >= 0:
            x = testline[0] + addx
            y = testline[1] + addy
            couldbe = True
            if x >= min and x <= max and y >= min and y <= max:
                for checkline in input:
                    checkmanhattan = abs(checkline[0] - checkline[2]) + abs(checkline[1] - checkline[3])
                    if abs(x - checkline[0]) + abs(y - checkline[1]) <= checkmanhattan:
                        couldbe = False
                        break
                if couldbe == True:
                    return (x * 4000000) + y
            addx -= 1
            addy += 1
        
        # x = -ve manhattan, y = 0 -> x = 0, y = -ve manhattan
        addx, addy = (manhattan + 1) * -1, 0
        while addx <= 0:
            x = testline[0] + addx
            y = testline[1] + addy
            couldbe = True
            if x >= min and x <= max and y >= min and y <= max:
                for checkline in input:
                    checkmanhattan = abs(checkline[0] - checkline[2]) + abs(checkline[1] - checkline[3])
                    if abs(x - checkline[0]) + abs(y - checkline[1]) <= checkmanhattan:
                        couldbe = False
                        break
                if couldbe == True:
                    return (x * 4000000) + y
            addx += 1
            addy -= 1

        # x = -ve manhattan, y = 0 -> x = 0, y = +ve manhattan
        addx, addy = (manhattan + 1) * -1, 0
        while addx <= 0:
            x = testline[0] + addx
            y = testline[1] + addy
            couldbe = True
            if x >= min and x <= max and y >= min and y <= max:
                for checkline in input:
                    checkmanhattan = abs(checkline[0] - checkline[2]) + abs(checkline[1] - checkline[3])
                    if abs(x - checkline[0]) + abs(y - checkline[1]) <= checkmanhattan:
                        couldbe = False
                        break
                if couldbe == True:
                    return (x * 4000000) + y
            addx += 1
            addy += 1

        # x = +ve manhattan, y = 0 -> x = 0, y = -ve manhattan
        addx, addy = manhattan + 1, 0
        while addx >= 0:
            x = testline[0] + addx
            y = testline[1] + addy
            couldbe = True
            if x >= min and x <= max and y >= min and y <= max:
                for checkline in input:
                    checkmanhattan = abs(checkline[0] - checkline[2]) + abs(checkline[1] - checkline[3])
                    if abs(x - checkline[0]) + abs(y - checkline[1]) <= checkmanhattan:
                        couldbe = False
                        break
                if couldbe == True:
                    return (x * 4000000) + y
            addx -= 1
            addy -= 1     
    return 'dude wtf'   


print(f"Part 1: {part1(input, 2000000)}")
print(f"Part 2: {part2(input, 0, 4000000)}")

t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")


# Part 1: 5564017
# Elapsed time: 0.0010253000000375323

# Part 1: 5564017
# Part 2: 11558423398893
# Elapsed time: 4.48901640000258