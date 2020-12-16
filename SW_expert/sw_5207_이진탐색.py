import sys
sys.stdin = open('./input/input_5207.txt', 'r')

TC = int(input())
for tc in range(TC):
    N, M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = list(map(int,input().split()))

    cnt = 0
    for i in range(len(B)):
        l = 0
        r = N - 1
        flag = 0
        while l <= r:
            m = (l + r) // 2
            if B[i] >= A[m]:
                if B[i] == A[m]:
                    cnt += 1
                    break
                l = m + 1
                if flag == 1:
                    break
                flag = 1
            elif B[i] < A[m]:
                r = m - 1
                if flag == -1:
                    break
                flag = -1
    print(f'#{tc+1} {cnt}')


