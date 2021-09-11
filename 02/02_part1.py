passwords = [x.strip("\n") for x in open("input.txt").readlines()]
result = 0
for line in passwords:
    cntRange, letter, password = line.split()
    lwrCnt, highCnt = [int(x) for x in cntRange.split("-")]
    letterCnt = password.count(letter[0])
    if lwrCnt <= letterCnt <= highCnt:
        result += 1

print(result)
