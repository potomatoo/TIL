TC = int(input())
for tc in range(TC):
    N = int(input())
    a = 1
    b = 3
    for _ in range(N//10-2):
        a, b = b, a*2+b
    print('#{} {}'.format(tc+1,b))
