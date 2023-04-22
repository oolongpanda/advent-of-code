with open('input/day11.txt') as f:
    input = [l.strip() for l in f.readlines()]
    grid = []
    for line in input:
        x = []
        for character in line:
            x += [int(character)]
        grid += [x]
    
    nonflash = 1
    totalflash = 0
    step = 0
    while nonflash != 0:
        step += 1
        nonflash = 0
        newflash = 0
        for l, line in enumerate(grid):
            for o, octopus in enumerate(line):
                grid[l][o] += 1
                if grid[l][o] > 9:
                    grid[l][o] = 'flash'
                    newflash += 1
        while newflash > 0:
            totalflash += newflash
            newflash = 0
            for l, line in enumerate(grid):
                for o, octopus in enumerate(line):
                    if octopus != 'flash' and octopus != 'oldflash':
                        # down left yay
                        if l + 1 != len(grid) and o != 0 and grid[l + 1][o - 1] == 'flash':
                            grid[l][o] += 1
                        # down yay
                        if l + 1 != len(grid) and grid[l + 1][o] == 'flash':
                            grid[l][o] += 1
                        # down right yay
                        if l + 1 != len(grid) and o + 1 != len(line) and grid[l + 1][o + 1] == 'flash':
                            grid[l][o] += 1
                        # left yay
                        if o != 0 and grid[l][o - 1] == 'flash':
                            grid[l][o] += 1
                        # right yay
                        if o + 1 != len(line) and grid[l][o + 1] == 'flash':
                            grid[l][o] += 1
                        # up right yay
                        if l != 0 and o + 1 != len(line) and grid[l - 1][o + 1] == 'flash':
                            grid[l][o] += 1
                        # up yay
                        if l != 0 and grid[l - 1][o] == 'flash':
                            grid[l][o] += 1
                        # up left
                        if l != 0 and o != 0 and grid[l - 1][o - 1] == 'flash':
                            grid[l][o] += 1
            for l, line in enumerate(grid):
                for o, octopus in enumerate(line):
                    if octopus == 'flash':
                        grid[l][o] = 'oldflash'
                    if octopus != 'flash' and octopus != 'oldflash':
                        if octopus > 9:
                            grid[l][o] = 'flash'
                            newflash += 1
        for l, line in enumerate(grid):
            for o, octopus in enumerate(line):
                if octopus == 'flash' or octopus == 'oldflash':
                    grid[l][o] = 0
                if octopus != 'flash' and octopus != 'oldflash':
                    nonflash += 1
        if step == 100:
            task1 = totalflash

    print ('Task 1:', task1)
    print ('Task 2:', step)
    
    
    # Task 1: 1773
    # Task 2: 494
