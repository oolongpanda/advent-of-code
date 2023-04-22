from queue import PriorityQueue
import copy
from time import perf_counter


with open("input/day23.txt") as f:
    t1_start = perf_counter()

    input = [l.strip('\n') for l in f.readlines()]

    def parse(input):
        corridor = list(i for i in (input[1][1:12]))
        dip2 = [input[2][3], input[3][3]]
        dip4 = [input[2][5], input[3][5]]
        dip6 = [input[2][7], input[3][7]]
        dip8 = [input[2][9], input[3][9]]
        return[corridor, dip2, dip4, dip6, dip8]
    
    startstate = (parse(input))
    
    bigstartstate = copy.deepcopy(startstate)
    bigstartstate[1] = [startstate[1][0], 'D', 'D', startstate[1][1]]
    bigstartstate[2] = [startstate[2][0], 'C', 'B', startstate[2][1]]
    bigstartstate[3] = [startstate[3][0], 'B', 'A', startstate[3][1]]
    bigstartstate[4] = [startstate[4][0], 'A', 'C', startstate[4][1]]

    def visual(state):
        print('#############')
        b = '#'
        for i in state[0]:
            b += str(i)
        b += '#'
        print(b)
        for d in range(len(state[1])):
            if d == 0:
                print(f"###{state[1][d]}#{state[2][d]}#{state[3][d]}#{state[4][d]}###")
            else:
                print(f"  #{state[1][d]}#{state[2][d]}#{state[3][d]}#{state[4][d]}#")
        print('  #########')
        pass
    
    # visual(startstate)
    # visual(bigstartstate)

    energytype = {
        'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000
    }

    home = {
        'A': 2,
        'B': 4,
        'C': 6,
        'D': 8
    }

    dipletter = {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D'
    }    

    homedip = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4
    }    


    def happyamphipods (state):
        for i in state[0]:
            if i != '.':
                return False
        for d, dip in enumerate(state[1:]):
            for i in dip:
                if i != dipletter[d]:
                    return False
        return True

    def underestimation(state):
        cost = 0
        for s, spot in enumerate(state[0]):
            if spot != '.':
                cost += (abs(s - home[spot]) + 1) * energytype[spot] #corridor -> home
        for d, dip in enumerate(state[1:]):
            lowestwrong = 'no'
            for s, spot in enumerate(dip):
                if spot != dipletter[d]:
                    cost += s*energytype[dipletter[d]] #to bottom of dip
                    if spot != '.':
                        cost += (abs(home[dipletter[d]] - home[spot]) + 2 + s) * energytype[spot] #wrong dip -> home
                        lowestwrong = s #get out of the way
            if lowestwrong != 'no': #get out of the way
                for s, spot in enumerate(dip[:lowestwrong]):
                    if spot == dipletter[d]:
                        cost += (2*s + 4) * energytype[spot] #get out of the way
        return cost

    def broken(state):
        c3, c5, c7 = state[0][3], state[0][5], state[0][7]
        if c3 == 'D':
            if c5 == 'A' or c7 == 'A':
                return True
        if c3 == 'C':
            if c5 == 'A':
                return True
        if c5 == 'A':
            if c3 == 'C' or c3 == 'D' or c7 == 'B':
                return True
        if c5 == 'D':
            if c3 == 'C' or c7 == 'A' or c7 == 'B':
                return True
        if c7 == 'A':
            if c3 == 'D' or c5 == 'D':
                return True
        if c7 == 'B':
            if c5 == 'D':
                return True
        return False

    # print(f"Underestimate part 1 start: {underestimation(startstate)}")
    # print('Example part 1 answer:      12521')
    # print(f"Underestimate part 2 start: {underestimation(bigstartstate)}")
    # print('Example part 2 answer:      44169 \n')


    def amphipodsort(startstate):
        q = PriorityQueue()
        q.put([underestimation(startstate), startstate, 0])
        while not q.empty():
            stateplus = q.get()
            if(happyamphipods(stateplus[1])):
                return stateplus[2]
            state = stateplus[1].copy()
            # visual(state)
            for s, spot in enumerate(state[0]):
                if spot != '.':
                    freepath = True
                    for place in state[0][min(s, home[spot])+1:max(s, home[spot])]:
                        if place != '.':
                                freepath = False
                    if state[0][home[spot]] != '.':
                        print(f"ILLEGAL AMPHIPOD IN CORRIDOR SPOT {home[spot]}")
                        visual(state)
                        freepath  = False
                    if freepath:
                        makingthings = True
                        for d, depth in enumerate(state[homedip[spot]]):
                            if depth != '.'and depth != spot:
                                makingthings = False
                            elif depth == '.':
                                lowestfree = d
                        if makingthings:
                            newstate = copy.deepcopy(state)
                            newstate[0][s] = '.'
                            newstate[homedip[spot]][lowestfree] = spot
                            if not broken(newstate):
                                newcost = stateplus[2] + (abs(s-home[spot]) + 1 + lowestfree)*energytype[spot]
                                x = [newcost + underestimation(newstate), newstate, newcost]
                                if x not in q.queue:
                                    q.put(x)
                                    # print(x)
            for d, dip in enumerate(state[1:5]):
                hit = False
                for s, spot in enumerate(dip):
                    if not hit:
                        tocorridor = False
                        stuckbelow = False
                        if spot != dipletter[d] and spot != '.':
                            hit = True
                            gohome = True
                            for h, homespot in enumerate(state[homedip[spot]]):
                                if homespot == '.':
                                    lowestfree = h
                                elif homespot != spot:
                                    gohome = False
                            if gohome:
                                for i in state[0][min(2*d+2, home[spot]):max(2*d+2, home[spot])]:
                                    if i != '.':
                                        gohome = False
                            if gohome:
                                newstate = copy.deepcopy(state)
                                newstate[d+1][s] = '.'
                                newstate[homedip[spot]][lowestfree] = spot
                                if not broken(newstate):
                                    newcost = stateplus[2] + (abs(2*d+2 - home[spot]) + 2 + lowestfree + s)*energytype[spot]
                                    x = [newcost + underestimation(newstate), newstate, newcost]
                                    if x not in q.queue:
                                        q.put(x)
                                        # print(x)
                            else:
                                tocorridor = True
                        if spot == dipletter[d]:
                            hit = True
                            for i in dip[s:]:
                                if i != spot:
                                    stuckbelow = True
                            if stuckbelow:
                                tocorridor = True
                        if tocorridor:
                            start = 2*d + 2
                            corridor = [0,1,3,5,7,9,10]
                            i = start
                            blocked = False
                            while i < 10 and blocked == False:
                                i += 1
                                if i in corridor:
                                    if state[0][i] == '.':
                                        newstate = copy.deepcopy(state)
                                        newstate[d+1][s] = '.'
                                        newstate[0][i] = spot
                                        if not broken(newstate):
                                            newcost = stateplus[2] + (abs(start-i) + 1 + s)*energytype[spot]
                                            x= [newcost + underestimation(newstate), newstate, newcost]
                                            if x not in q.queue:
                                                q.put(x)
                                    else:
                                        blocked = True
                            i = start
                            blocked = False
                            while i > 0 and blocked == False:
                                i -= 1
                                if i in corridor:
                                    if state[0][i] == '.':
                                        newstate = copy.deepcopy(state)
                                        newstate[d+1][s] = '.'
                                        newstate[0][i] = spot
                                        if not broken(newstate):
                                            newcost = stateplus[2] + (abs(start-i) + 1 + s)*energytype[spot]
                                            x= [newcost + underestimation(newstate), newstate, newcost]
                                            if x not in q.queue:
                                                q.put(x)
                                    else:
                                        blocked = True

                    # ramblings of impossibility
                    #   2 pieces IN THE CORRIDOR need to cross eachother to free themselves
                            # if A and C are both between 2 and 6, and A is right of C, t's broken
                    #   dip X with a non-X amphipod
                    #       not enough spaces in the corridor for X to go (between either the nearest X or the end wall)

        print('There are more than 9,900 amphipod species')
        print('Amphipods are mostly detritivores or scavengers')
        print('Amphipods range from 1 to 340 mm in size')
        return '... and either my code is broken or these stubbon amphipods are stuck in a knot of their own making'

    print(f"Task 1: {amphipodsort(startstate)}")
    
    t1_stop = perf_counter()
    # print("Elapsed time:", t1_stop - t1_start, "\n")

    print(f"Task 2: {amphipodsort(bigstartstate)}")

    t1_stop = perf_counter()
    print("\nElapsed time:", t1_stop - t1_start)
    

# Task 1: 13066 (in 18.8 seconds)
# Task 2: 47328 (in 336.7 seconds)
# i fixed the corridor checking and now it's 89.9 seconds
# i fixed added in a broken state check and now it's 42.9 seconds
