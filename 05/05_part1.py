import math
lines = [x.strip("\n") for x in open("input.txt").readlines()]


def binary_search(seat, n):
    lower = 0
    higher = n-1
    for char in seat:
        if char == "F" or char == "L":
            higher = math.floor((lower+higher)/2)
        elif char == "B" or char == "R":
            lower = math.floor((lower+higher)/2)

    return higher


highest = -math.inf
for line in lines:
    row_chars = line[:7]
    col_chars = line[7:]
    row = binary_search(row_chars, 128)
    col = binary_search(col_chars, 8)
    seat_id = row * 8 + col
    if seat_id > highest:
        highest = seat_id

print(highest)
