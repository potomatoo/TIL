N = int(input())
num = list(map(int,input().split()))
do_ls = list(map(int,input().split()))

arr = num
result = [arr[:]]
c = [0] * len(arr)
i = 0
print(result)
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
print(result)