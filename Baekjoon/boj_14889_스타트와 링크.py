from itertools import combinations

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

people = [x for x in range(N)]
combination = list(combinations(people, N//2))
answer = 1e9
for com in combination:
    team1 = 0
    team2 = 0
    for y in range(N):
        for x in range(N):
            if y == x:
                continue
            if y in com and x in com:
                team1 += board[y][x]
            elif y not in com and x not in com:
                team2 += board[y][x]

    mid_answer = abs(team1 - team2)
    answer = min(mid_answer, answer)
print(answer)

