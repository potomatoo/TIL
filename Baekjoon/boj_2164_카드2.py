import collections

N = int(input())
deq = collections.deque([x for x in range(1,N+1)])
while len(deq) != 1:
    deq.popleft()
    deq.rotate(-1)
print(*deq)