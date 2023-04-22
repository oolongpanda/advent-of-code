with open('input/day15.txt') as f:
    input = [l.strip() for l in f.readlines()]
    
    allsum = 0
    for row in input:
        for point in row:
            allsum += int(point)

    map = [[]]
    for r, row in enumerate(input):
        if r > 0:
            map += [[]]
        for point in row:
            map[r] += [[int(point), int(allsum)]]
    maxy = len(map) - 1
    maxx = len(map[0]) - 1
    tocheck = [[0,0]]
    map[0][0] = [0, 0]
    
    # IT GOES [ROW][COL]
    while len(tocheck) != 0:
        row = tocheck[0][0]
        col = tocheck[0][1]
        #up
        if row != 0:
            if map[row - 1][col][1] > map[row][col][1] + map[row - 1][col][0]:
                map[row - 1][col][1] = map[row][col][1] + map[row - 1][col][0]
                tocheck += [[row - 1, col]]
        #down
        if row != maxy:
            if map[row + 1][col][1] > map[row][col][1] + map[row + 1][col][0]:
                map[row + 1][col][1] = map[row][col][1] + map[row + 1][col][0]
                tocheck += [[row + 1, col]]
        #left
        if col != 0:
            if map[row][col - 1][1] > map[row][col][1] + map[row][col - 1][0]:
                map[row][col - 1][1] = map[row][col][1] + map[row][col - 1][0]
                tocheck += [[row, col - 1]]
        #right
        if col != maxx:
            if map[row][col + 1][1] > map[row][col][1] + map[row][col + 1][0]:
                map[row][col + 1][1] = map[row][col][1] + map[row][col + 1][0]
                tocheck += [[row, col + 1]]
        tocheck.pop(0)

    print ('Task 1:', map[maxy][maxx][1])
 
    biggerinput = []
    start = input[0]
    for i in range(5):
        for row in input:
            line = []
            for j in range (5):
                for point in row:
                    newpoint = int(point) + i + j
                    while newpoint > 9:
                        newpoint -= 9
                    line.append(str(newpoint))
            biggerinput.append(line)

    allsum = 0
    for row in biggerinput:
        for point in row:
            allsum += int(point)

    map = [[]]
    for r, row in enumerate(biggerinput):
        if r > 0:
            map += [[]]
        for point in row:
            map[r] += [[int(point), int(allsum)]]
    maxy = len(map) - 1
    maxx = len(map[0]) - 1
    tocheck = [[0,0]]
    map[0][0] = [0, 0]
    
    # IT GOES [ROW][COL]
    while len(tocheck) != 0:
        row = tocheck[0][0]
        col = tocheck[0][1]
        #up
        if row != 0:
            if map[row - 1][col][1] > map[row][col][1] + map[row - 1][col][0]:
                map[row - 1][col][1] = map[row][col][1] + map[row - 1][col][0]
                tocheck += [[row - 1, col]]
        #down
        if row != maxy:
            if map[row + 1][col][1] > map[row][col][1] + map[row + 1][col][0]:
                map[row + 1][col][1] = map[row][col][1] + map[row + 1][col][0]
                tocheck += [[row + 1, col]]
        #left
        if col != 0:
            if map[row][col - 1][1] > map[row][col][1] + map[row][col - 1][0]:
                map[row][col - 1][1] = map[row][col][1] + map[row][col - 1][0]
                tocheck += [[row, col - 1]]
        #right
        if col != maxx:
            if map[row][col + 1][1] > map[row][col][1] + map[row][col + 1][0]:
                map[row][col + 1][1] = map[row][col][1] + map[row][col + 1][0]
                tocheck += [[row, col + 1]]
        tocheck.pop(0)

    print ('Task 2:', map[maxy][maxx][1])

# Task 1: 656
# Task 2: 297