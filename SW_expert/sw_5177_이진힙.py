import sys
sys.stdin = open('./input/input_5177.txt', 'r')

def push(item):
    global hsize
    hsize += 1
    H[hsize] = item
    c, p = hsize, hsize//2
    while p and H[c] < H[p]:
        H[c], H[p] = H[p], H[c]
        c = p
        p = c // 2

TC = int(input())
for tc in range(TC):
    N = int(input())
    arr = list(map(int,input().split()))
    H = [0] * 1000001
    hsize = 0
    for val in arr:
        push(val)
    ans = 0
    while N:
        N //= 2
        ans += H[N]
    
    print('#{} {}'.format(tc+1, ans))
