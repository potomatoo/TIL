while True:
    N = int(input())
    if N == 0:
        break
    prime = [0] * (123456*2+1)
    for i in range(2, len(prime)):
        prime[i] = i
    for i in range(2, len(prime)):
        if prime[i] == 0:
            continue
        for j in range(i+i, len(prime), i):
            prime[j] = 0

    cnt = 0
    for i in range(N+1, (2*N+1)):
        if prime[i] != 0:
            cnt += 1
    print(cnt)