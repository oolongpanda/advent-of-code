import statistics

with open('input/day3.txt') as f:
    input = [l.strip() for l in f.readlines()]
    # print (input[0])
    # print (input[0][0])
    # print (len(input))
    # print (len(input[0]))
    
    position = 0
    line = 0
    characters = []
    gammabits = []
    epsilonbits = []


    while (position < len(input[0].strip())):
        while (line < len(input)):
            characters.extend([int(input[line][position])])
            line = line + 1
        gammabit = statistics.mode(characters)
        # gammabit = statistics.mode([int(x[position]) for x in input])
        if (gammabit == 0):
            epsilonbit = 1
        else:
            epsilonbit = 0
        gammabits.extend([gammabit])
        epsilonbits.extend([epsilonbit])
        position = position + 1
        characters = [0]
        line = 0
    
    gammabits.reverse()
    epsilonbits.reverse()
    decimalgamma = 0
    decimalepsilon = 0

    position = 0
    while (position < len(gammabits)):
        decimalgamma = decimalgamma + (gammabits[position] * 2**position)
        position = position + 1

    
    position = 0
    while (position < len(epsilonbits)):
        decimalepsilon = decimalepsilon + (epsilonbits[position] * 2**position)
        position = position + 1

    print ('Task 1:', decimalgamma*decimalepsilon)
    
    #oxygen generator rating
    position = 0
    oxygen = input
    while (len(oxygen) != 1):
        line = 0
        oxygen0 = []
        oxygen1 = []
        while (line < len(oxygen)):
            if (int(oxygen[line][position]) == 0):
                oxygen0.extend([oxygen[line].strip()])
            else:
                oxygen1.extend([oxygen[line].strip()])
            line = line + 1
        if (len(oxygen0) > len(oxygen1)):
            oxygen = oxygen0
        else:
            oxygen = oxygen1
        position = position + 1
    # print ('Oxygen generator rating:', (oxygen[0]))

    
    position = 0
    oxygen = oxygen[0][::-1]
    decimaloxygen = 0
    while (position < len(oxygen)):
        decimaloxygen = decimaloxygen + (int(oxygen[position]) * 2**position)
        position = position + 1
    
    #co2 scrubber rating
    position = 0
    co2 = input
    while (len(co2) != 1):
        line = 0
        co20 = []
        co21 = []
        while (line < len(co2)):
            if (int(co2[line][position]) == 0):
                co20.extend([co2[line].strip()])
            else:
                co21.extend([co2[line].strip()])
            line = line + 1
        if (len(co20) <= len(co21)):
            co2 = co20
        else:
            co2 = co21
        position = position + 1
    # print ('CO2 scrubber rating:', (co2[0]))

    
    position = 0
    co2 = co2[0][::-1]
    decimalco2 = 0
    while (position < len(co2)):
        decimalco2 = decimalco2 + (int(co2[position]) * 2**position)
        position = position + 1
    # print (decimalco2)

    print ('Task 2:', decimaloxygen*decimalco2)
