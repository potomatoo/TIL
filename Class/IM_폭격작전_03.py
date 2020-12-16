import sys
sys.stdin = open('./input/input_폭격작전_03.txt','r')

TC = int(input())

def is_range(ty, tx):
    if 0 <= ty <= N-1 and 0 <= tx <= N-1:
        return True
    else:
        return False

for tc in range(TC):
    N, M = map(int,input().split())
    b_map = []
    for _ in range(N):
        b_map.append(list(map(int,input().split())))
    bomb = [[0 for _ in range(N)] for _ in range(N)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    sum_ = 0
    for _ in range(M):
        b_y, b_x = map(int,input().split())
        if not bomb[b_y][b_x]:
            sum_ += b_map[b_y][b_x]
            bomb[b_y][b_x] = 1
        for i in range(4):
            ty = b_y + dy[i]
            tx = b_x + dx[i]
            if not is_range(ty, tx):
                continue
            while True:
                if not bomb[ty][tx]:
                    sum_ += b_map[ty][tx]
                    bomb[ty][tx] = 1
                ty = ty + dy[i]
                tx = tx + dx[i]
                if not is_range(ty,tx):
                    break
    print('#{} {}'.format(tc+1,sum_))