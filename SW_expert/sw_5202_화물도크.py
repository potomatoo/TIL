import sys
sys.stdin = open('./input/input_5202.txt', 'r')

TC = int(input())
for tc in range(TC):
    N = int(input())
    schedule = []
    for _ in range(N):
        s, e = map(int, input().split())
        schedule.append([s,e])
    cnt = 1
    schedule.sort(key=lambda x:x[1])

    k = 0
    for i in range(len(schedule)):
        if i >= k:
            for j in range(i+1, len(schedule)):
                if schedule[i][1] <= schedule[j][0]:
                    k = j
                    cnt += 1
                    break
    print(f'#{tc+1} {cnt}')