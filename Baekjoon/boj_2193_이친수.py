def fibo(N):
    if N == 1:
        return 1
    if N == 2:
        return 1
    if fibo_memo[N] != 0:
        return fibo_memo[N]
    fibo_memo[N] = fibo(N-1) + fibo(N-2)
    return fibo_memo[N]

N = int(input())
fibo_memo = [0] * 91
print(fibo(N))