from time import perf_counter
from queue import PriorityQueue

t1 = perf_counter()
with open('input/day16.txt') as f:
    input = [l.split(' ') for l in f.read().split("\n")]


def parse(input):
    long_parsed = {}
    short_parsed = {}
    valve_vals = []
    for line in input:
        tovalves = []
        value = int(line[4][5:-1])
        for word in line[9:]:
            if word[-1] == ',':
                tovalves += [word[:-1]]
            else:
                tovalves += [word]
        if value != 0 or line[1] == 'AA':
            valve_vals += [(value, line[1])]
            short_parsed.update({line[1]: [value, tovalves]})
        long_parsed.update({line[1]: [value, tovalves]})
    valve_vals = sorted(valve_vals, reverse=True)
    paths = {}
    for startvalve in long_parsed:
        paths.update({startvalve: []})
        for endvalve in long_parsed:
            if endvalve != startvalve:
                paths.update({startvalve: paths[startvalve] + [(endvalve, (len(input)))]})
    changes = True
    while changes == True:
        changes = False
        for startvalve in paths:
            for e, end in enumerate(paths[startvalve]):
                endvalve, path_length = end
                if path_length > 1 and endvalve in long_parsed[startvalve][1]:
                    paths[startvalve][e] = (endvalve, 1)
                    changes = True
                elif path_length > 2:
                    for checkvalve in long_parsed[startvalve][1]:
                        for checkend, checklength in paths[checkvalve]:
                            if checkend == endvalve and path_length > checklength + 1:
                                paths[startvalve][e] = (endvalve, checklength + 1)
                                changes = True
    

    return paths, short_parsed, valve_vals


paths, short_parsed, valve_vals = parse(input)

print(paths)

def overestimation(state, elephant=False):
# state = [pressure released, [[my valve, time left], [elephant valve, time left]], valves open]
# state = [pressure released, [[my valve, time left]], valves open]
    if len(state[1]) == 2:
        elephant = True
    sofar = state[0]
    beento = state[2].copy()
    if elephant:
        times_left = [state[1][0][1], state[1][1][1]]
        for valve in valve_vals:
            if max(times_left) < 2:
                break
            if valve[1] not in beento:
                sofar += valve[0] * max(times_left)
                beento += [valve[1]]
                times_left = [max(times_left) - 2, min(times_left)]
    # if not elephant:
    #     timeleft = state[1][0][1]
    #     for valve in valve_vals:
    #         if timeleft < 2:
    #             break
    #         if valve[1] not in beento:
    #             sofar += valve[0] * timeleft
    #             beento += [valve[1]]
    #             timeleft -= 2
    if not elephant:
        timeleft = state[1][0][1]
        valvestoopen = list(filter(lambda x: x[1] not in beento, valve_vals))
        # while timeleft > 1:
        #     for v, valve in valvestoopen:
        #         if valve[]
        for valve in valve_vals:
            if timeleft < 2:
                break
            if valve[1] not in beento:
                sofar += valve[0] * timeleft
                beento += [valve[1]]
                timeleft -= 2

    #the hashed bit above works, this doesn't. 
    # I want to make a way to check you're not going somewhere faster than the distance you are from it
    # So i need a way of changing my parsing/length finding. 
    # I gotta make it easy to look up the distance between two vent nodes.
    # can i make a dict of dicts e.g. ength['AA']['AB']
    # or will i have to save loads of tuples in a dict like {('AA', 'AB'): 4, ('AB', 'AA'): 4}
    
    return sofar * -1


def part1(input, duration, elephant=False):
    paths, short_parsed, valve_vals = parse(input)
    q = PriorityQueue()
    if elephant:
        state = [0, [['AA', duration], ['AA', duration]], ['AA']]
    else:
        state = [0, [['AA', duration]], ['AA']]
    guess = overestimation(state, elephant)
    q.put([guess, state])


    while not q.empty():
        stateplus = q.get()
        state = stateplus[1]
        allzero = True
        for player in state[1]:
            if player[1] != 0:
                allzero = False
        if allzero:
            print('No minutes left')
            return state[0]
        if len(state[2]) == len(short_parsed):
            print('All valves open')
            return state[0]
        
# state = [pressure released, [[my valve, time left], [elephant valve, time left]], valves open]
# state = [pressure released, [[my valve, time left]], valves open]
# short_parsed = {valve: [pressure, [tunnels]]...}
# Shortest paths = {from: [(to, len), (to, len)...]...}

        been_somewhere = False
        for p, player in enumerate(state[1]):
            for destination, duration in paths[player[0]]:
                if destination in short_parsed:
                    if duration + 2 <= player[1] and destination not in state[2]:
                        newpressure = state[0] + short_parsed[destination][0] * (player[1] - duration - 1)
                        if elephant:
                            newstate = [newpressure, [[destination, player[1] - duration - 1], [state[1][(p+1) % 2][0], state[1][(p+1) % 2][1]]], state[2] + [destination]]
                        else:
                            newstate = [newpressure, [[destination, player[1] - duration - 1]], state[2] + [destination]]    
                        q.put([overestimation(newstate), newstate])
                        been_somewhere = True
            if not been_somewhere:
                if elephant:
                    newstate = [state[0], [[state[1][0][0], 0], [state[1][1][0], 0]], state[2]]
                else:
                    newstate = [state[0], [[state[1][0][0], 0]], state[2]]
                q.put([overestimation(newstate), newstate])
    return stateplus



print(f"Part 1: {part1(input, 30)}")

t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")


# print(f"Part 2: {part1(input, 26, True)}")


t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")


# No minutes left
# Part 1: 1595
# Elapsed time: 0.4217716999992262