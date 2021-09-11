import itertools

numbers = [int(x) for x in open("input.txt").readlines()]
for (x, y, z) in itertools.product(numbers, repeat=3):
    if x + y + z == 2020:
        print(x * y * z)
        break
