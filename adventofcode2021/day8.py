from typing import Counter


with open('input/day8.txt') as f:
    input = [l.strip() for l in f.readlines()]

    read = []
    for i in input:
        individualread = i.split(' | ')
        patterns = individualread[0].split()
        output = individualread[1].split()
        read = read + [[patterns, output]]
    # print (read)

    easycount = 0
    for line in read:
        for i in line[1]:
            if len(i) == 2 or len(i) == 3 or len(i) == 4 or len(i) == 7:
                easycount += 1
    print('Task 1:', easycount)

    outputsum = 0
    for line in read:
        occurences = []
        lengths = [''] * 8
        key = [''] * 7
        for signal in line[0]:
            lengths[len(signal)] += signal
            for s in signal:
                occurences += s
        # print(occurences)
        for o in occurences:
            if occurences.count(o) == 6:
                key[1] = o
            if occurences.count(o) == 4:
                key[4] = o
            if occurences.count(o) == 9:
                key[5] = o
            if occurences.count(o) == 8:
                if lengths[2].count(o) == 0:
                    key[0] = o
                elif lengths[2].count(o) == 1:
                    key[2] = o
                else:
                    print ('REEEE')
            if occurences.count(o) == 7:
                if lengths[4].count(o) == 0:
                    key[6] = o
                elif lengths[4].count(o) == 1:
                    key[3] = o
                else:
                    print ('REEEE pt 2')
        output = 0
        for digit in line[1]:
            output = output * 10
            a = False
            b = False
            c = False
            d = False
            e = False
            f = False
            g = False
            if digit.count(key[0]) == 1:
                a = True
            if digit.count(key[1]) == 1:
                b = True
            if digit.count(key[2]) == 1:
                c = True
            if digit.count(key[3]) == 1:
                d = True
            if digit.count(key[4]) == 1:
                e = True
            if digit.count(key[5]) == 1:
                f = True
            if key[6] in digit:
                g = True
            if a and b and c and e and f and g and not d:
                output += 0
            elif c and f and not a and not b and not d and not e and not g:
                output += 1
            elif a and c and d and e and g and not b and not f:
                output += 2
            elif a and c and d and f and g and not b and not e:
                output +=3
            elif b and c and d and f and not a and not e and not g:
                output +=4
            elif a and b and d and f and g and not c and not e:
                output += 5
            elif a and b and d and e and f and g and not c:
                output += 6
            elif a and c and f and not b and not d and not e and not g:
                output += 7
            elif a and b and c and  d  and e and f and g:
                output += 8
            elif a and b and c and  d and f and g and not e:
                output += 9
            else:
                print ('reeee')
        outputsum += output
    
    print ('Task 2:', outputsum)

    # Task 1: 397
    # Task 2: 1027422

    # 0-a = 8: 8 occurences and not in 1 (2 letters)
    # 1-b = 6: 6 occurences
    # 2-c = 8: 8 occurences and in 1 (2 letters)
    # 3-d = 7: 7 occurences and in 4 (4 letters)
    # 4-e = 4: 4 occurences
    # 5-f = 9: 9 occurences
    # 6-g = 7: 7 occurences and not in 4 (4 letters