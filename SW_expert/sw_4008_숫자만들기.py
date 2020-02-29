import sys
sys.stdin = open('./input/input_4008.txt','r')

def max_cal(k):
    global ans
    global max_ans
    if max_ans < ans:
        return
    if k == N:
        ans = order[0]
        for i in range(1, len(order)):
            if cal[i-1] == '+':
                ans += order[i]
            elif cal[i-1] == '-':
                ans -= order[i]
            elif cal[i-1] == '*':
                ans *= order[i]
            elif cal[i-1] == '/':
                ans //= order[i]
        max_ans = max(ans, max_ans)
        return
    else:
        for i in range(N):
            if visit[i] == 1:
                continue
            visit[i] = 1
            order.append(nums[i])
            max_cal(k+1)
            visit[i] = 0
            order.pop()

def min_cal(k):
    global ans
    global min_ans

    if min_ans > ans:
        return

    if k == N:
        ans = order[0]
        for i in range(1, len(order)):
            if cal[i-1] == '+':
                ans += order[i]
            elif cal[i-1] == '-':
                ans -= order[i]
            elif cal[i-1] == '*':
                ans *= order[i]
            elif cal[i-1] == '/':
                ans //= order[i]
        max_ans = max(ans, max_ans)
        return

    else:
        for i in range(N):
            if visit[i] == 1:
                continue
            visit[i] = 1
            order.append(nums[i])
            permutation(k+1)
            visit[i] = 0
            order.pop()

TC = int(input())
for tc in range(TC):
    N = int(input())
    d = ['+', '-', '*', '/']
    k = list(map(int,input().split()))
    cal = []
    for i in range(len(d)):
        if k[i] == 0:
            continue
        for _ in range(k[i]):
            cal.append(d[i])
    nums = list(map(int,input().split()))
    visit = [0] * N
    order = []
    ans = 0
    max_ans = 0
    max_cal(0)
    anx = 0
    min_ans = 0xffffffff
    