def dfs(y, x, k):
    if k == 6:
        one = ''
        for i in range(len(order)):
            one += str(order[i])
        answer.add(one)
        return

    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or ty > 4 or tx < 0 or tx > 4:
            continue
        order.append(board[ty][tx])
        dfs(ty, tx, k+1)
        order.pop()

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

answer = set()
order = []
board = []
for _ in range(5):
    board.append(list(map(int, input().split())))

for y in range(5):
    for x in range(5):
        dfs(y, x, 0)
print(len(answer))