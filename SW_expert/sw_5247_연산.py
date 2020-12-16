import sys
sys.stdin = open('./input/input_5247.txt', 'r')
from _collections import deque

TC = int(input())
for tc in range(TC):
    N, M = map(int,input().split())
    visit = [0] * 1000001
    arr = ['1', '-1', '2', '-10']
    Q = deque()
    Q.append((N, 0))

    while Q:
        cal, d = Q.popleft()
        if cal == M:
            print('#{} {}'.format(tc+1, d))
            break
        for i in range(len(arr)):
            if arr[i] == '1':
                if 0 < cal + 1 <= 1000000 and not visit[cal+1]:
                    Q.append((cal+1, d+1))
                    visit[cal+1] = 1
            elif arr[i] == '-1':
                if 0 < cal - 1 <= 1000000 and not visit[cal-1]:
                    Q.append((cal-1, d+1))
                    visit[cal - 1] = 1
            elif arr[i] == '2' :
                if 0 < cal * 2 <= 1000000 and not visit[cal*2]:
                    Q.append((cal*2, d+1))
                    visit[cal * 2] = 1
            else:
                if 0 < cal - 10 <= 1000000 and not visit[cal-10]:
                    Q.append((cal-10, d+1))
                    visit[cal - 10] = 1
