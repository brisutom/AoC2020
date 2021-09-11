def apply_mask(address, mask):
    address = format(address, '036b')
    new_add = ""
    result = []
    for i in range(len(mask)):
        if mask[i] == "0":
            new_add += address[i]
        else:
            new_add += mask[i]
    for i in range(2**mask.count("X")):
        bits = format(i, '0' + str(mask.count("X")) + 'b')
        floating = new_add.split("X")
        variant = ""
        for j, part in enumerate(floating):
            variant += part
            if j < len(bits):
                variant += bits[j]
        result.append(variant)
    return [int(x, 2) for x in result]


lines = [x.strip("\n") for x in open("input.txt").readlines()]
memory = dict()
for line in lines:
    if line[:4] == "mask":
        mask = line.split(" ")[-1]
    elif line[:3] == "mem":
        address = int(line.split("]")[0][4:])
        value = int(line.split(" ")[-1])
        addresses = apply_mask(address, mask)
        for new_add in addresses:
            memory[str(new_add)] = value
print(sum(memory.values()))
