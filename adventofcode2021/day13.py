with open('input/day13.txt') as f:
    input = [l.strip() for l in f.readlines()]

    crosses = []
    directions = []
    xvalues = []
    yvalues = []
    for line in input:
        if ',' in line:
            point = line.split(',')
            crosses += [[int(point[0]), int(point[1])]]
            xvalues += [int(point[0])]
            yvalues += [int(point[1])]
        if '=' in line:
            direction = line.split('=')
            if 'x' in line:
                directions += [['x', int(direction[1])]]
            if 'y' in line:
                directions += [['y', int(direction[1])]]
    maxx = max(xvalues) + 1
    maxy = max(yvalues) + 1
    paper = [[' '] * maxx for i in range (maxy)]
    for cross in crosses:
        paper[cross[1]][cross[0]] = '#'

    marks = None
    for direction in directions:
        if direction[0] == 'y':
            for l, line in enumerate(paper[direction[1]:len(paper)]):
                newpoint = direction[1] - l
                for p, point in enumerate(line):
                    if point == '#':
                        paper[newpoint][p] = '#'
            del paper[(direction[1]):]
        if direction[0] == 'x':
            for l, line in enumerate(paper):
                for p, point in enumerate(line[direction[1]:len(line)]):
                    newpoint = direction[1] - p
                    if point == '#':
                        paper[l][newpoint] = '#'
                del paper[l][(direction[1]):]
        if not marks:
            marks = 0
            for line in paper:
                for point in line:
                    if point == '#':
                        marks += 1
            
    print ('Task 1:', marks)
    print ('Task 2:')
    for line in paper:
        for point in line:
            print (point, end = '')
        print()

# Task 1: 684
# Task 2: JRZBLGKH
