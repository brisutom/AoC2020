passwords = [x.strip("\n") for x in open("input.txt").readlines()]
result = 0
for line in passwords:
    positions, letter, password = line.split()
    pos1, pos2 = [int(x) for x in positions.split("-")]
    if (password[pos1 - 1] == letter[0]) ^ (password[pos2 - 1] == letter[0]):
        result += 1

print(result)
