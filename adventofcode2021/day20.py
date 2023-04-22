with open('input/day20.txt') as f:
    input = [l.strip() for l in f.readlines()]
    algorithm = input[0]
    image = input[2:]
    # algodict = {}
    # for v, value in enumerate(algorithm):
    #     algodict.update({v: value})


    def addedge(input, infinite):
        width = len(input[0])+6
        height = len(input)+6
        newgrid = []
        for i in range(height):
            newgrid += [[infinite]*width]
        for r, row in enumerate(input):
            for p, point in enumerate(row):
                newgrid[r+3][p+3] = point
        return newgrid
    
    def removeedge (grid):
        width = len(grid[0])-2
        height = len(grid)-2
        newgrid = []
        for i in range(height):
            newgrid += [['x']*width]
        for r, row in enumerate(grid):
            if r != 0 and r <= height:
                for p, point in enumerate(row):
                    if p != 0 and p <= width:
                        newgrid[r-1][p-1] = point
        return newgrid
    
    def ninesquare (y,x):
        coordinates = []
        for a in range (y-1, y+2):
            for b in range (x-1, x+2):
                coordinates.append([a,b])
        # print(coordinates)
        return(coordinates)


    def enhancement (grid, algorithm, times, infinite):
        grid = addedge(grid, infinite)
        height = len(grid)
        width = len(grid[0])
        newgrid = []
        for i in range(height):
            newgrid += [[infinite]*width]
        for y in range(1, height-1):
            for x in range(1, width-1):
                check = ninesquare(y,x)
                number = 0
                for point in check:
                    number *= 2
                    if grid[point[0]][point[1]] == '#':
                        number += 1
                newgrid[y][x] = algorithm[number]
        newgrid = removeedge(newgrid)
        if times > 1:
            outer = newgrid[0][0]
            newgrid = enhancement(newgrid, algorithm, times-1, outer)[0]
        outer = newgrid[0][0]
        if outer == '#':
            litcount = 'infinite'
        elif outer == '.':
            litcount = 0
            for row in newgrid:
                for point in row:
                    if point == '#':
                        litcount += 1
        else:
            print('reee edges')
        return newgrid, litcount
    
    print('Task 1:', enhancement(image, algorithm, 2, '.')[1])
    print('Task 2:', enhancement(image, algorithm, 50, '.')[1])

    # Task 1: 5400
    # Task 2: 1898