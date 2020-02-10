import sys
sys.stdin = open('input_5986.txt', 'r')
TC = int(input())
prime = []
for i in range(1, 1000):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
            continue
    if cnt == 2:
        prime.append(i)
for tc in range(TC):
    n = int(input())
    cnt = 0
    for i in range(len(prime)):
        for j in range(i,len(prime)):
            for k in range(j,len(prime)):
                if prime[i] + prime[j] + prime[k] == n:
                    cnt += 1

    print('#{} {}'.format(tc+1,cnt))
