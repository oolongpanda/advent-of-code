with open('input/day21.txt') as f:
    input = [l.strip() for l in f.readlines()]
    start0 = int(input[0][-1])
    if start0 == 0:
        start0 = 10
    start1 = int(input[1][-1])
    if start1 == 0:
        start1 = 10
    # print(start0, start1)

    def practisediracdice(start0, start1):
        # track = [position, score], [position, score]
        track = [[start0, 0],[start1, 0]]
        roll = -3
        turn = 0
        count = 0
        maxscore = 0
        while maxscore < 1000:
            roll += 9
            while roll > 10:
                roll -= 10
            track[turn][0] += roll
            while track[turn][0] > 10:
                track[turn][0] -= 10
            track[turn][1] += track[turn][0]
            if track[turn][1] > maxscore:
                maxscore = track[turn][1]
                loser = (turn + 1) % 2
            count += 1
            turn = count % 2
        lowscore = track[loser][1]
        return(lowscore*count*3)
    


    def crunch(list, point):
        if point + 1 < len(list):
            if list[point] > 3:
                list[point] = 1
                list[point + 1] += 1
                if list[point + 1] > 3:
                    list = crunch(list, point+1)
        else:
            return 'end'
        return list

    threerolls = [1] * 3
    end= False
    possibilities = []
    while end == False:
        possibilities.append(threerolls.copy())
        threerolls[0] += 1
        threerolls = crunch(threerolls, 0)
        if threerolls == 'end':
            end = True
    print(possibilities)



    def diracturn(track, roll):
        #track:
        # ((pos0, score0),(pos1, score1),(nextturn))
        [a,b],[c,d],e = track
        track = [[a,b],[c,d],e]
        turn = track[2]
        track[turn][0] += sum(roll)
        while track[turn][0] > 10:
            track[turn][0] -= 10
        track[turn][1] += track[turn][0]
        if track[turn][1] >= 21:
            return 'winner', turn
        track[2] = (turn +1) % 2
        (a,b),(c,d),e = track
        track = ((a,b),(c,d),e)
        return(track)
    
    def diracdice(start0, start1):
        wins = [0,0]
        # get a list where you store game states and freq (dict, state: freq)
        # for pick one, remove it, and do all 27 outcomes
        # for each of them, if they're in the dict, cool, add the freq on and move on
        # if not, add it in
        # if it wins, keep track of winners
        # print(next(iter(dic1))) gets the first key
        games = {}
        #track:
        # ((pos0, score0),(pos1, score1),(nextturn))
        games.update({((start0, 0),(start1, 0),(0)):1})
        while len(games) > 0:
            current = next(iter(games))
            freq = games[current]
            del games[current]
            for roll in possibilities:
                outcome = diracturn(current, roll)
                if outcome[0] == 'winner':
                    wins[outcome[1]] += freq
                else:
                    if outcome in games:
                        games[outcome] += freq
                    else:
                        games.update({outcome:freq})
        return wins


    print('Task 1:', practisediracdice(start0, start1))
    print('Task 2:', max(diracdice(start0, start1)))


# Task 1: 1073709
# Task 2: 14874783049344