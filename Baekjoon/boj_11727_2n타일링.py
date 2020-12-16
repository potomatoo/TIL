def get_taling(N):
    tali_memo = [0, 1, 3]
    if N >= 3:
        for i in range(3,N+1):
            tali_memo.append(tali_memo[i-1] + (2 * tali_memo[i-2]))
    return tali_memo[N]
N = int(input())

print(get_taling(N)%10007)