import json

lines = [x.strip("\n") for x in open("input.txt").readlines()]
data = []
actual_line = ""
for line in lines:
    if line != "":
        actual_line += " " + line
    else:
        data.append(actual_line)
        actual_line = ""
else:
    data.append(actual_line)

data = ["{" + x.replace(" ", "\",\"").replace(":", "\":\"")[2:]+"\"}" for x in data]
data_json = [json.loads(x) for x in data]
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
result = 0
for entry in data_json:
    valid = True
    for field in fields:
        if field not in list(entry.keys()):
            valid = False
            break

    if valid:
        result += 1

print(result)
