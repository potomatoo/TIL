import sys
sys.stdin = open('./input/input_폭격작전_04.txt','r')

'''
4 2
3 2 0 3
3 0 3 0
1 0 0 2
0 3 3 3
2 1 2
0 1 2
'''
TC = int(input())

def is_range(ty,tx):
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
    sum_ = 0
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for _ in range(M):
        b_y, b_x, b_s = map(int,input().split())
        if not bomb[b_y][b_x]:
            sum_ += b_map[b_y][b_x]
            bomb[b_y][b_x] = 1
        for i in range(4):
            ty = b_y + dy[i]
            tx = b_x + dx[i]
            if not is_range(ty,tx):
                continue
            for _ in range(b_s):
                if not bomb[ty][tx]:
                    sum_ += b_map[ty][tx]
                    bomb[ty][tx] = 1
                ty = ty + dy[i]
                tx = tx + dx[i]
                if not is_range(ty,tx):
                    break
    print('#{} {}'.format(tc+1,sum_))