import sys
sys.stdin = open('./input/input_5185.txt', 'r')

TC = int(input())
for tc in range(TC):
    N, number = map(str, input().split())
    N = int(N)
    result = ''

    for i in range(N):
        if 48 <= ord(number[i]) <= 57:
            n = ord(number[i]) - 48
            ans = format(n, 'b')
            while len(ans) < 4:
                ans = '0' + ans
            result += ans
        else:
            n = ord(number[i]) - 55
            ans = format(n, 'b')
            while len(ans) < 4:
                ans = '0' + ans
            result += ans
    print(f'#{tc + 1} {result}')

