import sys
sys.stdin = open('./input/input_5189.txt', 'r')

def permutation(k, d):
    global ans

    if d > ans:
        return
    if k == N:
        if d + golf[order[k-1]-1][0] < ans:
            ans = d + golf[order[k-1]-1][0]
        return
    else:
        for i in range(len(arr)):
            if visit[i]:
                continue
            if len(order) > 0:
                if order[0] != 1:
                    continue
            visit[i] = 1
            order.append(arr[i])
            if k == 0:
                permutation(k+1, d)
            if k > 0:
                permutation(k+1, d + golf[order[k-1]-1][order[k]-1])
            visit[i] = 0
            order.pop()

TC = int(input())
for tc in range(TC):
    N = int(input())
    golf = []
    for _ in range(N):
        golf.append(list(map(int,input().split())))
    arr = [x for x in range(1, N+1)]
    order = []
    visit = [0] * (N+1)
    ans = 0xffffff
    permutation(0,0)
    print(f'#{tc+1} {ans}')