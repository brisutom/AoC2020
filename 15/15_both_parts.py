import time
start = [0, 14, 1, 3, 7, 9]


def update_memory(memory, num, turn):
    try:
        memory[num].append(turn)
        if len(memory[num]) > 2:
            memory[num].pop(0)
    except KeyError:
        memory[num] = [turn]


def next_num(memory, last_num):
    try:
        return memory[last_num][1] - memory[last_num][0]
    except IndexError:
        return 0


turn = len(start)+1
last_num = start[-1]
memory = dict()
for num in start:
    memory[num] = [start.index(num)+1]

start_time = time.time()
while turn <= 2020:
    spoken = next_num(memory, last_num)
    update_memory(memory, spoken, turn)

    last_num = spoken
    turn += 1

print("Part 1: ", spoken)

while turn <= 30000000:
    if turn % 3000000 == 0:
        print(round(turn/30000000 * 100), "% done")
    spoken = next_num(memory, last_num)
    update_memory(memory, spoken, turn)

    last_num = spoken
    turn += 1

# part takes a bit under a minute, runs much faster in PyPy
print("Part 2: ", spoken)
print("Took ", time.time() - start_time, " seconds")
