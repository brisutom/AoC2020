from functools import reduce
lines = [x.strip("\n") for x in open("input.txt").readlines()]
data = []
group = []
for line in lines:
    if line != "":
        group.append(line)
    else:
        data.append(group)
        group = []
else:
    data.append(group)

result = 0
for group in data:
    consensus = reduce((lambda x, y: set(x) & set(y)), group)
    result += len(consensus)

print(result)
