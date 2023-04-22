import math

with open('input/day18.txt') as f:
    input = [l.strip() for l in f.readlines()]

    def parse(input):
        skip = False
        snailfishnumber = ['.','.']
        point = 0
        skipcount = 0
        for c, character in enumerate(input):
            if not skip:
                if character == '[':
                    if c != 0:
                        parsedpoint, justparsed = parse(input[c:])
                        snailfishnumber[point] = parsedpoint
                        skip = True
                elif character == ']':
                    return snailfishnumber, input[:c+1]
                elif character == ',':
                    point = 1
                else:
                    snailfishnumber[point] = int(character)
            else:
                skipcount += 1
                if skipcount == len(justparsed) - 1:
                    skipcount = 0
                    skip = False
        return snailfishnumber



    # EXPLODING
    def explode (input):
        path = [0,0,0,0]
        explosion = False

        while not explosion:
            a, b, c, d = path
            leftexplode = '.'
            rightexplode = '.'
            
            if type(input[a]) is list:
                if type(input[a][b])is list:
                    if type(input[a][b][c]) is list:
                        if type(input[a][b][c][d]) is list:
                            leftexplode = input[a][b][c][d][0]
                            rightexplode = input[a][b][c][d][1]
                            explosion = True
            
            if not explosion:
                if d == 0:
                    path = [a,b,c,1]
                elif c == 0:
                    path = [a,b,1,0]
                elif b == 0:
                    path = [a,1,0,0]
                elif a == 0:
                    path = [1,0,0,0]
                elif path == [1,1,1,1]:
                    return 'no explosion'
                else:
                    print('the path counter is broken')
        

        # print(input)
        # print(input[a][b][c][d])

        # Left explosion
        if path != [0,0,0,0]:
            if d == 1:
                if type(input[a][b][c][0]) is int:
                    input[a][b][c][0] += leftexplode
                elif type(input[a][b][c][0]) is list:
                    if type(input[a][b][c][0][1]) is int:
                        input[a][b][c][0][1] += leftexplode
                    else:
                       return 'the leftexplode has gone wrong 1' 
                else:
                    return 'the leftexplode has gone wrong 1'
            elif c == 1:
                if type(input[a][b][0]) is int:
                    input[a][b][0] += leftexplode
                elif type(input[a][b][0][1]) is int:
                    input[a][b][0][1] += leftexplode
                elif type(input[a][b][0][1][1]) is int:
                    input[a][b][0][1][1] += leftexplode
                else:
                    return 'the leftexplode has gone wrong 2'
            elif b == 1:
                if type(input[a][0]) is int:
                    input[a][0] += leftexplode
                elif type(input[a][0][1]) is int:
                    input[a][0][1] += leftexplode
                elif type(input[a][0][1][1]) is int:
                    input[a][0][1][1] += leftexplode
                elif type(input[a][0][1][1][1]) is int:
                    input[a][0][1][1][1] += leftexplode
                else:
                    return 'the leftexplode has gone wrong 3'
            elif a == 1:
                if type(input[0]) is int:
                    input[0] += leftexplode
                elif type(input[0][1]) is int:
                    input[0][1] += leftexplode
                elif type(input[0][1][1]) is int:
                    input[0][1][1] += leftexplode
                elif type(input[0][1][1][1]) is int:
                    input[0][1][1][1] += leftexplode
                elif type(input[0][1][1][1][1]) is int:
                    input[0][1][1][1][1] += leftexplode
                else:
                    return 'the leftexplode has gone wrong 4'  
            else:
                return 'the leftexplode has gone wrong 5'

        # Right explosion
        if path != [1,1,1,1]:

            if d == 0:
                if type(input[a][b][c][1]) is int:
                    input[a][b][c][1] += rightexplode
                elif type(input[a][b][c][1]) is list:
                    if type(input[a][b][c][1][0]) is int:
                        input[a][b][c][1][0] += rightexplode
                    else:
                        # print (input, input[a][b][c][1][0])
                        return 'the rightexplode has gone wrong 0' 
                else:
                    # print (input, input[a][b][c][1][0])
                    return 'the rightexplode has gone wrong 1'
            elif c == 0:
                if type(input[a][b][1]) is int:
                    input[a][b][1] += rightexplode
                elif type(input[a][b][1][0]) is int:
                    input[a][b][1][0] += rightexplode
                elif type(input[a][b][1][0][0]) is int:
                    input[a][b][1][0][0] += rightexplode
                else:
                    return 'the rightexplode has gone wrong 2'
            elif b == 0:
                if type(input[a][1]) is int:
                    input[a][1] += rightexplode
                elif type(input[a][1][0]) is int:
                    input[a][1][0] += rightexplode
                elif type(input[a][1][0][0]) is int:
                    input[a][1][0][0] += rightexplode
                elif type(input[a][1][0][0][0]) is int:
                    input[a][1][0][0][0] += rightexplode
                else:
                    return 'the rightexplode has gone wrong 3'
            elif a == 0:
                if type(input[1]) is int:
                    input[1] += rightexplode
                elif type(input[1][0]) is int:
                    input[1][0] += rightexplode
                elif type(input[1][0][0]) is int:
                    input[1][0][0] += rightexplode
                elif type(input[1][0][0][0]) is int:
                    input[1][0][0][0] += rightexplode
                elif type(input[1][0][0][0][0]) is int:
                    input[1][0][0][0][0] += rightexplode
                else:
                    return 'the rightexplode has gone wrong 4'
            else:
                return 'the rightexplode has gone wrong 5'
        
        input[a][b][c][d] = 0

        return input       
                
    # SPLITTING
    def split (input):
        path = [0,0,0,0]

        while True:
            a, b, c, d = path
            
            if type(input[a]) is int:
                if input[a] > 9:
                    down = int(input[a]/2)
                    up = int(math.ceil(input[a]/2))
                    input[a] = [down, up]
                    return input
            elif type(input[0]) is list:
                if type(input[a][b])is int:
                    if input[a][b] > 9:
                        down = int(input[a][b]/2)
                        up = int(math.ceil(input[a][b]/2))
                        input[a][b] = [down, up]
                        return input
                elif type(input[a][b]) is list:
                    if type(input[a][b][c]) is int:
                        if input[a][b][c] > 9:
                            down = int(input[a][b][c]/2)
                            up = int(math.ceil(input[a][b][c]/2))
                            input[a][b][c] = [down, up]
                            return input
                    elif type(input[a][b][c]) is list:
                        if type(input[a][b][c][d]) is int:
                            if input[a][b][c][d] > 9:
                                down = int(input[a][b][c][d]/2)
                                up = int(math.ceil(input[a][b][c][d]/2))
                                input[a][b][c][d] = [down, up]
                                return input
                            # else:
                                # print(input[a][b][c][d])
            
            if d == 0:
                path = [a,b,c,1]
            elif c == 0:
                path = [a,b,1,0]
            elif b == 0:
                path = [a,1,0,0]
            elif a == 0:
                path = [1,0,0,0]
            elif path == [1,1,1,1]:
                return 'no split'
            else:
                print('the path counter is broken')
            


    def reduce (input):
        exploding = True
        splitting = True
        while exploding or splitting:
            exp = explode(input)
            if exp == 'no explosion':
                # print(exp)
                exploding = False
                spl = split(input)
                if spl == 'no split':
                    splitting = False
                    # print(spl)
                elif type(spl) is list:
                    splitting = True
                    input = spl
                    # print ('after spl:', input)
            elif type(exp) is list:
                exploding = True
                input = exp
                # print('after exp:', exp)
        return input
    
    def magnitude(input):
        if type(input[0]) is int:
            a = input[0] * 3
        elif type(input[0]) is list:
            a = magnitude(input[0]) * 3
        if type(input[1]) is int:
            b = input[1] * 2
        elif type(input[1]) is list:
            b = magnitude(input[1]) * 2
        return a+b

    


    # ADDING

    for n, number in enumerate(input):
        if n == 0:
            snailfishnumber = parse(input[0])[0]
        else:
            snailfishnumber = [snailfishnumber] + [parse(input[n])[0]]
        snailfishnumber = reduce(snailfishnumber)
    


    print('Task 1:', magnitude(snailfishnumber))

    highestmagnitude = 0
    for n1 in input:
        for n2 in input:
            if n1 != n2:
                m = magnitude(reduce([parse(n1)[0]] + [parse(n2)[0]]))
                if m > highestmagnitude:
                    highestmagnitude = m
    
    print('Task 2:', highestmagnitude)

    # Task 1: 3763
    # Task 2: 466