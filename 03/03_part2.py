from functools import reduce
rights = [1, 3, 5, 7, 1]
downs = [1, 1, 1, 1, 2]


def count_trees(right, down):
    result = 0
    lines = [x.strip("\n") for x in open("input.txt").readlines()][::down]
    for i, line in enumerate(lines):
        x = (i * right) % len(line)
        if line[x] == "#":
            result += 1
    return result


results = list(count_trees(right, down) for (right, down) in zip(rights, downs))
print(results)
print(reduce((lambda x, y: x * y), results))
