import itertools
numbers = [int(x) for x in open("input.txt").readlines()]
preamble = 25
invalid = -1
for i, num in enumerate(numbers[preamble:]):
    for pair in itertools.product(numbers[i:i+preamble], repeat=2):
        if sum(pair) == num:
            break
    else:
        invalid = num

for i in range(len(numbers)):
    inner_sum = 0
    j = 0
    invalid_range = []
    while inner_sum <= invalid:
        inner_sum += numbers[i+j]
        invalid_range.append(numbers[i+j])
        j += 1
        if inner_sum == invalid:
            print(min(invalid_range)+max(invalid_range))
            quit()
