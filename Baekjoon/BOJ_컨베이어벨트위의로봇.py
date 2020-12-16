from collections import deque

N, K = map(int, input().split())

lin = list(map(int, input().split()))
line = deque()
for i in range(len(lin)):
    line.append((lin[i], 0))
line.rotate(1)
print(line)
while True:
    if line.count(0) >= K:
        break
    line.rotate(1)
    if line[0][1] == 0:
        line[0][1] = 1
    



