from contextlib import suppress
import numpy as np
from matplotlib import pyplot as plt


config = [x.strip("\n").replace(".", "-1 ").replace("L", "0 ").replace("#", "1 ") for x in open("input.txt").readlines()]
config = [np.fromstring(line, dtype=int, sep=' ') for line in config]
config = np.array(config)


def count_occupied(config, i, j):
    neighbors = []
    k = 0
    while i-k != 0 and j-k != 0:
        neighbors.append(config[i-1-k, j-1-k])
        if config[i-1-k, j-1-k] != -1:
            break
        k += 1
    k = 0
    while i-k != 0:
        neighbors.append(config[i-1-k, j])
        if config[i-1-k, j] != -1:
            break
        k += 1
    k = 0
    while i-k != 0:
        with suppress(IndexError):
            neighbors.append((config[i-1-k, j+1+k]))
            if config[i-1-k, j+1+k] != -1:
                break
        k += 1
    k = 0
    while j-k != 0:
        neighbors.append((config[i, j-1-k]))
        if config[i, j-1-k] != -1:
            break
        k += 1
    k = 0
    while j-k != 0 and i+1+k <= config.shape[0]:
        with suppress(IndexError):
            neighbors.append((config[i+1+k, j-1-k]))
            if config[i+1+k, j-1-k] != -1:
                break
        k += 1
    k = 0
    while j+k+1 <= config.shape[1]:
        with suppress(IndexError):
            neighbors.append((config[i, j+1+k]))
            if config[i, j+1+k] != -1:
                break
        k += 1
    k = 0
    while i+k+1 <= config.shape[0]:
        with suppress(IndexError):
            neighbors.append((config[i+1+k, j]))
            if config[i+1+k, j] != -1:
                break
        k += 1
    k = 0
    while i+k+1 <= config.shape[0] and j+k+1 <= config.shape[1]:
        with suppress(IndexError):
            neighbors.append((config[i+1+k, j+1+k]))
            if config[i+1+k, j+1+k] != -1:
                break
        k += 1

    return neighbors.count(1)


def update(config):
    new_config = config.copy()
    for i, line in enumerate(config):
        for j, seat in enumerate(line):
            if seat == 0 and count_occupied(config, i, j) == 0:
                new_config[i, j] = 1
            elif seat == 1 and count_occupied(config, i, j) >= 5:
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
