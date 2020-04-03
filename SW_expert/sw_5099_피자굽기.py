import sys
sys.stdin = open('./input/input_5099.txt','r')
from _collections import deque
TC = int(input())
for tc in range(TC):
    N, M = map(int,input().split())
    pizza = list(map(int,input().split()))
    Q = deque()
    for i in range(N):
        Q.append([pizza[i], i])
    while len(Q) != 1:
        Q[0][0] = Q[0][0] // 2
        if Q[0][0] == 0:
            if N == M:
                Q.popleft()
            else:
                Q.popleft()
                Q.append([pizza[N], N])
                N += 1
        else:
            first = Q.popleft()
            Q.append(first)
    print('#{} {}'.format(tc+1, Q[0][1]+1))








