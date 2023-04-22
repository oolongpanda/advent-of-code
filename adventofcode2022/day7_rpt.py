from time import perf_counter

t1 = perf_counter()
with open('input/day4.txt') as f:
    input = [l.split(' ') for l in f.read().split('\n')]

def parse (input):
    dir = []

t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")
