import sys
sys.stdin = open('./input/input_4881.txt','r')

def permutation(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

TC = int(input())
for tc in range(TC):
    N = int(input())
    b_map = []

    for _ in range(N):
        b_map.append(list(map(int,input().split())))
    per = permutation([x for x in range(0,N)])
    sum_min = 10000000000
    print(per)
    print(b_map)
    for i in range(len(per)):
        sum_ = 0
        print()
        for y in range(N):
            if sum_ >= sum_min:
                break
            sum_ += b_map[y][per[i][y]]
            print(b_map[y][per[i][y]], end= ' ')

        if sum_ <= sum_min:
            sum_min = sum_

    print('#{} {}'.format(tc+1, sum_min))


