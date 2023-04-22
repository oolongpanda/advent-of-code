with open('input/day14.txt') as f:
    input = [l.strip() for l in f.readlines()]
    
    polymer = {}
    rules = {}
    combos = []
    letters = []
    for i in input[2:]:
        rule = i.split(' -> ')
        rules.update({rule[0]:rule[1]})
        combos += [rule[0]]

    firstletters = {input[0][-1]:{input[0][-1]}}
    letters += input[0][-1]
    for combo in combos:
        polymer.update({combo:0})
        #here's the weird one
        polymer.update({(input[0][-1]):1})
        if combo[0] in firstletters:
            newset = firstletters[combo[0]]
            newset.update({combo})
            dict.update({combo[0]:newset})
        else:
            firstletters.update({combo[0]:{combo}})
            letters += combo[0]
    
    masternew = polymer.copy()
     
    for r, residue in enumerate(input[0][0:-1]):
        pair = input[0][r] + input[0][r+1]
        if pair in polymer:
            polymer.update({pair:polymer[pair] + 1})
    
    for i in range(0,10):
        new = masternew.copy()
        for pair in combos:
            middle = rules[pair]
            newpair1 = pair[0] + middle
            newpair2 = middle + pair[1]
            amount = polymer[pair]
            new.update({newpair1:(new[newpair1] + amount)})
            new.update({newpair2:(new[newpair2] + amount)})
        polymer = new.copy()
    
    sums = []
    for letter in letters:
        total = 0
        for item in firstletters[letter]:
            total += polymer[item]
        sums += [total]

    print ('Task 1:', max(sums) - min(sums))
    
    for i in range(0,30):
        new = masternew.copy()
        for pair in combos:
            middle = rules[pair]
            newpair1 = pair[0] + middle
            newpair2 = middle + pair[1]
            amount = polymer[pair]
            new.update({newpair1:(new[newpair1] + amount)})
            new.update({newpair2:(new[newpair2] + amount)})
        polymer = new.copy()
    
    sums = []
    for letter in letters:
        total = 0
        for item in firstletters[letter]:
            total += polymer[item]
        sums += [total]
        
    print ('Task 2:', max(sums) - min(sums))

    # Task 1: 3009
    # Task 2: 345982253945