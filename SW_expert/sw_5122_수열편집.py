import sys
sys.stdin = open('./input/input_5122.txt', 'r')

TC = int(input())
for tc in range(TC):
    N, M, L = map(int,input().split())
    arr = list(map(int,input().split()))
    for _ in range(M):
        do = input().split()
        if do[0] == 'I':
            arr.insert(int(do[1]), int(do[2]))
        elif do[0] == 'C':
            arr[int(do[1])] = int(do[2])
        elif do[0] == 'D':
            arr.pop(int(do[1]))
    if len(arr) < L:
        print('#{} {}'.format(tc+1, -1))
    else:
        print('#{} {}'.format(tc+1, arr[L]))

