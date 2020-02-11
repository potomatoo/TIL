import sys
sys.stdin = open('./input/input_폭격작전_02.txt','r')

def is_range(ty,tx):
    if 0 <= ty <= N-1 and 0 <= tx <= N-1:
        return True
    else:
        return False

TC = int(input())
for tc in range(TC):
    N, M = map(int,input().split())

    b_map = []
    for _ in range(N):
        b_map.append(list(map(int,input().split())))

    b_where = []
    for _ in range(M):
        b_where.append(list(map(int,input().split())))

    dy = [0,1,1]
    dx = [1,1,0]
    changes = []
    for k in range(len(b_where)):
        change = []
        for i in range(3):
            ty = b_where[k][0] + dy[i]
            tx = b_where[k][0] + dx[i]
            change.append(ty)
        changes.append(change)
    print(changes)
