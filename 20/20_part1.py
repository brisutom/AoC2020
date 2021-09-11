import numpy as np

lines = [x.strip("\n").replace(".", "0").replace("#", "1") for x in open("input.txt").readlines()]
data = []
actual_line = []
ids = []
for line in lines:
    if line[:4] == "Tile":
        ids.append(line.split(" ")[1][:-1])
    elif line != "":
        actual_line.append(np.array(list(line), dtype=int))
    else:
        data.append(actual_line)
        actual_line = []
else:
    data.append(actual_line)


# really not proud of this
def fits_lr(A, B):
    if np.array_equal(A[:, -1], B[:, 0]):
        return True
    if np.array_equal(A[:, -1], B[:, 0][::-1]):
        return True
    if np.array_equal(A[:, -1], B[:, -1]):
        return True
    if np.array_equal(A[:, -1], B[:, -1][::-1]):
        return True
    if np.array_equal(A[:, 0], B[:, 0]):
        return True
    if np.array_equal(A[:, 0], B[:, 0][::-1]):
        return True
    if np.array_equal(A[:, 0], B[:, -1]):
        return True
    if np.array_equal(A[:, 0], B[:, -1][::-1]):
        return True
    if np.array_equal(A[:, -1][::-1], B[:, 0]):
        return True
    if np.array_equal(A[:, -1][::-1], B[:, 0][::-1]):
        return True
    if np.array_equal(A[:, -1][::-1], B[:, -1]):
        return True
    if np.array_equal(A[:, -1][::-1], B[:, -1][::-1]):
        return True
    if np.array_equal(A[:, 0][::-1], B[:, 0]):
        return True
    if np.array_equal(A[:, 0][::-1], B[:, 0][::-1]):
        return True
    if np.array_equal(A[:, 0][::-1], B[:, -1]):
        return True
    if np.array_equal(A[:, 0][::-1], B[:, -1][::-1]):
        return True
    return False


corners = []
for i in range(0, len(data)):
    cnt = 0
    for j in range(0, len(data)):
        if i != j:
            A = np.array(data[i])
            B = np.array(data[j])
            if fits_lr(A, B) or fits_lr(A.T, B) or fits_lr(A, B.T) or fits_lr(A.T, B.T):
                cnt += 1
    if cnt == 2:
        corners.append(int(ids[i]))

print(corners)
# print(np.prod(corners))
# numpy overflows, regular python doesn't
print(corners[0] * corners[1] * corners[2] * corners[3])
