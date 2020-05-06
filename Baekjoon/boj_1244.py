l_swich = int(input())
swich = list(map(int,input().split()))
n = int(input())
for _ in range(n):
    sex, num = map(int, input().split())
    num = num - 1
    if sex == 1:
        for i in range(1, len(swich)+1):
            if i % (num+1) == 0:
                if swich[i-1] == 0:
                    swich[i-1] = 1
                else:
                    swich[i-1] = 0
    else:
        for i in range(1,l_swich):
            if num == 0 or num == l_swich-1:
                break
            if num - i < 0 or num + i > l_swich-1:
                break
            if swich[num - i] != swich[num + i]:
                break
            if swich[num - i] == swich[num + i]:
                if swich[num - i] == 0:
                    swich[num - i], swich[num + i] = 1, 1
                else:
                    swich[num - i], swich[num + i] = 0, 0

        if swich[num] == 1:
            swich[num] = 0
        else:
            swich[num] = 1

for i in range(1,l_swich+1):
    if i % 20 == 0:
        print(swich[i-1])
        continue
    print(swich[i-1], end=' ')