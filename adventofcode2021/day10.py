import statistics

with open('input/day10.txt') as f:
    input = [l.strip() for l in f.readlines()]
    # print (input)

    missing = []
    errorscore = 0
    for line in input:
        corrupted = False
        expected = []
        for l in line:
            if l == '(':
                expected += ')'
            elif l == '[':
                expected += ']'
            elif l == '{':
                expected += '}'
            elif l == '<':
                expected += '>'
            elif l == expected[len(expected) - 1]:
                expected.pop()
            else:
                if l == ')':
                    errorscore += 3
                elif l == ']':
                    errorscore += 57
                elif l == '}':
                    errorscore += 1197
                elif l == '>':
                    errorscore += 25137
                corrupted = True
                break
        if not corrupted:
            missing += [expected]
    print ('Task 1:', errorscore)
    
    allscores = []
    for line in missing:
        score = 0
        for c, character in enumerate(line):
            score *= 5
            if line[(-c - + 1)] == ')':
                score += 1
            elif line[(-c - + 1)] == ']':
                score += 2
            elif line[(-c - + 1)] == '}':
                score += 3
            elif line[(-c - + 1)] == '>':
                score += 4
        allscores += [score]

    print ('Task 2:', statistics.median(allscores))

# Task 1: 294195
# Task 2: 349080273