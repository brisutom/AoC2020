from contextlib import suppress
import numpy as np
from matplotlib import pyplot as plt


config = [x.strip("\n").replace(".", "-1 ").replace("L", "0 ") for x in open("input.txt").readlines()]
config = [np.fromstring(line, dtype=int, sep=' ') for line in config]
config = np.array(config)


def count_occupied(config, i, j):
    neighbors = []

    if i != 0 and j != 0:
        neighbors.append(config[i - 1, j - 1])
    if i != 0:
        neighbors.append(config[i - 1, j])
        with suppress(IndexError):
            neighbors.append((config[i - 1, j + 1]))
    if j != 0:
        neighbors.append((config[i, j - 1]))
        with suppress(IndexError):
            neighbors.append((config[i+1, j - 1]))
    with suppress(IndexError):
        neighbors.append((config[i, j + 1]))
    with suppress(IndexError):
        neighbors.append((config[i+1, j]))
    with suppress(IndexError):
        neighbors.append((config[i+1, j + 1]))

    return neighbors.count(1)


def update(config):
    new_config = config.copy()
    for i, line in enumerate(config):
        for j, seat in enumerate(line):
            if seat == 0 and count_occupied(config, i, j) == 0:
                new_config[i, j] = 1
            elif seat == 1 and count_occupied(config, i, j) >= 4:
                new_config[i, j] = 0
    return new_config


while True:
    new_config = update(config)
    if np.array_equal(new_config, config):
        break
    config = new_config

print(np.count_nonzero(config == 1))
plt.imshow(update(update(config)), interpolation='nearest')
plt.show()
