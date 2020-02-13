c_map = []
for _ in range(5):
    line = list(map(int, input().split()))
    c_map.append(line)
numbers = []
for _ in range(5):
    number = input().split()
    numbers += number
numbers = list(map(int, numbers))

cnt = 1

for n in range(len(numbers)):
    bingo = 0
    for y in range(len(c_map)):
        for x in range(len(c_map[y])):
            if c_map[y][x] == numbers[n]:
                c_map[y][x] = 0

    for y in range(len(c_map)):
        if sum(c_map[y]) == 0:
            bingo += 1
    if bingo >= 3:
        break
    for x in range(len(c_map[0])):
        sero = 0
        for y in range(len(c_map)):
            if c_map[y][x] != 0:
                sero += 1
        if sero == 0:
            bingo += 1
    if bingo >= 3:
        break

    degak = 0
    for y in range(len(c_map)):
        for x in range(len(c_map[y])):
            if x == y and c_map[y][x] == 0:
                degak += 1
    if degak == 5:
        bingo += 1

    if bingo >= 3:
        break

    degak2 = 0
    for y in range(len(c_map)):
        for x in range(len(c_map[y])):
            if x + y == 4 and c_map[y][x] == 0:
                degak2 += 1
    if degak2 == 5:
        bingo += 1

    if bingo >= 3:
        break

    cnt += 1
print(cnt)