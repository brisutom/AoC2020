import itertools

numbers = [int(x) for x in open("input.txt").readlines()]
for (x, y) in itertools.product(numbers, repeat=2):
    if x+y == 2020:
        print(x*y)
        break
