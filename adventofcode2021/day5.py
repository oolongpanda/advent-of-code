with open('input/day5.txt') as f:
    input = [l.strip() for l in f.readlines()]



    read = []
    for current in input:
        xy = current.split(' -> ')
        xy = [xy[0].split(','), xy[1].split(',')]
        read = read + [xy]
            

    coordinates = [[0] * 1000 for i in range (1000)]
    for line in read:
        if line[0][0] == line[1][0]:
            x1 = int(line[0][0])
            y1 = int(line[0][1])
            y2 = int(line[1][1])
            diff = y1-y2
            if diff > 0:
                while diff >= 0:
                    coordinates[x1][y2 + diff] += 1
                    diff -= 1
            else:
                while diff <= 0:
                    coordinates[x1][y2 + diff] += 1
                    diff += 1
        elif line[0][1] == line[1][1]:
            y1 = int(line[0][1])
            x1 = int(line[0][0])
            x2 = int(line[1][0])
            diff = x1-x2
            coordinates[x2][y1] += 1
            if diff > 0:
                while diff != 0:
                    coordinates[x2 + diff][y1] += 1
                    diff -= 1
            if diff < 0:
                while diff != 0:
                    coordinates[x2 + diff][y1] += 1
                    diff += 1
    allcoordinates = []
    for line in coordinates:
        allcoordinates += line

    print ('Task 1:', len([i for i in allcoordinates if i>1]))


    coordinates = [[0] * 1000 for i in range (1000)]
    for line in read:
        if line[0][0] == line[1][0]:
            x1 = int(line[0][0])
            y1 = int(line[0][1])
            y2 = int(line[1][1])
            diff = y1-y2
            coordinates[x1][y2] +=  1
            if diff > 0:
                while diff != 0:
                    coordinates[x1][y2 + diff] += 1
                    diff -= 1
            if diff < 0:
                while diff != 0:
                    coordinates[x1][y2 + diff] += 1
                    diff += 1
        if line[0][1] == line[1][1]:
            y1 = int(line[0][1])
            x1 = int(line[0][0])
            x2 = int(line[1][0])
            diff = x1-x2
            coordinates[x2][y1] += 1
            if diff > 0:
                while diff != 0:
                    coordinates[x2 + diff][y1] += 1
                    diff -= 1
            if diff < 0:
                while diff != 0:
                    coordinates[x2 + diff][y1] += 1
                    diff += 1
        else:
            y1 = int(line[0][1])
            y2 = int(line[1][1])
            x1 = int(line[0][0])
            x2 = int(line[1][0])
            xdiff = x1 - x2
            ydiff = y1 - y2
            if xdiff == ydiff or -xdiff == ydiff:
                coordinates[x2][y2] += 1
                if xdiff > 0 and ydiff > 0:
                    while xdiff != 0:
                        coordinates[x2 + xdiff][y2 + ydiff] += 1
                        xdiff -= 1
                        ydiff -= 1
                if xdiff < 0 and ydiff > 0:
                    while xdiff != 0:
                        coordinates[x2 + xdiff][y2 + ydiff] += 1
                        xdiff += 1
                        ydiff -= 1
                if xdiff > 0 and ydiff < 0:
                    while xdiff != 0:
                        coordinates[x2 + xdiff][y2 + ydiff] += 1
                        xdiff -= 1
                        ydiff += 1
                if xdiff < 0 and ydiff < 0:
                    while xdiff != 0:
                        coordinates[x2 + xdiff][y2 + ydiff] += 1
                        xdiff += 1
                        ydiff += 1
                

    allcoordinates = []
    for line in coordinates:
        allcoordinates += line
    print ('Task 2:', len([i for i in allcoordinates if i>1]))

