numbers = sorted([int(x) for x in open("input.txt").readlines()])
numbers.append(max(numbers) + 3)

prev = 0
diffs = []
for num in numbers:
    diffs.append(num-prev)
    prev = num

diff1_cnt = diffs.count(1)
diff3_cnt = diffs.count(3)
print(diff1_cnt * diff3_cnt)
