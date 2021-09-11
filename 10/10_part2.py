numbers = sorted([int(x) for x in open("input.txt").readlines()])
numbers.append(max(numbers)+3)


def search_path(num, target, numbers):
    result = 0
    candidates = list(set(range(num + 1, num + 4)) & set(numbers))
    if target in candidates:
        return 1
    for candidate in candidates:
        result += search_path(candidate, target, numbers)
    return result


three_jumps = [0]
prev = 0
for num in numbers:
    if num-prev == 3:
        three_jumps.append(num)
    prev = num

result = 1
for i in range(1, len(three_jumps)):
    prev = three_jumps[i-1]
    num = three_jumps[i]
    result *= search_path(prev, num, numbers)

print(result)
