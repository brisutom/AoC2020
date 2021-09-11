def apply_mask(num, mask):
    num = format(num, '036b')
    new_num = ""
    for i in range(len(mask)):
        if mask[i] != "X":
            new_num += mask[i]
        else:
            new_num += num[i]

    return int(new_num, 2)


lines = [x.strip("\n") for x in open("input.txt").readlines()]
memory = dict()
for line in lines:
    if line[:4] == "mask":
        mask = line.split(" ")[-1]
    elif line[:3] == "mem":
        address = line.split("]")[0][4:]
        value = int(line.split(" ")[-1])
        memory[address] = apply_mask(value, mask)

print(sum(memory.values()))
