from collections import deque
N, k = map(int,input().split())
queue = deque([x for x in range(1,N+1)])

print('<',end = '')
while queue:
    queue.rotate(-(k-1))
    v = queue.popleft()
    if len(queue) == 0:
        print('{}'.format((v)),end='')
    else:
        print('{}, '.format(v), end='')
print('>')

