import re
lines = [x.strip("\n") for x in open("input.txt").readlines()]
data = []
actual_line = []
for line in lines:
    if line != "":
        actual_line.append(line)
    else:
        data.append(actual_line)
        actual_line = []
else:
    data.append(actual_line)

fields, my_ticket, nearby = data
nearby = nearby[1:]
numbers = [int(x) for x in re.findall(r"\d+", "".join(fields))]
intervals = []
for i in range(0, len(numbers)-1, 2):
    intervals.append(range(numbers[i], numbers[i+1]+1))

result = []
for ticket in nearby:
    for value in ticket.split(","):
        tf = [int(value) in interval for interval in intervals]
        if True not in tf:
            result.append(int(value))

print(sum(result))
