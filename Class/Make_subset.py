ls = [1,2,3]
subset = []
n = len(ls)
for i in range(1 << n):
    line = []
    for j in range(n):
        tf = i & (1 << j)
        if tf:
            line.append(ls[j])
    subset.append(line)
print(subset)