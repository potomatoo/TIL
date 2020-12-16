import sys
sys.stdin = open('./input/input_2817.txt','r')

def subset(num,N,S):
    cnt = 0
    for i in range(1 << N):
        one = []
        for j in range(N):
            tf = i & (1 << j)
            if tf:
                one.append(num[j])
        if sum(one) == S:
            cnt += 1
    return cnt

TC = int(input())
for tc in range(TC):
    N, S = map(int,input().split())
    num = list(map(int,input().split()))
    print('#{} {}'.format(tc+1, subset(num,N,S)))