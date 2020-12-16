# 1부터 N까지 자연수 중에서 중복없이 M개를 고른 수열
def permutaion(k):
    if k == M:
        for i in range(len(order)):
            print(order[i], end= ' ')
        print()
    else:
        for i in range(N):
            if visit[i] == 1:
                continue
            visit[i] = 1
            order.append(arr[i])
            permutaion(k+1)
            visit[i] = 0
            order.pop()

N, M = map(int,input().split())
arr = [x for x in range(1,N+1)]
n = len(arr)
visit = [0] * n
order = []
permutaion(0)