w, h = map(int,input().split())
n = int(input())
garo = []
sero = []
for i in range(n):
    where, idx = map(int,input().split())
    if where == 0:
        garo.append(idx)
    else:
        sero.append(idx)

garo.append(0)
sero.append(0)
garo.append(h)
sero.append(w)

garo.sort()
sero.sort()
ls1 = []
ls2 = []
for i in range(len(garo)-1):
    ls1.append(garo[i+1] - garo[i])
for i in range(len(sero)-1):
    ls2.append(sero[i+1] - sero[i])
print(max(ls1)*max(ls2))