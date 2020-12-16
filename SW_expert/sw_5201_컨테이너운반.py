import sys
sys.stdin = open('./input/input_5201.txt', 'r')

TC = int(input())
for tc in range(TC):
    N, M = map(int,input().split())
    weight = list(map(int,input().split()))
    limit = list(map(int,input().split()))
    weight.sort(reverse=True)
    limit.sort(reverse=True)
    ans = 0
    for i in range(len(weight)):
        for j in range(len(limit)):
            if weight[i] <= limit[j]:
                limit[j] = 0
                ans += weight[i]
                break
    print(f'#{tc+1} {ans}')

