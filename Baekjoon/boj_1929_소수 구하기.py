N, M = map(int,input().split())
num = 1000000
prime = [0] * 1000001
for i in range(2,len(prime)):
    prime[i] = i
for i in range(2,len(prime)):
    if prime[i] == 0:
        continue
    for j in range(i+i, len(prime), i):
        prime[j] = 0
for i in range(N,M+1):
    if prime[i] != 0:
        print(i)