TC = int(input())

def recursive(n):
    if n == N // 10:
        return
    else:
        if arr[i] + arr[j] + arr[k] == N:
            if arr[j] != 0:
                result.append((arr[i], arr[j], arr[k]))
        recursive(n+1)




for tc in range(TC):
    N = int(input())
    arr = [10, 20, 20, 0]
    result = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if arr[i] + arr[j] + arr[k] == N:
                    if arr[j] != 0:
                        result.append((arr[i], arr[j], arr[k]))
    recursive(0)
    result = set(result)
    print(result)