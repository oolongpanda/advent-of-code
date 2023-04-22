with open('input/day16.txt') as f:
    input = [l.strip() for l in f.readlines()]
    input = input[0]
    
    tobinary = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
    binary = ''
    for i in input:
        binary += tobinary[i]
    input = binary

    def todecimal(binary):
        decimal = 0
        for i in str(binary):
            decimal = decimal * 2
            decimal += int(i)
        return decimal

    # print (input)

    def parse(packet, oldversionsum, literalvalues):
        packet = str(packet)
        versionsum = oldversionsum + todecimal(packet[0:3])
        if todecimal(packet[3:6]) == 4:
            placement = 6
            bits = ''
            firstbit = int(packet[placement])
            if firstbit == 0:
                byte = packet[int(placement + 1):int(placement + 5)]
                bits += byte
                placement += 5
            while firstbit == 1:
                firstbit = int(packet[placement])
                byte = packet[int(placement + 1):int(placement + 5)]
                bits += byte
                placement += 5
            # print ('literalvalue', todecimal(bits))
            literalvalues += [todecimal(bits)]
            remaining = packet[placement:]
        
        typeID = todecimal(packet[3:6])
        if typeID != 4:
            # print('typeID', todecimal(packet[3:6]))
            if packet[6] == '0':
                length = todecimal(packet[7:22])
                # print ('0:', length, 'bits encoded')
                remainingafter = len(packet) - 22 - length
                c_remaining = packet[22:]
                c_literalvalues = []
                while len(c_remaining) != remainingafter:
                    c_versionsum, c_remaining, c_literalvalues = parse(c_remaining, versionsum, c_literalvalues)
                    versionsum = c_versionsum
                remaining = c_remaining
                literalvalues += [operators(typeID, c_literalvalues)]
            elif packet[6] == '1':
                subpackets = todecimal(packet[7:18])
                # print ('1:', subpackets, 'sub-packets encoded')
                c_remaining = packet[18:]
                c_literalvalues = []
                for i in range(subpackets):
                    c_versionsum, c_remaining, c_literalvalues = parse(c_remaining, versionsum, c_literalvalues)
                    versionsum = c_versionsum
                remaining = c_remaining
                literalvalues += [operators(typeID, c_literalvalues)]
            else:
                print ('AAAAGGGHHH')
        # print (literalvalues)
        return versionsum, remaining, literalvalues
    
    def operators(typeID, values):
        if typeID == 0:
            return sum(values)
        if typeID == 1:
            product = 1
            for i in values:
                product = product * i
            return product
        if typeID == 2:
            return min(values)
        if typeID == 3:
            return max(values)
        if typeID == 5:
            # ALWAYS has 2 subpackets
            if values[0] > values[1]:
                return 1
            else:
                return 0
        if typeID == 6:
            # ALWAYS has 2 subpackets
            if values[0] < values[1]:
                return 1
            else:
                return 0
        if typeID == 7:
            # ALWAYS has 2 subpackets
            if values[0] == values[1]:
                return 1
            else:
                return 0

    print('Task 1:', parse(input, 0, [])[0])
    print('Task 2:', parse(input, 0, [])[2][0])

# Task 1: 923
# Task 2: 258888628940
    


# First three bits = packet version
    # Task 1 asks for a sum of these

# Next three bits = packet type ID
    # type ID 4 represent a literal value
    # NOT 4 = operator (contains packet(s))

# Literal value (type ID 4)
    # groups of 5 bits
    # 1st bit = 1 if not the last group; = 0 if it is the last group
    # next four bits = next four didgits of a binary number (1000 and 1111 -> 10001111)

#  Operator (type ID not 4)
    # first bit = lenth type ID
    # if 0: next 15 bits = total length in bits of the sub-packets contained
    # if 1: next 11 bits = number of sub-packets immediately contained
    # Packet type IDs mean different things and act upon the values contained within it to produce a value
    
# The very end of the outermost layer might be padded out with 0