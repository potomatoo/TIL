N = int(input())
board = list(map(int, input().split()))
answer = 0
for i in range(N):
    now = i
    visit = [0] * N
    while True:
        if visit[now] == 2:
            answer = max(answer, visit.count(2))
            break
        visit[now] += 1
        now += board[now]
    print(visit)
print(answer)