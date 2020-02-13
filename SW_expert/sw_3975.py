import sys
sys.stdin = open('input_3975.txt', 'r')
TC = int(input())
for tc in range(TC):
    a, b, c, d = map(int,input().split())
    if a == c:
        if b > d:
            print('#{} {}'.format(tc+1, 'ALICE'))
        elif b < d:
            print('#{} {}'.format(tc+1, 'BOB'))
        else:
            print('#{} {}'.format(tc + 1, 'DRAW'))
    else:
        if a / b < c / d:
            print('#{} {}'.format(tc+1, 'BOB'))
        elif a / b > c / d:
            print('#{} {}'.format(tc + 1, 'ALICE'))
        else:
            print('#{} {}'.format(tc+1, 'DRAW'))

