import json
import re


def validate_entry(entry):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid = True
    for field in fields:
        if field not in list(entry.keys()):
            valid = False
            break

        if field == "byr":
            if len(entry[field]) != 4 or int(entry[field]) < 1920 or int(entry[field]) > 2002:
                valid = False
                break

        elif field == "iyr":
            if len(entry[field]) != 4 or int(entry[field]) < 2010 or int(entry[field]) > 2020:
                valid = False
                break

        elif field == "eyr":
            if len(entry[field]) != 4 or int(entry[field]) < 2020 or int(entry[field]) > 2030:
                valid = False
                break

        elif field == "hgt":
            m = re.fullmatch(r"\d+((in)|(cm))", entry[field])
            if not m:
                valid = False
                break
            else:
                if m.string[-2:] == "cm":
                    if int(m.string[:-2]) > 193 or int(m.string[:-2]) < 150:
                        valid = False
                        break
                elif m.string[-2:] == "in":
                    if int(m.string[:-2]) > 76 or int(m.string[:-2]) < 59:
                        valid = False
                        break
        elif field == "hcl":
            m = re.fullmatch(r"#[0-9a-f]{6}", entry[field])
            if not m:
                valid = False
                break
        elif field == "ecl":
            if entry[field] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                valid = False
                break
        elif field == "pid":
            m = re.fullmatch(r"[0-9]{9}", entry[field])
            if not m:
                valid = False
                break

    return valid


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
result = 0
for entry in data_json:
    if validate_entry(entry):
        result += 1

print(result)
