with open('input/day2.txt') as f:
    input = f.readlines()

    line = -1
    horizontal = 0
    depth = 0
    for current in input:
        direction = current.split()[0]
        magnitude = int(current.split()[1])
        if (direction == 'forward'):
            horizontal = horizontal + magnitude
        if (direction == 'down'):
            depth = depth + magnitude
        if (direction == 'up'):
            depth = depth - magnitude
    print ('Task 1:', horizontal * depth)

    line = -1
    horizontal = 0
    depth = 0
    aim = 0
    while (line + 1 < len(input)):
        line = line + 1
        current = input[line]
        direction = current.split()[0]
        magnitude = int(current.split()[1])
        if (direction == 'forward'):
            horizontal = horizontal + magnitude
            depth = depth + (aim * magnitude)
        if (direction == 'down'):
            aim = aim + magnitude
        if (direction == 'up'):
            aim = aim - magnitude
    print ('Task 2:', horizontal * depth)

# Task 1: 1604850
# Task 2: 168518610