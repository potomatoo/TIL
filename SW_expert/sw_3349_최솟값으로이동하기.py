import sys
sys.stdin = open('./input/input_3349.txt','r')
from collections import deque

def get_int(k):
    return int(k)-1

TC = int(input())
for tc in range(TC):
    W, H, N = map(int,input().split())
    road = [[0 for _ in range(W)] for _ in range(H)]
    point = []
    for _ in range(N):
        point.append(list(map(get_int, input().split())))
    dy = [-1, 1, 0, 0, 1, -1]
    dx = [0, 0, -1, 1, 1, -1]
    ans = 0
    for i in range(len(point)-1):
        s_y = point[i][1]
        s_x = point[i][0]
        visit = [[0 for _ in range(W)] for _ in range(H)]
        D = [[0 for _ in range(W)] for _ in range(H)]
        Q = deque()
        Q.append((s_y,s_x))
        visit[s_y][s_x] = 1
        while Q:
            y, x = Q.popleft()
            if y == point[i+1][1] and x == point[i+1][0]:
                ans += D[point[i+1][1]][point[i+1][0]]
            for k in range(6):
                ty = y + dy[k]
                tx = x + dx[k]
                if ty < 0 or tx < 0 or ty > H - 1 or tx > W - 1:
                    continue
                if visit[ty][tx] == 0:
                    Q.append((ty,tx))
                    visit[ty][tx] = 1
                    D[ty][tx] = (D[y][x] + 1)

    print('#{} {}'.format(tc+1, ans))
