import sys
sys.stdin = open('./input/input_3752.txt','r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    test = list(map(int, input().split()))
    arr = []
    for i in range(N):
        arr = list(set(arr))
        if not arr:
            arr.append(test[i])
            continue

        x = len(arr)
        for a in range(x):
            s = arr[a] + test[i]
            arr.append(s)

        arr.append(test[i])

    ans = len(list(set(arr)))+1
    print('#{} {}'.format(t, ans))