instructions = [x.strip("\n") for x in open("input.txt").readlines()]
counts = [0] * len(instructions)
i = 0
acc = 0
while True:
    instruction = instructions[i]
    operation, arg = instruction.split(" ")
    arg = int(arg)
    counts[i] += 1
    if counts[i] > 1:
        print(acc)
        break

    if operation == "acc":
        acc += arg
        i += 1
    elif operation == "jmp":
        i += arg
    elif operation == "nop":
        i += 1
