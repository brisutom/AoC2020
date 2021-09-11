import math
lines = [x.strip("\n") for x in open("input.txt").readlines()]
instructions = [(line[0], int(line[1:])) for line in lines]


def add_points(a, b):
    return tuple(map(lambda x, y: x+y, a, b))


def rotate_point(p, theta):
    theta = math.radians(theta)
    x = round(p[0]*math.cos(theta) - p[1]*math.sin(theta))
    y = round(p[0]*math.sin(theta) + p[1]*math.cos(theta))
    return x, y


point = (0, 0)
offset = (10, 1)

for inst in instructions:
    action = inst[0]
    value = inst[1]

    if action == "N":
        offset = add_points(offset, (0, value))
    elif action == "S":
        offset = add_points(offset, (0, -value))
    elif action == "E":
        offset = add_points(offset, (value, 0))
    elif action == "W":
        offset = add_points(offset, (-value, 0))
    elif action == "L":
        offset = rotate_point(offset, value)
    elif action == "R":
        offset = rotate_point(offset, -value)
    elif action == "F":
        for i in range(value):
            point = add_points(point, offset)


print(abs(point[0]) + abs(point[1]))
