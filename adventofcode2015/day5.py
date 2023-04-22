from time import perf_counter
t1 = perf_counter()
with open('input/day5.txt') as f:
    input = [l.strip() for l in f.readlines()]


    def naughtynice1(words):
        vowels = 'aeiou'
        badcombos = ['ab', 'cd', 'pq', 'xy']
        goodwords = 0
        for word in words:
            double = False
            nobads = True
            if word[-1] in vowels:
                vowelcount = 1
            else:
                vowelcount = 0
            for l, letter in enumerate(word[:-1]):
                if letter in vowels:
                    vowelcount += 1
                if letter == word[l+1]:
                    double = True
                if letter + word[l+1] in badcombos:
                    nobads = False
                    break
            if double and nobads and vowelcount >= 3:
                goodwords += 1
        return goodwords
    
    def naughtynice2(words):
        goodcombos = 0
        for word in words:
            twoslist = []
            twos = False
            owo = False
            for l, letter in enumerate(word[:-1]):
                if not twos:
                    pair = letter + word[l+1]
                    if l > 1:
                        if pair in twoslist[:-1]:
                            twos = True
                    twoslist += [pair]
                if not owo:
                    if l+2 < len(word):
                        if letter == word[l+2]:
                            owo = True
            if twos and owo:
                goodcombos += 1
        return goodcombos


    print('Part 1:', naughtynice1(input))
    print('Part 2:', naughtynice2(input))



t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")

# Part 1: 255
# Part 2: 55
# Elapsed time: 0.0083125000091968