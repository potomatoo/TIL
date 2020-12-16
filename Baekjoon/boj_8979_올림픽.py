N, k = map(int,input().split())
ls = []
for _ in range(N):
    ls.append(list(map(int,input().split())))
g = sorted(ls, key = lambda  x: [x[1],x[2],x[3]] )
cnt = 1
same = 1
for i in range(len(g)-1, -1, -1):
    if g[i][0] == k:
        print(cnt)
        break
    if g[i][1:4] == g[i-1][1:4]:
        same += 1
    else:
        cnt += same
        same = 1
