from itertools import combinations

dy = [-1, 1, 0, 0, 0]
dx = [0, 0, -1, 1, 0]

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

flowers = []
for y in range(1, N-1):
    for x in range(1, N-1):
        mid_flower = []
        for i in range(5):
            ty = y + dy[i]
            tx = x + dx[i]
            mid_flower.append((ty, tx))
        flowers.append(mid_flower)

answer = 0xffffff
for flower in combinations(flowers, 3):
    mid_answer = 0
    check_dup = set()
    for i in range(len(flower)):
        for j in range(len(flower[i])):
            check_dup.add(flower[i][j])

    if len(check_dup) != 15:
        continue

    flag = True
    for y, x in check_dup:
        if mid_answer > answer:
            flag = False
            break
        mid_answer += board[y][x]
    if flag:
        answer = min(answer, mid_answer)
print(answer)