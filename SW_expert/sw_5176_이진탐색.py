import sys
sys.stdin = open('./input/input_5176.txt', 'r')

def push(item, N):
    global cnt
    if item <= N:
        push(item * 2, N)
        H[item] = cnt
        cnt += 1
        push(item * 2 + 1, N)

TC = int(input())
for tc in range(TC):
    N = int(input())
    H = [0] * (N+1)
    cnt = 1
    push(1, N)
    print('#{} {} {}'.format(tc+1, H[1], H[N//2]))
