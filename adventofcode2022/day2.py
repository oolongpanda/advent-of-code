from time import perf_counter
t1 = perf_counter()
with open('input/day2.txt') as f:
    input = [l.split(' ') for l in f.read().split('\n')]

def score1 (opponent, you):
    win  = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    choice = {'X': 1, 'Y': 2, 'Z': 3}
    score = choice[you]
    if win[opponent] == you:
        score += 6
    elif draw[opponent] == you:
        score += 3
    elif lose[opponent] != you:
        print('aagh')
    return score

def part1(input):
    totalscore = 0
    for game in input:
        totalscore += score1(*game)
    return totalscore

def score2(opponent, outcome):
    win  = {'A': 'B', 'B': 'C', 'C': 'A'}
    lose = {'A': 'C', 'B': 'A', 'C': 'B'}
    winpoints = {'Z': 6, 'Y': 3, 'X': 0}
    extrapoints = {'A': 1, 'B': 2, 'C': 3}
    score = winpoints[outcome]
    if outcome == 'Z':
        score += extrapoints[win[opponent]]
    elif outcome == 'X':
        score += extrapoints[lose[opponent]]
    elif outcome == 'Y':
        score += extrapoints[opponent]
    else:
        print('aaagh2')
    return score

def part2(input):
    totalscore = 0
    for game in input:
        totalscore += score2(*game)
    return totalscore


print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input)}")
    

t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")


# Part 1: 8890
# Part 2: 10238
# Elapsed time: 0.0039799001533538