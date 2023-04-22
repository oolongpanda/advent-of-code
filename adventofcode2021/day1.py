currentline = 1
increased = 0
with open('input/day1.txt') as f:
    lines = f.readlines()
    # print (lines[0])
    # print (lines[0][0])
    # print(line)
    # print (len(lines))


    while (currentline < len(lines)):
        current = int(lines[currentline].strip())
        previous = int(lines[currentline - 1].strip())
        if (current > previous):
            increased = increased + 1
        currentline = currentline + 1
    print("Task 1:", increased)


    currentline = 3
    increased = 0

    while (currentline < len(lines)):
        current = int(lines[currentline].strip())
        previous = int(lines[currentline - 3].strip())
        if (current > previous):
            increased = increased + 1
        currentline = currentline + 1
    print("Task 2:", increased