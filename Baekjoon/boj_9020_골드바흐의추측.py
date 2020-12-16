TC = int(input())
for tc in range(TC):
    N = int(input())
    prime = [0] * 10001
    for i in range(2, len(prime)):
        prime[i] = i
    for i in range(2, len(prime)):
        if prime[i] == 0:
            continue
        for j in range(i+i, len(prime), i):
            prime[j] = 0
    for i in range(N // 2,-1,-1):
        if prime[i] != 0 and prime[N-i] != 0:
            print(i, N-i)
            break


