import sys
sys.stdin = open('./input/input_5178.txt', 'r')

TC = int(input())
for tc in range(TC):
    N, M, L = map(int,input().split())
    tree = [[] for _ in range(N+1)]
    for _ in range(M):
        v, e = map(int,input().split())
        tree[v].append(e)

    if N % 2 == 1:
        for i in range(N,1,-2):
            tree[(i-1)//2] = tree[i] + tree[i-1]

    if N % 2 == 0:
        for i in range(N,1,-2):
            if i == N:
                tree[N//2] = tree[i]
            else:
                tree[i//2] = tree[i] + tree[i+1]

    print('#{} {}'.format(tc+1,sum(tree[L])))