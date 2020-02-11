N, L = map(int,input().split())
golds, slivers, browns = [], [], []
for _ in range(N):
    gold, sliver, brown = map(int,input().split())
    golds.append(gold)
    slivers.append(sliver)
    browns.append(brown)

golds[0] = golds[0] + L
print(golds, slivers, browns)
while True:
    for i in range(1,len(golds)):
        if golds[i] == golds[0]:




