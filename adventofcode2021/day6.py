with open('input/day6.txt') as f:
    input = [l.strip() for l in f.readlines()]
    input = (input[0].split(','))

    data = [0]*9
    for fish in input:
        data[int(fish)] +=1
    data2 = [i for i in data]
   
    order = [1, 2, 3, 4, 5, 6, 7, 8, 0]
   
    for i in range (80):
        # data = [data[i] for i in order]
        data = data[1:] + data[:1]
        data[6] += data[8]

    print ('Task 1:', sum(data))

    for i in range (256):
        data2 = [data2[i] for i in order]
        data2[6] += data2[8]

    print ('Task 2:', sum(data2))

# Task 1: 353079
# Task 2: 160540013003