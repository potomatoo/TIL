TC = int(input())
c_map = [[0 for _ in range(101)] for _ in range(101)]
k = 1
for _ in range(TC):
    x, y, w, h = map(int, input().split())
    w = w - 1
    h = h - 1
    for i in range(len(c_map)):
        for j in range(len(c_map[i])):
            if y <= i <= y + h and x <= j <= x + w:
                c_map[i][j] = k
    k += 1

cnt = [0]*(k-1)
for z in range(k):
    for i in range(len(c_map)):
        for j in range(len(c_map[i])):
            if c_map[i][j] == z+1:
                cnt[z] += 1
for i in range(len(cnt)):
    print(cnt[i])

