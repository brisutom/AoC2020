instructions = [x.strip("\n") for x in open("input.txt").readlines()]


def terminates(instructions):
    counts = [0] * len(instructions)
    i = 0
    acc = 0

    while True:
        if i >= len(instructions):
            return True, acc
        instruction = instructions[i]
        operation, arg = instruction.split(" ")
        arg = int(arg)
        counts[i] += 1
        if counts[i] > 1:
            return False, acc

        if operation == "acc":
            acc += arg
            i += 1
        elif operation == "jmp":
            i += arg
        elif operation == "nop":
            i += 1


for j, line in enumerate(instructions):
    new_instructions = instructions.copy()
    operation, arg = line.split(" ")
    if operation == "nop":
        new_instructions[j] = "jmp " + arg
    elif operation == "jmp":
        new_instructions[j] = "nop " + arg
    if terminates(new_instructions)[0]:
        print(terminates(new_instructions)[1])
