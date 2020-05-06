import sys
sys.stdin = open('./input/input_5097.txt','r')
from _collections import deque
TC = int(input())
for tc in range(TC):
    N, M = map(int,input().split())
    Q = deque(map(int,input().split()))
    for _ in range(M):
        Q.append(Q[0])
        Q.popleft()

    print('#{} {}'.format(tc+1, Q[0]))