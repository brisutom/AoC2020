import itertools
numbers = [int(x) for x in open("input.txt").readlines()]
preamble = 25
for i, num in enumerate(numbers[preamble:]):
    for pair in itertools.product(numbers[i:i+preamble], repeat=2):
        if sum(pair) == num:
            break
    else:
        print(num)
