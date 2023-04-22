from time import perf_counter
t1 = perf_counter()
with open('input/day6.txt') as f:
    input = [l.strip() for l in f.read()]

def main (input, length):
    for start, letter in enumerate(input[length:]):
        end = start + length
        letterset = set(input[start:end])
        if len(letterset) == length:
            return end
    raise Exception('No answer found')

print(f"Part 1: {main(input, 4)}")
print(f"Part 2: {main(input, 14)}")

t2 = perf_counter()
print(f"Elapsed time: {t2-t1}")

# Part 1: 1848
# Part 2: 2308
# Elapsed time: 0.00411749980412423