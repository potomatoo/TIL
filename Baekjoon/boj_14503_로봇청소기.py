
N, M = map(int,input().split())
y, x, d = map(int,input().split())
y = y-1
x = x-1
c_map = []
for _ in range(N):
    c_map.append(list(map(int,input().split())))
visit = [[0 for _ in range(M)] for _ in range(N)]
if d == 0:
    dy = [0, -1, -1]
    dx = [-1, -1, 0]
if d == 1:
    dy = [-1, -1, 0]
    dx = [0, -1, -1]
if d == 2:
    dy = [0, -1, -1]
    dx = [1, 1, 0]
if d == 3:
    dy = [1, 1, 0]
    dx = [0, 1, 1]
