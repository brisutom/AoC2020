lines = [x.strip("\n") for x in open("input.txt").readlines()]
data = []
actual_line = ""
for line in lines:
    if line != "":
        actual_line += line
    else:
        data.append(actual_line)
        actual_line = ""
else:
    data.append(actual_line)

counts = [len(set(x)) for x in data]
print(sum(counts))
