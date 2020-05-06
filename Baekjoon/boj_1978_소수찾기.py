N = int(input())
numbers = list(map(int,input().split()))
prime = [0] * 1001
for i in range(2,len(prime)):
    prime[i] = i
for i in range(2, len(prime)):
    if prime[i] == 0:
        continue
    for j in range(i+i, len(prime), i):
        prime[j] = 0
cnt = 0
for i in numbers:
    if prime[i] != 0:
        cnt += 1
print(cnt)
