lines = [x.strip("\n") for x in open("input.txt").readlines()]
instructions = [(line[0], int(line[1:])) for line in lines]


def add_points(a, b):
    return tuple(map(lambda x, y: x+y, a, b))


point = (0, 0)
orientation = 0

for inst in instructions:
    action = inst[0]
    value = inst[1]

    if action == "N":
        point = add_points(point, (0, value))
    elif action == "S":
        point = add_points(point, (0, -value))
    elif action == "E":
        point = add_points(point, (value, 0))
    elif action == "W":
        point = add_points(point, (-value, 0))
    elif action == "L":
        orientation += value
        orientation = orientation % 360
    elif action == "R":
        orientation -= value
        orientation = orientation % 360
    elif action == "F":
        if orientation == 0:
            point = add_points(point, (value, 0))
        elif orientation == 90:
            point = add_points(point, (0, value))
        elif orientation == 180:
            point = add_points(point, (-value, 0))
        elif orientation == 270:
            point = add_points(point, (0, -value))


print(abs(point[0]) + abs(point[1]))
