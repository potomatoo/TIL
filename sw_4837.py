import sys
sys.stdin = open('input_4837.txt', 'r')

TC = int(input())
for tc in range(TC):
    N, K = map(int, input().split())
    ls = [x for x in range(1,13)]
    M = len(ls)
    result = []
    n_sum = 0
    for subset in range(1 << M):
        N_ls = []
        for i in range(M):
            if subset & (1 << i):
                N_ls.append(ls[i])
        if len(N_ls) == N:
            result.append(N_ls)
    for i in range(len(result)):
        if sum(result[i]) == K:
            n_sum += 1
    print('#{} {}'.format(tc+1, n_sum))