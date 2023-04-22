with open('input/day9.txt') as f:
    input = [l.strip() for l in f.readlines()]
    
    riskscore = 0
    lowpoints = []
    for l, line in enumerate(input):
        for n, number in enumerate(line):
            if number < line[n - 1] or n == 0:
                if n == len(line) - 1 or number < line [n + 1]:
                    if number < input[l - 1][n] or l == 0:
                        if l == len(input) - 1 or number < input[l + 1][n]:
                            riskscore  += int(number) + 1
                            lowpoints += [[int(l), int(n)]]
    
    print ('Task 1:', riskscore)
    basinsizes = []
    for lowpoint in lowpoints:
        basin = [lowpoint]
        oldnewpoints = [lowpoint]
        newpoints = []
        stopped = False
        while not stopped:
            for point in oldnewpoints:
                # Down
                if int(point[0]) != len(input) - 1 and int(input[point[0] + 1][point[1]]) != 9:
                    if [int(point[0] + 1), int(point[1])] not in newpoints and [int(point[0] + 1), int(point[1])] not in basin:
                        newpoints += [[int(point[0] + 1), int(point[1])]]
                # Up
                if point[0] != 0 and int(input[point[0] - 1][point[1]]) != 9:
                    if [int(point[0] - 1), int(point[1])] not in newpoints and [int(point[0] - 1), int(point[1])] not in basin:
                        newpoints += [[int(point[0] - 1), int(point[1])]]
                # Right
                if point[1] != len(input[0]) - 1 and int(input[point[0]][point[1] + 1]) != 9:
                    if [int(point[0]), int(point[1] + 1)] not in newpoints and [int(point[0]), int(point[1] + 1)] not in basin:
                        newpoints += [[int(point[0]), int(point[1] + 1)]]
                # Left
                if point[1] != 0 and int(input[point[0]][point[1] - 1]) != 9:
                    if [int(point[0]), int(point[1] - 1)] not in newpoints and [int(point[0]), int(point[1] - 1)] not in basin:
                        newpoints += [[int(point[0]), int(point[1] - 1)]]
            basin += newpoints
            oldnewpoints = [i for i in newpoints]
            if len(newpoints) == 0:
                stopped = True
            newpoints = []
        basinsizes += [len(basin)]

    bigbasins = 1
    for i in range(3):
        bigbasins *= max(basinsizes)
        basinsizes.remove(max(basinsizes))
    print ('Task 2:', bigbasins