import sys
sys.stdin = open('./input/input_2805.txt','r')

TC = int(input())
for tc in range(TC):
    N = int(input())
    a_map = [[] for _ in range(N)]
    for _ in range(N):
        line = input()
        for i in range(len(line)):
            a_map[i].append(int(line[i]))

    sum_ = 0
    k = 0
    for y in range(N//2+1):
        for x in range(N//2 - k,N//2 + (k+1)):
            sum_ += a_map[y][x]
        k += 1

    k = 0
    for y in range(N-1,N//2,-1):
        for x in range(N//2 - k, N//2 + (k+1)):
            sum_ += a_map[y][x]
        k += 1

    print('#{} {}'.format(tc+1, sum_))


