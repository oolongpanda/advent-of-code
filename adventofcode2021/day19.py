with open('input/day19.txt') as f:
    input = [l.strip() for l in f.readlines()]

    scanner = -1
    beacons = []
    newscanner = False
    for i in input:
        # print(i)
        if i == '':
            newscanner = False
        if newscanner == True:
            stringstoadd = i.split(',')
            intstoadd = []
            for s in stringstoadd:
                intstoadd += [int(s)]
            beacons[scanner] += [intstoadd]
        if i != '':
            if i[4] == 's':
                newscanner = True
                scanner += 1
                beacons += [[]]

    def rotate(point, axis, turns):
        x = point[0]
        y = point[1]
        z = point[2]
        for i in range(turns):
            if axis == 'x':
                x, y, z = x, z, -y
            elif axis == 'y':
                x, y, z = z, y, -x
            elif axis == 'z':
                x, y, z = -y, x, z
            else:
                return 0
        return[x, y, z]
    
    def brotations(point1):
        list = []
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    newpoint = rotate(point1, 'x', x)
                    newpoint = rotate(newpoint, 'y', y)
                    newpoint = rotate(newpoint, 'z', z)
                    if newpoint not in list:
                        list += [newpoint]
        return list
    
    def scannerrotations(scanner):
        list = []
        for i in range(24):
            list += [[]]
        for beacon in scanner:
            currentbeacons = brotations(beacon)
            for r, rotation in enumerate(currentbeacons):
                list[r] += [rotation]
        return list
    

    relativetosanner0 = beacons[0]
    toadd = beacons[1:]
    scannerpositions = [[0,0,0]]



    while len(toadd) > 0:
        rotations  = scannerrotations(toadd[0])
        rotationfound = False
        for r in rotations:
            if not rotationfound:
                distances = {}
                for p, point in enumerate(r):
                    for beacon in relativetosanner0:
                        diff = (beacon[0]-point[0], beacon[1]-point[1], beacon[2]-point[2])
                        if diff in distances:
                            distances[diff] += 1
                        if diff not in distances:
                            distances.update({diff:1})
            diffs = [k for k, count in distances.items() if count >= 12]
            if len(diffs) == 1:
                diff = diffs[0]
                rotationfound = True
                scannerpositions += [diff]
                for point in r:
                    newpoint = [point[0] + diff[0], point[1] + diff[1], point[2] + diff[2]]
                    if newpoint not in relativetosanner0:
                        relativetosanner0 += [newpoint]
                break
        if not rotationfound:
            prevbeacon = toadd[0]
            toadd += [prevbeacon]
        toadd.pop(0)

    print('Task 1:', len(relativetosanner0))

    biggestmanhattan = 0
    for s1 in scannerpositions:
        for s2 in scannerpositions:
            manhattan = abs(s1[0] - s2[0]) + abs(s1[1] - s2[1]) + abs(s1[2] - s2[2])
            if manhattan > biggestmanhattan:
                biggestmanhattan = manhattan
    
    print('Task 2:', biggestmanhattan)

    # Task 1: 496
    # Task 2: 14478
