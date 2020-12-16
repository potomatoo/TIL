import sys
sys.stdin = open('./input/input_5209.txt', 'r')

def backtrack(idx, cost):
    global ans
    if cost > ans:
        return
    if idx == N:
        ans = min(cost, ans)
        return

    for i in range(N):
        if check[i] == 0:
            check[i] = 1
            backtrack(idx+1, cost+factory[idx][i])
            check[i] = 0


TC = int(input())
for tc in range(TC):
    N = int(input())
    factory = []
    for _ in range(N):
        factory.append(list(map(int,input().split())))
    check = [0] * N
    ans = 0xffffff
    backtrack(0, 0)
    print(f'#{tc+1} {ans}')
