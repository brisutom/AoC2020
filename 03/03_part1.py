lines = [x.strip("\n") for x in open("input.txt").readlines()]
result = 0
for i, line in enumerate(lines):
    x = (i * 3) % len(line)
    if line[x] == "#":
        result += 1

print(result)
