arr = [69, 10, 30, 2, 16, 8, 31, 22]
N = len(arr)

for i in range(1, N):  # 1부터 N-1까지
    tmp = arr[i]
    print(arr[:i], arr[i:])
    j = i-1
    while j >= 0 and arr[j] > tmp:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = tmp

print(arr)