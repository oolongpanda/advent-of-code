import statistics

with open('input/day7.txt') as f:
    input = [l.strip() for l in f.readlines()]
    # input = ['16,1,2,0,4,2,7,1,2,14']
    input = [int(i) for i in (input[0].split(','))]

    median = int(statistics.median(i for i in input))
    fuel = 0
    for i in input:
        fuel += abs(i - median)
    print ('Centre (1):', median)
    print ('Task 1:', fuel)
    
    oldfuel = 0
    for i in range (min(input),max(input)):
        centre = i
        fuel = 0
        for i in input:
            steps = abs(i - centre)
            fuel += ((steps * (steps + 1)) / 2)
        if fuel < oldfuel or oldfuel == 0:
            oldfuel = fuel
            newcentre = centre
    
    print ('Centre (2):', centre)
    print ('Task 2:', int(oldfuel))

# Centre (1): 311
# Task 1: 347011
# Centre (2): 1898
# Task 2: 9836377