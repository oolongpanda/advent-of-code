
with open('input/day17.txt') as f:
    input = [l.strip() for l in f.readlines()]
    input = input[0]

    lims = (input.split(':')[1].split(','))
    x1 = int(lims[0].split('..')[0].split('=')[1])
    x2 = int(lims[0].split('..')[1])
    y1 = int(lims[1].split('..')[0].split('=')[1])
    y2 = int(lims[1].split('..')[1])


    def trajectory(xvel, yvel):
        xpos = 0
        ypos = 0
        while 1 == 1:
            xpos += xvel
            ypos += yvel
            if xvel > 0:
                xvel -= 1
            yvel -= 1
            if xpos >= x1 and xpos <= x2 and ypos >= y1 and ypos <= y2:
                return 'hit', [xpos, ypos]
                break
            if xpos > x2 and ypos > y2:
                return 'overshot', [xpos, ypos]
                break
            if xpos < x1 and ypos < y1:
                return 'undershot', [xpos, ypos]
                break
            if xpos > x2 and ypos <= y2:
                return 'skipped', [xpos, ypos]
                break
            if xpos >= x1 and ypos < y1:
                return 'skipped', [xpos, ypos]
                break

    # print(trajectory(7,2))

    yvel = 0
    xvel = 0
    

    while True:
        stop = (xvel * (xvel + 1))/2
        if stop >= x1:
            xvelmin = xvel
            break
        xvel += 1
    xvelmax = x2


    
    yvelmax = -y1 -1
    yvelmin = y1
    print ('Task 1:', int((yvelmax * (yvelmax + 1))/2))
        

    startvels = []

    for y in range (yvelmin, yvelmax + 1):
        for x in range (xvelmin, xvelmax + 1):
            landing = trajectory(x, y)
            if landing[0] == 'hit':
                startvels += [[x, y]]
    
    print('Task 2:', len(startvels))

# Task 1: 35511
# Task 2: 3282


