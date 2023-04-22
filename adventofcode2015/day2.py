from time import perf_counter
t1 = perf_counter()

with open('input/day2.txt') as f:
    input = [[int(x) for x in l.strip().split('x')] for l in f.readlines()]
    
    def wrappresent(dimensions):
        w, l, h = dimensions
        towrap = 2*(w*h + l*h + w*l) + int(w*l*h/max(w,l,h))
        return towrap
    
    def wrapall(all):
        total = 0
        for present in all:
            total += wrappresent(present)
        return total
    
    def ribbon(dimensions):
        w, l, h = dimensions
        length = w*l*h + 2*(w + h + l - max(w, l, h))
        return length
    
    def tieall(all):
        total = 0
        for present in all:
            total += ribbon(present)
        return total
    
    print('Part 1:', wrapall(input))
    print('Part 2:', tieall(input))

t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")

# Part 1: 1588178
# Part 2: 3783758
# Elapsed time: 0.00450920000002952