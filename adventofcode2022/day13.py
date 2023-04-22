from time import perf_counter

t1 = perf_counter()
with open('input/day13.txt') as f:
    input = [l.strip() for l in f.readlines()]

def parseline(line, recursion=False):
    point = 1
    item = ''
    parsed = []
    while point < len(line):
        if line[point] == '[':
            item, moved = parseline(line[point:], True)
            point += moved
        elif line[point] == ']':
            if type(item) is str:
                if item != '':
                    parsed += [int(item)]
            elif type(item) is list:
                parsed += [item]
            else:
                raise Exception(f"Item: {item}. Type: {type(item)}")
            item = ''
            if recursion:
                return parsed, point
            else:
                return parsed
        elif line[point] == ',':
            if type(item) is str:
                if item != '':
                    parsed += [int(item)]
            elif type(item) is list:
                parsed += [item]
            else:
                raise Exception(f"Item: {item}. Type: {type(item)}")
            item = ''
        else:
            item += line[point]
        point += 1

def compare(left, right):
    if type(left) == str:
        if left[0] == '[':
            left = parseline(left)
            right = parseline(right)
    for item in range(min(len(left), len(right))):
        leftitem = left[item]
        rightitem = right[item]
        if type(leftitem) is int and type(rightitem) is int:
            if leftitem > rightitem:
                return False
            elif leftitem < rightitem:
                return True
        else:
            if type(leftitem) is int:
                leftitem = [leftitem]
            elif type(rightitem) is int:
                rightitem = [rightitem]
            if compare(leftitem, rightitem) is not None:
                return compare(leftitem, rightitem)
    if len(left) > len(right):
        return False
    elif len(left) < len(right):
        return True

def part1 (input):
    sum = 0
    for l, line in enumerate(range(0, len(input), 3)):
        if compare(input[line], input[line + 1]):
            sum += l + 1
    return sum

def part2 (input):
    ordered = [
        [[2]],
        [[6]],
        ]
    for line in input:
        if line != '':
            line = parseline(line)
            for p, packet in enumerate(ordered):
                if compare(line, packet):
                    ordered.insert(p, line)
                    break
                if p == len(ordered) - 1:
                    ordered += [line]
                    break
                pass
    key = 1
    for l, line in enumerate(ordered):
        if line == [[2]] or line == [[6]]:
            key *= l + 1
    return key


print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input)}")

t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")

# Part 1: 5760
# Part 2: 26670
# Elapsed time: 0.078309300000000