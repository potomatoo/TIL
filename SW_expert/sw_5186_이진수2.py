import sys
sys.stdin = open('./input/input_5186.txt', 'r')

def Binary(n):
    ans = ''
    cnt = 0
    while True:
        k = n * 2

        if k == 1:
            ans += '1'
            break

        if k > 1:
            ans += '1'
            n = k - 1
        else:
            ans += '0'
            n = k
        cnt += 1

        if cnt >= 13:
            return 'overflow'
    return ans

TC = int(input())
for tc in range(TC):
    N = float(input())
    print(f'#{tc+1} {Binary(N)}')
