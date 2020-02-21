def get_subset(arr):
    N = len(arr)
    subset = []
    for i in range(1 << N):
        line = []
        for j in range(N):
            tf = i & (1 << j)
            if tf:
                line.append(arr[j])
        subset.append(line)
    return subset




TC = int(input())
T, M = [], []
for _ in range(TC):
    t, m = map(int, input().split())
    T.append(t)
    M.append(m)
while True:
    for i in range(len(T)-1,-1,-1):




